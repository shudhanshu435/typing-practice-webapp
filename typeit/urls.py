from django.urls import path
from .views import *

urlpatterns = [
    path('test/', typing_test, name='typing_test'),
    path('save-result/', save_result, name='save_result'),
    path('history/', typing_history, name='typing_history'),

    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('generate-passage/', generate_passage, name="generate_passage"),
]