from django.urls import path


from . import views
urlpatterns = [
    path('', views.homepage, name=''),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name='my_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('my_logout', views.my_logout, name='my_logout'),
   
]



















