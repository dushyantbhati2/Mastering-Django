from django.urls import path
from . import views

urlpatterns = [
    path('',views.market),
    path('test/',views.test),
]
