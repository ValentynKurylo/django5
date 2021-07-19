from django.urls import path

from user.views import m

urlpatterns = [
    path('', m)
]