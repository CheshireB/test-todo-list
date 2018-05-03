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


from tasks.models import Task
from .serializers import TaskSerializer


class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



@method_decorator(csrf_exempt, name='dispatch')
class TaskAPIView(RetrieveAPIView, UpdateModelMixin, CreateModelMixin, DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
         return self.update(request, *args, **kwargs)