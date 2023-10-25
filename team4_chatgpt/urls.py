from django.urls import path
from . import views

app_name = "team4_chatgpt"
urlpatterns = [
  path("",views.TopView.as_view(),name="top"),
  path("index/", views.index, name="index"),
]