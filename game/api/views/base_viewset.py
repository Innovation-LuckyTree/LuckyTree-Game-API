from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

class BaseViewSet(viewsets.ViewSet):
    """Allows basic operations like list, retrieve, delete, """
    """ when using this provide:        """
    """ - queryset                      """
    """ - serializer_class              """
    queryset = ()
    serializer_class = ()
    
    permission_classes = [IsAuthenticated]


    @action(detail=False, methods=['get'], url_path='list-all')
    def list_all(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    

    def list(self, request):
        queryset = self.queryset.filter(is_deleted=False)

        serializer = self.serializer_class(queryset, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    
    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(instance)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        instance.is_deleted = True
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)
