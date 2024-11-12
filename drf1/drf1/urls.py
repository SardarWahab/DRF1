
from django.contrib import admin
from django.urls import path
from task.views import get_notes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', get_notes, name='notes')
]
