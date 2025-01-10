from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.user_login, name='root'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('add/', views.add_marks, name='add'),
    path('view/', views.view_marks, name='view'),
    path('update/<int:student_id>/', views.update_marks, name='update_marks'),
    path('delete/<int:student_id>/', views.delete_marks, name='delete'),
    path('export/', views.export_csv, name='export'),  # Add this line
    path('export_csv/', views.export_csv, name='export_csv')
]

