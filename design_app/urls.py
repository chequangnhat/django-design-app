from django.urls import path
from .views import login_view
from .views import register_view


urlpatterns = [
    path('api/login/', login_view, name='login'),
    path('api/register/', register_view, name='register'),
]