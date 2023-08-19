from django import forms
from .models import Item

''' 
If you are using a ModelForm then there is no any need
of playing with a cleaned_data dictionary because 
when you do form.save() it is already be matched 
and the cleaned data is saved.
'''

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
      "class": "file-input file-input-bordered file-input-accent w-full",
      "required": False
    })

class EditItemForm(NewItemForm):
  class Meta(NewItemForm.Meta):
    fields = NewItemForm.Meta.fields + ["status"]
    widgets = {
      'image': forms.FileInput(attrs={
        "class": "file-input file-input-bordered file-input-accent w-full",
        "required": False
      })
    }