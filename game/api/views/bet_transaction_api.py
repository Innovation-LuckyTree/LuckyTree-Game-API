from .base_viewset import BaseViewSet
from game.models import BetTransaction
from game.api.serializers import BaseBetTransactionSerializer, BetTransactionCreateSerializer
from drf_spectacular.utils import extend_schema
from django.http import JsonResponse
from rest_framework import status
from django.db.models import Max

class BetTransactionViewset(BaseViewSet):
    queryset = BetTransaction.objects.all()
    serializer_class = BaseBetTransactionSerializer
    
    @extend_schema(request=BetTransactionCreateSerializer, responses=BetTransactionCreateSerializer)
    def create(self, request):
        max_id = BetTransaction.objects.aggregate(Max('id'))['id__max'] # get the maximum existing id in the table
        next_id = max_id + 1 if max_id is not None else 1
        serializer = BetTransactionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = BaseBetTransactionSerializer(BetTransaction.objects.filter(pk=next_id).prefetch_related('bet_items').first())

        return JsonResponse(data=response.data, status=status.HTTP_201_CREATED, safe=False)
