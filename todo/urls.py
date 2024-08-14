# from django.contrib import admin // disabled administrators
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),  // disabled administrators
    path('todo/', include('todoapp.urls')),
]
