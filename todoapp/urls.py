from django.urls import path
from .views import index, about, deleteTodo

urlpatterns = [
    path('', index, name="home"),
    path('delete-todo/<int:id>', deleteTodo, name="deleteTodo"),
    path('about-us/', about, name="about"),
]
