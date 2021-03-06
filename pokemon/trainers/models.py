import logging

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .constants import POKEMON, POKEMON_CHOICES


log = logging.getLogger(__name__)


IV = [(x, str(x)) for x in range(0, 16)]

MYSTIC = 1
VALOR = 2
INSTINCT = 3

TEAMS = (
    (MYSTIC, 'Mystic'),
    (VALOR, 'Valor'),
    (INSTINCT, 'Instinct'),
)


class Badge(models.Model):
    logo = models.ImageField(upload_to='badges')
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class TrainerUpdate(models.Model):
    trainer = models.ForeignKey('Trainer', related_name='updates', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    xp = models.BigIntegerField()
    pokemon_caught = models.IntegerField()
    pokestops_spun = models.IntegerField()
    battles_won = models.IntegerField()
    kilometers_walked = models.FloatField()
    pokedex_number = models.IntegerField()
    hours_defended = models.IntegerField('Hours Defended', default=0)
    berries_fed = models.IntegerField('Berries Fed', default=0)
    eggs_hatched = models.IntegerField('Eggs Hatched', default=0)


class Trainer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='trainer', on_delete=models.CASCADE)
    username = models.CharField('Trainer Name', max_length=64, unique=True)
    team = models.IntegerField(choices=TEAMS)

    updated_at = models.DateTimeField(blank=True, null=True)

    xp = models.BigIntegerField('Total XP')

    pokemon_caught = models.IntegerField('Pokemon Caught')
    pokestops_spun = models.IntegerField('Pokestops Spun')
    battles_won = models.IntegerField('Battles Won')
    kilometers_walked = models.FloatField('Kilometers Walked')
    pokedex_number = models.IntegerField('Pokedex Entries')

    hours_defended = models.IntegerField('Hours Defended', default=0)
    berries_fed = models.IntegerField('Berries Fed', default=0)
    eggs_hatched = models.IntegerField('Eggs Hatched', default=0)

    __original_xp = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_xp = self.xp

    @property
    def url(self):
        return self.get_absolute_url()

    @property
    def level(self):
        if self.xp >= 20000000:
            return 40
        elif self.xp >= 15000000:
            return 39
        elif self.xp >= 12000000:
            return 38
        elif self.xp >= 9500000:
            return 37
        elif self.xp >= 7500000:
            return 36
        elif self.xp >= 6000000:
            return 35
        elif self.xp >= 4750000:
            return 34
        elif self.xp >= 3750000:
            return 33
        elif self.xp >= 3000000:
            return 32
        elif self.xp >= 2500000:
            return 31
        elif self.xp >= 2000000:
            return 30
        elif self.xp >= 1650000:
            return 29
        elif self.xp >= 1350000:
            return 28
        elif self.xp >= 1100000:
            return 27
        elif self.xp >= 900000:
            return 26
        elif self.xp >= 710000:
            return 25
        elif self.xp >= 560000:
            return 24
        elif self.xp >= 435000:
            return 23
        elif self.xp >= 335000:
            return 22
        elif self.xp >= 260000:
            return 21
        elif self.xp >= 210000:
            return 20
        return "<20"

    @property
    def team_name(self):
        return TEAMS[self.team - 1][1]

    @property
    def team_image(self):
        return 'img/{0}.png'.format(self.team_name.lower())

    def get_absolute_url(self):
        return reverse('trainer-detail', kwargs={'username': self.username})

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if self.pk and self.xp != self.__original_xp:
            TrainerUpdate.objects.create(
                trainer=self,
                created_at=timezone.now(),
                xp=self.xp,
                pokemon_caught=self.pokemon_caught,
                pokestops_spun=self.pokestops_spun,
                battles_won=self.battles_won,
                kilometers_walked=self.kilometers_walked,
                pokedex_number=self.pokedex_number,
                berries_fed=self.berries_fed,
                hours_defended=self.hours_defended,
                eggs_hatched=self.eggs_hatched,
            )
        return super().save(*args, **kwargs)


class TrainerBadge(models.Model):
    created_at = models.DateTimeField(editable=True)
    trainer = models.ForeignKey(Trainer, related_name='trainer_badges', on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, related_name='trainer_badges', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Badge'
        verbose_name_plural = 'Badges'


class BadgeApplication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    trainer = models.ForeignKey(Trainer, related_name='badge_applications', on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, related_name='badge_applications', on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='badge_applications')
    screenshot2 = models.ImageField(upload_to='badge_applications', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        TrainerBadge.objects.create(
            trainer=self.trainer,
            badge=self.badge,
            created_at=timezone.now()
        )
        self.approved = True
        self.save()

    class Meta:
        verbose_name = 'Badge Application'
        verbose_name_plural = 'Badge Applications'


class FavoritePokemon(models.Model):
    trainer = models.ForeignKey(Trainer, related_name='favorite_pokemon', on_delete=models.CASCADE)

    number = models.IntegerField(choices=POKEMON_CHOICES)
    cp = models.IntegerField()

    shiny = models.BooleanField(default=False)

    attack = models.IntegerField(choices=IV, blank=True, null=True)
    defense = models.IntegerField(choices=IV, blank=True, null=True)
    hp = models.IntegerField(choices=IV, blank=True, null=True)

    fast_move = models.CharField(max_length=64, blank=True)
    charge_move = models.CharField(max_length=64, blank=True)

    @property
    def image(self):
        number = str(self.number)
        while len(number) < 3:
            number = '0' + number
        url = number + '-00'
        if self.shiny:
            url += '-shiny'
        return 'https://pokemon.gameinfo.io/images/pokemon-go/{0}.png'.format(url)

    @property
    def iv(self):
        if not self.attack or not self.defense or not self.hp:
            return None
        return (self.attack + self.defense + self.hp) / 45 * 100

    @property
    def name(self):
        return POKEMON[self.number]

    def __str__(self):
        return '{0}\'s {1} CP {2}'.format(
            self.trainer.username,
            self.cp,
            self.name,
        )

    class Meta:
        verbose_name = 'Favorite Pokemon'
        verbose_name_plural = 'Favorite Pokemon'
        ordering = ('-cp',)
