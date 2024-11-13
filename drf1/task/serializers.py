from rest_framework import serializers
from .models import Task

class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title','description']

