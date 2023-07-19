from django.urls import path
from .views import login_view
from .views import register_view
from .views import logout_view
from .views import check_login_view
from .views import get_data_test_view


urlpatterns = [
    path('api/login/', login_view, name='login'),
    path('api/register/', register_view, name='register'),
    path('api/logout/', logout_view, name='logout'),
    path('api/check_login/', check_login_view, name='check_login'),
    path('api/get_data/', get_data_test_view, name='get_data'),
]