from .base_viewset import BaseViewSet
from game.models import Result
from game.api.serializers import BaseResultSerializer, SimpleCreateResultSerializer
from drf_spectacular.utils import extend_schema
from django.http import JsonResponse
from rest_framework import status

class ResultViewset(BaseViewSet):
    queryset = Result.objects.all()
    serializer_class = BaseResultSerializer


    @extend_schema(request=SimpleCreateResultSerializer, responses=BaseResultSerializer)
    def create(self, request):
        serializer = SimpleCreateResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = BaseResultSerializer(Result.objects.last())

        return JsonResponse(data=response.data, status=status.HTTP_201_CREATED, safe=False)
