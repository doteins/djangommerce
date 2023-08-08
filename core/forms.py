from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
        "class": "w-full py-4 px-6 rounded-xl border border-gray-300", 
        "placeholder": f"{str.title(field)}", 
        "required": True, 
      }
      self.fields[str(field)].widget.attrs.update(inputs_attributes)
    
    # Overwrite placeholder
    self.fields["password1"].widget.attrs.update({
      "placeholder": "Password",
    })
    self.fields["password2"].widget.attrs.update({
      "placeholder": "Confirm password",
    })

class LoginForm(AuthenticationForm):
  class Meta:
    model = User
    fields = ['email', 'password']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      inputs_attributes = {
        "class": "w-full py-4 px-6 rounded-xl border border-gray-300", 
        "placeholder": f"{str.title(field)}", 
        "required": True, 
      }
      self.fields[str(field)].widget.attrs.update(inputs_attributes)
 
class ContactForm(forms.Form):
  name = forms.CharField(max_length=120)
  from_email = forms.EmailField() # from_mail
  subject = forms.CharField(max_length=70)
  message = forms.CharField(widget=forms.Textarea)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      inputs_attributes = {
        "class": "w-full py-4 px-6 rounded-xl border border-gray-300", 
        "placeholder": f"{str.title(field)}", 
        "required": True, 
      }
      self.fields[str(field)].widget.attrs.update(inputs_attributes)
    
    # Overwrite placeholder
    self.fields["from_email"].widget.attrs.update({
      "placeholder": "Email",
    })
    self.fields["message"].widget.attrs.update({
      "rows": 7
    })
