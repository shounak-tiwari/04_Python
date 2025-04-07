from django.urls import path
from .views import HomePage,login,signup,stafflogin

urlpatterns = [
    path('',HomePage,name="HomePage"),
    path('log-in/',login,name="log-in"),
    path('sign-up/',signup,name='sign-up'),
    path('stafflogin/',stafflogin,name="stafflogin")
]
