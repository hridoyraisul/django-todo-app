from django.urls import path
from .views import index, about, deleteTodo, tasks, userRegistration, userLogin, userLogout

urlpatterns = [
    path('', index, name="home"),
    path('delete-todo/<int:id>', deleteTodo, name="deleteTodo"),
    path('about-us/', about, name="about"),
    path('user-registration/', userRegistration, name="userRegistration"),
    path('user-login/', userLogin, name="userLogin"),
    path('user-logout/', userLogout, name="userLogout"),
    path('tasks', tasks),
]
