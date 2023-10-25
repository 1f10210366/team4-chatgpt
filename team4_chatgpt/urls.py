from django.urls import path
from . import views

app_name = "team4_chatgpt"
urlpatterns = [
  path("",views.TopView.as_view(),name="top"),
  path("index/", views.index, name="index"),
  path("login/", views.login, name="login"),  # 'login' パターンを追加
  path("signup/", views.signup, name="signup"),  # 例：'signup' パターンも追加
]