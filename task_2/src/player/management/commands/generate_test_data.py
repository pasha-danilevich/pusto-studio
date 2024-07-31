from django.core.management.base import BaseCommand
from player.models import Player, Level, Prize, PlayerLevel, LevelPrize
import random
from datetime import datetime, timedelta
from faker import Faker

class Command(BaseCommand):
    help = 'Генерация тестовых данных для моделей Player, Level, Prize, PlayerLevel и LevelPrize'

    def handle(self, *args, **kwargs):
        # Генерация игроков
        players = []
        for i in range(20): 
            name = Faker().name()
            player = Player.objects.create(name=name)
            players.append(player)

        # Генерация уровней
        levels = []
        for i in range(10):  
            level = Level.objects.create(title=f'Level {i}', order=i)
            levels.append(level)

        # Генерация призов
        prizes = []
        for i in range(7): 
            prize = Prize.objects.create(title=f'Prize {i}')
            prizes.append(prize)

        # Генерация PlayerLevel и LevelPrize
        for player in players:
            for level in levels:
                is_completed = random.choice([True, False])
                completed_date = datetime.now() - timedelta(days=random.randint(1, 30))
                
                player_level = PlayerLevel.objects.create(
                    player=player,
                    level=level,
                    completed=completed_date,
                    is_completed=is_completed,
                    score=random.randint(0, 100)
                )

                # Если уровень завершен, присваиваем приз
                if is_completed:
                    for prize in prizes:
                        LevelPrize.objects.create(
                            level=level,
                            prize=prize,
                            received=datetime.now() - timedelta(days=random.randint(0, 10))
                        )

        self.stdout.write(self.style.SUCCESS(
            'Тестовые данные успешно сгенерированы!'))
