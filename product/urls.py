from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.browser, name='items'),
    path('new/', views.new_item, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete_item, name='delete'),
]