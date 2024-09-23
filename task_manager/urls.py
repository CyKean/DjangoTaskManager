from django.contrib import admin    
from django.urls import path, include
from tasks import views  # Siguruhing tumpak ang path depende sa iyong project structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.logout, name='logout'), 
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('past-due/', views.past_due, name='past_due'),
    path('completed/', views.completed, name='completed'),
]
