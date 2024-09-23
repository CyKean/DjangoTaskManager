from django.urls import path, include
from tasks import views  # Siguruhing tumpak ang path depende sa iyong project structure

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.logout, name='logout'), 
    path('home/', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('past-due/', views.past_due, name='past_due'),
    path('completed/', views.completed, name='completed'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),

]