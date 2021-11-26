from django.contrib import admin
from .models import InventoryItem, Categories

admin.site.register(InventoryItem)
admin.site.register(Categories)


class ItemsInline(admin.TabularInline):
    model = InventoryItem

# Define the admin class
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacturer', 'model', 'serial_number',
                    'purchase_date', 'notes', 'category', 'image')
    # Fields to include on the form, in order.
    fields = ['id', 'name', 'manufacturer', 'model', 'serial_number',
                    'purchase_date', 'notes', 'category', 'image']
    inlines = [ItemsInline]


class CategoriesInline(admin.TabularInline):
    model = Categories


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    # Fields to include on the form, in order.
    fields = ['id', 'category']
    inlines = [CategoriesInline]

