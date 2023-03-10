
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("track/",views.track,name="track"),
    path("search/",views.search,name="search"),
    path("productview/",views.product,name="product"),
    path("checkout/",views.checkout,name="Check"),
]
