from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('toggle/<int:user_id>/', views.toggle_status, name='toggle_status'),
]
