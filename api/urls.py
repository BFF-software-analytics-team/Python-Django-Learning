from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_func),
    path('post', views.post_func),
    path('put/<id>', views.put_func)
]