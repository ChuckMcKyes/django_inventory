from django.shortcuts import render
from django.views import generic
from .models import Categories, InventoryItem
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UpdateForm
from .serializers import InventoryListSerializer, InventoryDetailSerializer, \
    CategoryListSerializer
from rest_framework import generics


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_items = InventoryItem.objects.all().count()
    num_categories = Categories.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # returns a user object. properties are username, password, email,
    # first_name, last_name (https://docs.djangoproject.com/en/3.1/topics/auth/default/)
    # The __str__ magic method returns username or 'AnonymousUser'
    current_user = request.user
    session_keys = request.session.keys()

    context = {
        'num_items': num_items,
        'num_categories': num_categories,
        'num_visits': num_visits,
        'current_user': current_user,
        'session_keys': session_keys
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ItemListView(generic.ListView):
    # model = InventoryItem  # don't need this because get_queryset
                             # was overridden
    paginate_by = 12

    # 'ordering' is a parameter from the url pattern
    def get_queryset(self):
        self.ordering = self.kwargs['ordering']
        # if url ends with query string '?shmee='tree'
        # it can be access as follows
        #print(self.request.GET.get('shmee'))
        if self.request.GET and self.request.GET.get('search'):
            self.queryset_local = InventoryItem.objects.order_by\
                (self.ordering).filter(name__icontains=
                self.request.GET.get('search'))
            # this must be done because pagination deletes the search
            # pagination will be reset upon a non-search list request
            self.paginate_by = 100
        else:
            self.queryset_local = InventoryItem.objects.order_by\
                (self.ordering)
        return self.queryset_local

    # adds 'ordering' as list_order in the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_order'] = self.ordering
        context['item_count'] = self.get_queryset().count()
        print(context)
        return context

    context_object_name = 'item_list'
    template_name = 'item_list.html'


class CategoryListView(generic.ListView):
    model = Categories
    paginate_by = 10
    # my own name for the list as a template variable
    context_object_name = 'category_list'
    # (default is the_model_name_list.html)
    template_name = 'category_list.html'


class ItemDetailView(generic.DetailView):
    model = InventoryItem
    context_object_name = 'item'
    template_name = 'item_detail.html'


# "create" and "update" views use the same template by default
# I created UpdateForm in forms.py to add a datepicker widget
class ItemCreateView(LoginRequiredMixin, CreateView):
    # because script alias root is /inventory
    login_url = '/inventory/accounts/login/'
    model = InventoryItem
    form_class = UpdateForm
    # in template: <form enctype="multipart/form-data" action="" method="post">
    template_name = 'item_update_form.html'


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    # because script alias root is /inventory
    login_url = '/inventory/accounts/login/'
    model = InventoryItem
    form_class = UpdateForm
    # in template: <form enctype="multipart/form-data" action="" method="post">
    template_name = 'item_update_form.html'


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    # because script alias root is /inventory
    login_url = '/inventory/accounts/login/'
    model = InventoryItem
    context_object_name = 'items'
    success_url = reverse_lazy('item_list', args=['name'])
    # default template is 'inventory/item_confirm_delete.html'
    template_name = 'item_confirm_delete.html'


# "create" and "update" views use the same template by default.
# The "update" view is not included because once a category is
# created and items are assigned to it, it cannot be deleted.
class CategoryCreateView(LoginRequiredMixin, CreateView):
    # because script alias root is /inventory
    login_url = '/inventory/accounts/login/'
    model = Categories
    fields = ['category']
    success_url = reverse_lazy('category_list')
    template_name = 'category_form.html'


"""  views for web api """
# ListAPIView for no form to enter new data
class InventoryListAPI(generics.ListAPIView):
    #queryset = InventoryItem.objects.all()
    serializer_class = InventoryListSerializer

    def get_queryset(self):
        # if url ends with query string '?shmee='tree'
        # it can be access as follows
        #print(self.request.GET.get('shmee'))
        # page links will result in 'search' = None
        if self.request.GET and self.request.GET.get('search'):
            self.queryset_local = InventoryItem.objects\
            .filter(name__icontains=
                self.request.GET.get('search'))
        else:
            self.queryset_local = InventoryItem.objects

        return self.queryset_local

class CategoryListAPI(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoryListSerializer

class InventoryDetailsAPI(generics.RetrieveAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryDetailSerializer
