from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    
    # 리뷰 CR (유저기준)
    path('review/create/', views.review),
    path('<int:movie_id>/review/list/',views.review_list),
    path('review/delete/', views.review_delete),
    path('review/update/', views.review_update),

    # 리뷰 UD (유저기준)
    path('<int:user_id>/review/<review_id>/', views.review_detail),
    

    path('cnt/', views.movie_cnt),

    path('manyrate/', views.many_rate),
    path('userreviews/', views.user_reviews),

    path('like/', views.movie_like),
    path('manylike/', views.movie_manylike),

    
    path('<int:user_id>/likes/', views.get_user_likes),
    path('detail/<int:movie_pk>/', views.movie_detail),
    path('genre/<int:movie_genre>/', views.movie_genre),
    path('recommend/', views.movie_reccommendation),
    path('search/<str:movie_title>/', views.search),
    path('movie_list/', views.movie_list),
    
    # path('admin/', views.admin),
    # path('admin/<int:movie_pk>/', views.admin_detail),
]
