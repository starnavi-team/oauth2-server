from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('user-update/', views.UserUpdate.as_view(), name='user-update'),
]
