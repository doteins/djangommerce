from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
  path('', views.index, name="index"),
  path('user/<str:username/items', views.user_items, name="dashboard"),
  path('contact/', views.contact, name="contact"),
  path('about/', views.about, name="about"),
  path('signup/', views.signup, name="signup"),
  path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name="login")
]

# Do NOT use this settings in production environment!
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)