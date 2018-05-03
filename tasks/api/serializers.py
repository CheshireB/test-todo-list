
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'