from .base_viewset import BaseViewSet
from game.models import DrawSchedule
from game.api.serializers import BaseDrawScheduleSerializer
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.http import JsonResponse
from rest_framework import status

class DrawScheduleViewset(BaseViewSet):
    queryset = DrawSchedule.objects.all()
    serializer_class = BaseDrawScheduleSerializer
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='company_game', 
                description='companyGameId filter', 
                type=int
            )
        ],
        responses=BaseDrawScheduleSerializer)
    @action(detail=False, methods=["get"], url_path="company-game")
    def get_companygames_by_company_game(self, request):
        queryset = self.queryset.filter(is_deleted=False)
        company_game = self.request.query_params.get('company_game', None)

        if company_game:
            try:
                queryset = queryset.filter(company_game__exact=company_game)
            except ValueError:
                return JsonResponse({"error": "Invalid Company Game"}, status=status.HTTP_400_BAD_REQUEST)


        serializer = BaseDrawScheduleSerializer(queryset, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    