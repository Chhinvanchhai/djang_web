from django.urls import path

from . import views

app_name = 'user' 
urlpatterns = [
    # path("", views.index, name="index"),\
        path('', views.user_list, name='user_list'),
    path('<int:pk>/', views.user_detail, name='user_detail'),
    path('create/', views.user_create, name='user_create'),
    path('<int:pk>/edit/', views.user_update, name='user_update'),
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),
]