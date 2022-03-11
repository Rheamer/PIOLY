from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
# Create your views here.
import promo.views
from .models import *
from .serializers import *


class PromoListApiView(generics.ListCreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer

class ObjectMixin():
    object_model = None

    def get_object(self):
        return self.object_model


class ObjectAddMixin():
    def post(self, request, promo_id):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        object = serializer.create()
        object.active_promo = promo_id
        object.save()
        return Response(data = object.id(), status=status.HTTP_201_CREATED)


class ObjectDeleteMixin(ObjectMixin):
    def delete(self, request, promo_id, object_id):
        object = self.get_object().object.filter(id = object_id)
        delid = object.id
        object.delete()
        return Response(data=delid, status=status.HTTP_200_OK)


class ParticipantDeleteApiView(generics.GenericAPIView, ObjectDeleteMixin):
    serializer_class = ParticipantSerializer
    object_model = Participant


class ParticipantAddApiView(generics.GenericAPIView, ObjectAddMixin):
    serializer_class = ParticipantSerializer
    object_model = Participant


class PrizeDeleteApiView(generics.GenericAPIView, ObjectDeleteMixin):
    serializer_class = PrizeSerializer
    object_model = Prize


class PrizeAddApiView(generics.GenericAPIView, ObjectAddMixin):
    serializer_class = PrizeSerializer
    object_model = Prize


class PromoApiView(generics.GenericAPIView, ObjectAddMixin, ObjectDeleteMixin):
    serializer_class = PromoSerializer
    object_model = Promo

    def get(self, request):
        pass

class PlayPromoApiView(generics.GenericAPIView):
    serializer_class = PromoResultSerializer
    def post(self, request, promo_id):
        partc = Promo.object.all().select_related('participant')
        prizes = Promo.object.all().select_related('prize')
        if partc.count != prizes.count:
            return Response(status.HTTP_409_CONFLICT)
        reses = []
        for i in range(partc.count):
            res = PromoResult()
            res.winner = partc[i].id
            res.prize = prizes[i].id
            reses.append(res)
            res.save()
        serializer = PromoSerializer(data=reses, many=True)
        return Response(serializer.data, status.HTTP_201_CREATED)