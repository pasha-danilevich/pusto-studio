from django.http import JsonResponse
from .csv_log import export_player_levels_to_csv
from .services import assign_prize_to_player


def export_to_csv(request):
    return export_player_levels_to_csv(request)

def assign_prize(request, player_id: int, level_id: int):
    success = assign_prize_to_player(player_id, level_id)
    if success:
        return JsonResponse({'success': True, 'message': 'The prize has been successfully awarded!'})
    else:
        return JsonResponse({'success': False, 'message': 'The prize could not be awarded. Check if the level is completed.'}, status=400)