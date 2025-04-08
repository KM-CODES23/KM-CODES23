from django.urls import path
from . import views

urlpatterns = [
    path('', views.loading_view, name='loading'),
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('tracker/', views.tracker_view, name='tracker'),
     path('logger/', views.logger_view, name='logger'),
]