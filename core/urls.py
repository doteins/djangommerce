from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('contact/', views.contact, name="contact"),
  path('about/', views.about, name="about"),
]

# Do NOT use this settings in production environment!
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)