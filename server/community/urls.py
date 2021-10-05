from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('article/create/', views.article_create),
    path('<int:article_id>/article_detail/', views.article_detail),
    path('<int:article_id>/article_update/', views.article_update),
    path('<int:article_id>/article_delete/', views.article_delete),
    path('<int:article_id>/comment/', views.comment),
    path('<int:article_id>/comment/<int:comment_id>/', views.comment_delete),
    path('<int:comment_id>/comment_detail/', views.comment_detail),
    
]
