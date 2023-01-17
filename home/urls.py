from django.urls import path
from .views import download_pdf, home, my_view, hello_world

urlpatterns = [
    path('download_pdf/', download_pdf, name='download_pdf'),
    path('home/', home, name='home'),
    path('my_view/', my_view, name='my_view'),
    path('hello_world/', hello_world, name='hello_world'),
]