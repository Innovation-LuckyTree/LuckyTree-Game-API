from .base_viewset import BaseViewSet
from game.models import CompanyGame
from game.api.serializers import BaseCompanyGameSerializer, CompanyGameListSerializer, UpdateRequestSerializer,GameDetailsUpdateRequest,SimpleCompanyGameSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter
import uuid

class CompanyGameViewset(BaseViewSet):
    queryset = CompanyGame.objects.all()
    serializer_class = BaseCompanyGameSerializer


    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='companyId', 
                description='companyId filter', 
                type=str
            )
        ],
        responses=CompanyGameListSerializer)
    @action(detail=False, methods=["get"], url_path="company")
    def get_companygames_by_company_id(self, request):
        queryset = self.queryset.filter(is_deleted=False)
        company_id = self.request.query_params.get('companyId', None)

        if company_id:
            try:
                company_id = uuid.UUID(company_id)
                queryset = queryset.filter(company_id__exact=company_id)
            except ValueError:
                return JsonResponse({"error": "Invalid UUID format for companyId"}, status=status.HTTP_400_BAD_REQUEST)


        serializer = CompanyGameListSerializer(queryset, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    

    @extend_schema(
        request=UpdateRequestSerializer,
        responses=CompanyGameListSerializer)
    @action(detail=True, methods=["patch"], url_path="mechanics")
    def update_mechanics(self, request,pk=None):
        updates = []
        instance = get_object_or_404(self.queryset, pk=pk)
        mechanics = instance.mechanics

        #Check changed fields
        if mechanics.get('winAmount') != request.data.get('winAmount'):
            updates.append('winAmount')
        if mechanics.get('straightLimit') != request.data.get('straightLimit'):
            updates.append('straightLimit')
        if mechanics.get('rumbleLimit') != request.data.get('rumbleLimit'):
            updates.append('rumbleLimit')
        
        updatedFields = ', '.join(updates)

        serializer = CompanyGameListSerializer(instance, data={
            "mechanics":request.data, 
            "updated_property": updatedFields, 
            "updated_by": request.data.get('updated_by')
            }, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    
    @extend_schema(
        request=GameDetailsUpdateRequest,
        responses=CompanyGameListSerializer
    )
    @action(detail=True, methods=["patch"], url_path="details")
    def update_game_details(self, request, pk=None):
        updates = []
        instance = get_object_or_404(self.queryset, pk=pk)
        print(instance, request.data)

        #Check changed fields
        if instance.title != request.data.get('title'):
            updates.append('title')
        if instance.description != request.data.get('description'):
            updates.append('description')
        if instance.is_playable != request.data.get('is_playable'):
            updates.append('is_playable')
        
        updatedFields = ', '.join(updates)

        serializer = SimpleCompanyGameSerializer(instance, data={
            **request.data, 
            "updated_property": updatedFields, 
            "updated_by": request.data.get('updated_by')
            }, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    
