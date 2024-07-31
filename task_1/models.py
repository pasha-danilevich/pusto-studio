from django.db import models
from django.utils import timezone

class Player(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_login = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True)
    points = models.IntegerField(default=0)
    last_points_entry = models.DateTimeField(null=True, blank=True)
    
    def record_first_login(self):
        """Записывает первый вход пользователя"""
        
        self.first_login = timezone.now()
        self.save()
        # дата первого посещения записывается в бд, так легче вести аналитику
        # еще можно вызывать отдельную функцию, 
        # которая будет записывать дату в отдельный файл, не касаять бд


    def earn_points_for_entry(self):
        """Начисляем баллы за вход только один раз в сутки."""
        now = timezone.now()
        
        # Проверяем, было ли начисление баллов в тот же день
        if self.last_points_entry is None or self.last_points_entry.date() < now.date():
            self.points += 10  
            self.last_points_entry = now 
            self.save()

    def __str__(self):
        return self.username
    
def user_login(username):
    player, created = Player.objects.get_or_create(username=username)
    player.record_first_login()
    player.earn_points_for_entry()  
    

class Boost(models.Model):
    BOOST_TYPES = [
        ('speed', 'Ускорение'),
        ('strength', 'Сила'),
        ('defense', 'Защита'),
    ]

    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='boosts')
    boost_type = models.CharField(max_length=20, choices=BOOST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    

    @classmethod
    def grant_boost(cls, player, boost_type):
        """Начисляет буст игроку."""
        boost = cls(player=player, boost_type=boost_type)
        boost.save()
        
    def __str__(self):
        return f"{self.player.username} - {self.get_boost_type_display()}"



def grant_player_boost(username, boost_type):
    player = Player.objects.get(username=username)
    Boost.grant_boost(player, boost_type)