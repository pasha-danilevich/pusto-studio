import csv
from django.http import HttpResponse
from .models import PlayerLevel, LevelPrize

def export_player_levels_to_csv(request):
    # Создаем HTTP-ответ с заголовками для CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="player_levels.csv"'

    writer = csv.writer(response)
    writer.writerow(['Player ID', 'Level Title', 'Is Completed', 'Received Prize'])

    player_levels = PlayerLevel.objects.select_related('player', 'level').prefetch_related('level__levelprize_set')

    for player_level in player_levels:
        pk = player_level.player.pk
        level_title = player_level.level.title
        is_completed = player_level.is_completed

        prizes = LevelPrize.objects.filter(level=player_level.level)
        received_prizes = [prize.prize.title for prize in prizes if prize.received]

        # Записываем данные в CSV
        writer.writerow([pk, level_title, is_completed, ', '.join(received_prizes)])

    return response
