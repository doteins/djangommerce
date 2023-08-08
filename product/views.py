from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Item, Category

def browser(request):
  query = request.GET.get('query', '')
  items = Item.objects.filter(status=Item.AVAILABLE)
  category_id = request.GET.get('category', 0)
  categories = Category.objects.all()

  if category_id:
    items = Item.objects.filter(category_id=category_id)
  if query:
    items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

  ctx = {
    "title": "Items",
    'query':query,
    "items": items,
    "categories": categories,
    "category_id": int(category_id),
  }
  return render(request, 'items.html', ctx)

def detail(request, pk):
  item = get_object_or_404(Item, pk=pk)
  related_items = Item.objects.filter(category=item.category, status=Item.AVAILABLE).exclude(pk=pk)[0:3]
  user_items = None
  if request.user.is_authenticated:
    user_items = Item.objects.filter(created_by=request.user)
  
  form = EditItemForm(instance=item)
  if request.method == "POST":
    form = EditItemForm(request.POST, request.FILES, instance=item)
    if form.is_valid:
      # No need to clean data as form uses a ModelForm
      form.save()

      return redirect('item:detail', pk=item.id)
  
  ctx = { 
    "item": item, 
    "related_items": related_items,
    "form": form, 
    "title": "Edit item",
    "user_items": user_items,
  }
  
  return render(request, "detail.html", ctx)

@login_required
def new_item(request):
  form = NewItemForm()
  if request.method == "POST":
    form = NewItemForm(request.POST, request.FILES)
    if form.is_valid:
      item = form.save(commit=False)
      item.created_by = request.user
      item.save()

      return redirect('item:detail', pk=item.id)
  
  ctx = { "form": form, "title": "New item" }
  return render(request, "generic_form.html", ctx)

@login_required
def delete_item(request, pk):
  user = request.user
  item = get_object_or_404(Item, pk=pk, created_by=user)
  item.delete()

  return redirect("core:user_items")