from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>/', views.display_menu_item, name='menu_item'),
]
