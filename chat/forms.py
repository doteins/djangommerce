from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ('content',)
    widgets = {
      'content': forms.Textarea(attrs={
        'class': 'input input-bordered w-full text-xl',
        'placeholder': 'Message',
      })
    }