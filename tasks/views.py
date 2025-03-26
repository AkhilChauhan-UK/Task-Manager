from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer, TaskAssignSerializer

#  API to create a task
class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#  API to assign a task to users
class AssignTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAssignSerializer

    def update(self, request, *args, **kwargs):
        """Custom logic to handle multiple user assignments"""
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task assigned successfully!", "task": serializer.data})
        return Response(serializer.errors, status=400)

#  API to get tasks assigned to a user
class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """Retrieve tasks assigned to a specific user"""
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)

#  Home API for root URL
@api_view(['GET'])
def home_view(request):
    """Return a simple welcome message or redirect to API documentation"""
    return Response({
        "message": "Welcome to the Task Management API",
        "endpoints": {
            "Create Task": "/tasks/create/",
            "Assign Task": "/tasks/{id}/assign/",
            "User Tasks": "/tasks/user/{user_id}/"
        }
    })
