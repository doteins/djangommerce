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
