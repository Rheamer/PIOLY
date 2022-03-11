from django.urls import path, include
from .views import *
urlpatterns = [
    path('promo', PromoListApiView.as_view()),
    path('promo/<int:promo_id>', PromoApiView.as_view()),
    path('promo/<int:promo_id>/participant', ParticipantAddApiView.as_view()),
    path('promo/<int:promo_id>/participant/<int:participant_id>', ParticipantDeleteApiView.as_view()),
    path('promo/<int:promo_id>/prize', PrizeAddApiView.as_view()),
    path('promo/<int:promo_id>/participant/<int:prize_id>', PrizeDeleteApiView.as_view()),
    path('promo/<int:promo_id>/raffle', PlayPromoApiView.as_view()),
]