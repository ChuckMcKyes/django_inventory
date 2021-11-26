from django import forms
from .models import InventoryItem

# these classes are for a calendar widget
# date input

class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'manufacturer', 'model', 'serial_number',
                  'purchase_date', 'purchase_price', 'notes', 'category', 'image']
        widgets = {
            'purchase_date': DateInput(),
        }
