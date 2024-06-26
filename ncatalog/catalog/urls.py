from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('like/<int:clothing_id>/', like_clothing, name='like_clothing'),
    path('comment/<int:clothing_id>/', comment_clothing, name='comment_clothing'),
    path('add/', add_clothing, name='add_clothing'),
    path('edit/<int:clothing_id>/', edit_clothing, name='edit_clothing'),
    path('delete/<int:clothing_id>/', delete_clothing, name='delete_clothing'),
    path('detail/<int:clothing_id>/', detail_clothing, name='detail_clothing'),
    path('spa', spa, name='spa'),
    path('spa_detail/<int:clothing_id>/', spa_detail, name='spa_detail'),
    path('spa_like/<int:clothing_id>/', spa_like, name='spa_like'),
    path('spa_comment/<int:clothing_id>/', spa_comment, name='spa_comment'),
]