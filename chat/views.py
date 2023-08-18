from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from product.models import Item
from .forms import MessageForm
from .models import Conversation

@login_required
def new_conversation(request, item_pk):
  item = get_object_or_404(Item, pk=item_pk)

  if item.created_by == request.user:
    return redirect('core:user_items')
  
  conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

  if conversations:
    return redirect('chat:chat', pk=conversations.first().id)

  if request.method == 'POST':
    form = MessageForm(request.POST)

    if form.is_valid():
      conversation = Conversation.objects.create(item=item)
      conversation.members.add(request.user)
      conversation.members.add(item.created_by)
      conversation.save()

      conversation_message = form.save(commit=False)
      conversation_message.conversation = conversation
      conversation_message.created_by = request.user
      conversation_message.save()

      return redirect('item:detail', pk=item_pk)
  else:
    form = MessageForm()
  
  ctx = { 'form': form }
  return render(request, 'new.html', ctx)

