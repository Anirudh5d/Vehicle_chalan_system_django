from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_chalan/<int:vehicle_id>/', views.add_chalan, name='add_chalan'),
    path('register_vehicle/', views.register_vehicle, name='register_vehicle'), 
    path('vehicle_list/', views.vehicle_list, name='vehicle_list'),
    path('delete_vehicle/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
    path('vehicle/<int:vehicle_id>/chalans/', views.chalan_list, name='chalan_list'),
]
