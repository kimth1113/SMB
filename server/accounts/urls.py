from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('delete/', views.delete),
    path('password/', views.change_password),

    path('<int:person_id>/following/', views.following),
    path('<int:user_id>/mypage/', views.mypage),
]