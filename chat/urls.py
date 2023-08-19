from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
  path('', views.inbox, name='inbox'),
  path('<int:pk>/', views.chat, name='chat'),
  path('new/<int:item_pk>/', views.new_conversation, name='new'),
]