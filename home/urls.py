from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('post/create-update/', views.post_create_update, name='post_create_update'),
    path('email', views.email, name='email'),
    path('email_validation', views.email_validation, name='email_validation')
]