from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from product.models import Category, Item
from .forms import SignupForm

def index(request):
  items = Item.objects.filter(status=Item.AVAILABLE)[0:6] # This paginates the results to get only 6 items
  categories = Category.objects.all()
  ctx = {
    "categories": categories,
    "items": items,
  }
  return render(request, 'index.html', ctx)
 
def signup(request):
  form = SignupForm()
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("/login/")
    
  ctx = { "form": form }
  return render(request, 'signup.html', ctx)

def login(request):
  return render(request, 'login.html', {})

def contact(request):
  return render(request, 'contact.html', {})

def about(request):
  return render(request, 'about.html', {})