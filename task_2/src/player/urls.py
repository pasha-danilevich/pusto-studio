from django.urls import path
from .views import export_to_csv, assign_prize

urlpatterns = [
    path('export/player-levels/', export_to_csv, 
        name='export_player_levels'),
    path('assign-prize/<int:player_id>/<int:level_id>/', assign_prize, name='assign_prize'),
]
