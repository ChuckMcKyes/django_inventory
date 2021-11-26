from django.db import models
# Used to generate URLs by reversing the URL patterns:
from django.urls import reverse
from django.contrib.auth.models import User
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'inventory/media')

class Categories(models.Model):
    category = models.CharField(max_length=100, unique=True)

    # need this to show the category names in the InventoryList
    # API view
    def __str__(self):
        return self.category


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(null=True, blank=True,
                        max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Categories, to_field='category',
            related_query_name='categories', on_delete=models.SET_NULL,
            null=True, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        # string for representing the Model object:
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('item_detail', args=[str(self.id)])


# this is an example of creating a new user on the first run
if not User.objects.filter(username='scitizen').exists():
    # Create user and save to the database
    user = User.objects.create_user('scitizen', 'myemail@crazymail.com', 'mypassword')

    # Update fields and then save again
    user.first_name = 'Sue'
    user.last_name = 'Citizen'
    user.save()
