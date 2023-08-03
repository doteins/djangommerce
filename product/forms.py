from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ["category", "name", "description", "price", "image"]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      inputs_attributes = {
        "class": "w-full py-4 px-6 rounded-xl border border-gray-300", 
        "placeholder": f"{str.title(field)}", 
        "required": True, 
      }
      self.fields[str(field)].widget.attrs.update(inputs_attributes)
    
    # Overwrite properties
    self.fields["category"].empty_label = "-- Click here to choose the category --"
    self.fields["description"].widget.attrs.update({
      "rows": 8
    })
    self.fields["price"].widget.attrs.update({
      "min": 0
    })
    self.fields["image"].widget.attrs.update({
      "class": "w-full py-3 px-6 text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
    })

