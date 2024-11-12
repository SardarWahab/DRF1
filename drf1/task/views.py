from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
# Create your views here.

@api_view(['GET'])
def get_notes(request):
#     notes = Task.objects.all()
#     serializer = NoteSerializer(notes, many=True)
    return Response("Hallo World")
