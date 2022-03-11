from rest_framework import serializers
from .models import *


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class PromoResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoResult
        fields = '__all__'