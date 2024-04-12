from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index-page"),
    path('aboutme/',about,name="about-page"),
    path('contact/',contact,name="contact-page"),
    path('login/',login,name="login-page"),
    path('projects/',Projects,name="Projects-page"),
    path('CV_Download/',download_cv,name="cv-page")
]


