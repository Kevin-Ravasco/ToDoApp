from . import views
from django.urls import path


urlpatterns = [
    path( '', views.tasks, name='home'),
    path('todo/', views.todo),
    path('delete_todo/<int:todo_id>', views.delete_todo),
]