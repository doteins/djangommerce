from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

  # --- This is another way to add classes to the input fields ---
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      inputs_attributes = {
        "class": "w-full py-4 px-6 rounded-xl", 
        "placeholder": f"{str.title(field)}", 
        "required": True, 
      }
      self.fields[str(field)].widget.attrs.update(inputs_attributes)
