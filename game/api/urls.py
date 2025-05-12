from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'game', GameViewset, basename='game')
router.register(r'company_game', CompanyGameViewset, basename='company_game')
router.register(r'soldout', SoldoutCombinationViewset, basename='soldout')
router.register(r'combination_limit', CombinationLimitViewset, basename='combination_limit')
router.register(r'draw_schedules', DrawScheduleViewset, basename='draw_schedules')
router.register(r'game_schedule', GameScheduleViewset, basename='game_schedule')
router.register(r'combination', CombinationViewset, basename='combination')
router.register(r'bet_transaction', BetTransactionViewset, basename='bet_transaction')
router.register(r'bet_item', BetItemViewset, basename='bet_item')
router.register(r'result', ResultViewset, basename='result')
router.register(r'winner', WinnerViewset, basename='winner')