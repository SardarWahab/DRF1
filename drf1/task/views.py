from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TasksSerializers
# Create your views here.

@api_view(['GET'])
def get_notes(request):
    tasks = Task.objects.all()
    serializer = TasksSerializers(tasks, many=True)
    return Response(serializer.data)
