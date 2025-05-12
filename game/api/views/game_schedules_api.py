from .base_viewset import BaseViewSet
from game.models import GameSchedule
from game.api.serializers import BaseGameScheduleSerializer
from django.http import JsonResponse
from django.db import transaction
from rest_framework.decorators import action
from rest_framework import status

class GameScheduleViewset(BaseViewSet):
    queryset = GameSchedule.objects.all()
    serializer_class = BaseGameScheduleSerializer

    @action(detail=False, methods=['get'], url_path='daily')
    def get_game_schedule_daily(self, request):
        current_active = self.queryset.filter(status=1, is_deleted=False).order_by("-id").first()
        draws_of_the_day = self.queryset.filter(date=current_active.date, is_deleted=False)
        serializer = self.serializer_class(draws_of_the_day, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        
        
    @action(detail=False, methods=['post'], url_path='daily')
    def upsert_game_schedules(self, request):
        data = request.data.get('data', [])
        if not isinstance(data, list):
            return JsonResponse({'detail': 'Expected a list of objects.'}, status=400)
        
        isUpdate = request.data.get('isUpdate', False)
        results = []

        with transaction.atomic():
            if isUpdate:
                # UPDATE
                ids = [item['id'] for item in data]
                existing_objs = {obj.id: obj for obj in GameSchedule.objects.filter(id__in=ids)}

                for item in data:
                    obj = existing_objs.get(item['id'])
                    if not obj:
                        continue
                    serializer = self.serializer_class(obj, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    results.append(serializer.save())

            else:
                # CREATE
                serializers = [self.serializer_class(data=item) for item in data]
                for s in serializers:
                    s.is_valid(raise_exception=True)
                    results.append(s.save())

        serialized = self.serializer_class(results, many=True)
        return JsonResponse(serialized.data, safe=False, status=status.HTTP_200_OK)


        
