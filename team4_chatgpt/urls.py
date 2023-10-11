from django.urls import path
from . import views

app_name = "team4_chatgpt"
urlpatterns = [
  path("",views.index,name="index")
]