from django.urls import path

from . import views

app_name = "email"
urlpatterns = [
    path('',views.home,name="home"),
    path('detail/<slug>/',views.post_detail,name="detail"),
    ]
