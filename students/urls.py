from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('index/', views.index, name='index'),
    path('<int:id>/', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
