from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Item

def detail(request, pk):
  item = get_object_or_404(Item, pk=pk)
  related_items = Item.objects.filter(category=item.category, status=Item.AVAILABLE).exclude(pk=pk)[0:3]
  ctx = { "item": item, "related_items": related_items }
  
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
  return render(request, "new.html", ctx)

@login_required
def edit_item(request, pk):
  user = request.user
  item = get_object_or_404(Item, pk=pk, created_by=user)

  form = EditItemForm(instance=item)
  if request.method == "POST":
    form = EditItemForm(request.POST, request.FILES, instance=item)
    if form.is_valid:
      form.save()

      return redirect('item:detail', pk=item.id)
  
  ctx = { "form": form, "title": "Edit item" }
  return render(request, "new.html", ctx)

@login_required
def delete_item(request, pk):
  user = request.user
  item = get_object_or_404(Item, pk=pk, created_by=user)
  item.delete()

  return redirect("core:user_items")