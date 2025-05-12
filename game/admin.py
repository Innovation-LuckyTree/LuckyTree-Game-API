from django.contrib import admin
from game.models import *

# Register your models here.
admin.site.register(BetItem)
admin.site.register(BetTransaction)
admin.site.register(Combination)
admin.site.register(CombinationLimit)
admin.site.register(DrawSchedule)
admin.site.register(GameSchedule)
admin.site.register(Game)
admin.site.register(Result)
admin.site.register(Winner)