from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import (
    DestroyModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response

from tasks.models import Task
from .serializers import TaskSerializer

# @method_decorator(csrf_exempt, name='dispatch')
class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# @method_decorator(csrf_exempt, name='dispatch')
class TaskAPIView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
         return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        object = self.get_object()
        object.is_complete = not object.is_complete
        object.save()

        return Response()


# @method_decorator(csrf_exempt, name='dispatch')
class TaskCreateAPIView(RetrieveAPIView, CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

