from django.conf.urls import url
from django.urls import include, path
import accounts.views

urlpatterns =[
    path('login', accounts.views.login, name='login'),
    path('signup', accounts.views.signup, name='signup'),
    path('logou', accounts.views.logout, name='logout'),
]