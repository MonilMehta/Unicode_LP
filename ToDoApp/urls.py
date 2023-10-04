from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('<str:pk>/',views.todo,name='todopage'),
    path('update_todo/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete_todo/<str:pk>/', views.delete_todo, name='delete_todo'),
    path('logout/<str:pk>', views.logout_view, name='logout'),

]