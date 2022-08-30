from django.urls import path
from django.urls.resolvers import URLPattern
from . import views



urlpatterns = [
    path ('', views.index, name = 'index'),
    path('delete/<int:post_id>/', views.delete, name ='delete'),
    path('editpost/<int:post_id>/', views.editpost, name='edit'),
    path('like/<int:post_id>/',views.like,name='like'),
]

