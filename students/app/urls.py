from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.list_student, name='home'),
    path('add_student/',views.add_student, name='add_student'),
    path('edit_student/<int:id>/',views.edit_student,name='edit_student'),
    path('delete_student/<int:id>/',views.delete_student,name='delete_student'),
    path('search_student/',views.search_student,name='search'),

    path('register/', views.dangky, name= 'register'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
