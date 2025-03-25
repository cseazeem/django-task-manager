from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer


# API to create a task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # API to assign a task to users
    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        task = self.get_object()
        user_ids = request.data.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)

        if users.exists():
            task.assigned_users.set(users)
            return Response({'message': 'Task assigned successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid user IDs'}, status=status.HTTP_400_BAD_REQUEST)

# API to get tasks assigned to a specific user
class UserTaskViewSet(viewsets.ViewSet):
    def list(self, request, user_id=None):
        tasks = Task.objects.filter(assigned_users__id=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
