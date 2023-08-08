from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from product.models import Category, Item
from .forms import SignupForm, ContactForm

def index(request):
  items = Item.objects.filter(status=Item.AVAILABLE)[0:6] # This paginates the results to get only 6 items
  categories = Category.objects.all()
  ctx = {
    "categories": categories,
    "items": items,
  }
  return render(request, 'index.html', ctx)
 
def signup(request):
  categories = Category.objects.all()
  
  form = SignupForm()
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      form.cleaned_data()
      form.save()
      return redirect("/login/")
    
  ctx = { "form": form, "categories": categories, "title": "Sign up"}
  return render(request, 'generic_form.html', ctx)


@login_required
def user_items(request):
  user_items = Item.objects.filter(created_by=request.user)

  ctx = { "items": user_items, "title": "My items" }
  return render(request, "user_items.html", ctx)

def contact(request):
  form = ContactForm()
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data["name"]
      from_email = form.cleaned_data["from_email"]
      subject = form.cleaned_data["subject"]
      message = form.cleaned_data["message"]
      try:
        send_mail(
          from_email,
          subject,
          message,
          ["admin@example.com"], # Recipient email
          fail_silently=False,
        )
      except BadHeaderError:
        return HttpResponse("Invalid header found")

      ctx = { 
        "username": name, 
        "user_email": from_email, 
        "title": "Thank you" 
        }
      return render(request, "contact.html", ctx)
  ctx = { "form": form, "title": "Contact Us"}
  return render(request, 'generic_form.html', ctx)

def about(request):
  return render(request, 'about.html', {})
