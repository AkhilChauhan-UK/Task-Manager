from django.urls import path
from .views import CreateTaskView, AssignTaskView, UserTasksView, home_view

urlpatterns = [
    path('', home_view, name='home'), 
    path('tasks/create/', CreateTaskView.as_view(), name='create-task'),
    path('tasks/<int:pk>/assign/', AssignTaskView.as_view(), name='assign-task'),
    path('tasks/user/<int:user_id>/', UserTasksView.as_view(), name='user-tasks'),
]
