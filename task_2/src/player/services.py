from django.utils import timezone
from .models import Player, Level, PlayerLevel, LevelPrize


def assign_prize_to_player(player_id: int, level_id: int) -> bool:
    try:
        player = Player.objects.get(id=player_id)
        level = Level.objects.get(id=level_id)
        player_level = PlayerLevel.objects.get(player=player, level=level)
        
    except (Player.DoesNotExist, Level.DoesNotExist, PlayerLevel.DoesNotExist):
        return False  # Игрок или уровень не найдены
    
    is_successful_assignment = _assign_prizes_to_player(
        player_level=player_level, 
        level=level
        )
    
    return is_successful_assignment
    
    


def _assign_prizes_to_player(player_level:PlayerLevel, level:Level) -> bool:
    if player_level.is_completed:
        # Получаем призы для уровня
        level_prizes = LevelPrize.objects.filter(level=level)

        # Присваиваем призы игроку
        for level_prize in level_prizes:
            level_prize.received = timezone.now() 
            level_prize.save() 
        return True  
    else:
        return False  # Уровень не завершен