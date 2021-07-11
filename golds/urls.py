from django.urls import path
from . import views
urlpatterns[
    path("",views.gold_list,name="post_list")
]