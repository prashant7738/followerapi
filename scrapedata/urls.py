from django.urls import path
from .views import FacebookFollowerListCreateView
from .models import FacebookFollower
from . import views

urlpatterns = [
    path('fb-followers/', FacebookFollowerListCreateView.as_view(), name='fb-followers'),
    path('fb-followers/<str:page>',views.get_latest_follower_count),
]
