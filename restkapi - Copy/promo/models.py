from django.db import models

# Create your models here.


class Promo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Prize(models.Model):
    description = models.CharField(max_length=100)
    active_promo = models.ForeignKey(
        Promo,
        related_name='prize',
        on_delete=models.PROTECT,
        blank=True,
        null=True)


class Participant(models.Model):
    name = models.CharField(max_length=100)
    active_promo = models.ForeignKey(
        Promo,
        related_name='participant',
        on_delete=models.CASCADE,
        blank=True,
        null=True)


class PromoResult(models.Model):
    winner = models.ForeignKey(
        Participant,
        related_name='promores',
        on_delete=models.CASCADE,
        )
    prize = models.ForeignKey(
        Prize,
        related_name='promores',
        on_delete=models.CASCADE,
        )
