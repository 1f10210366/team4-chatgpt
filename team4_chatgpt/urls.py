from django.urls import path
from . import views

app_name = "team4_chatgpt"
urlpatterns = [
  path("",views.TopView.as_view(),name="top"),
  path("home/", views.HomeView.as_view(), name="home"),
  path("index/", views.index, name="index"),
  path("login/", views.LoginView.as_view(), name="login"),  # 'login' パターンを追加
  path("signup/", views.SignUpView.as_view(), name="signup"),  # 例：'signup' パターンも追加
]