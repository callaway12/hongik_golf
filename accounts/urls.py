from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views
import accounts.views

urlpatterns = [
    path('login/', accounts.views.login, name='login'),
    path('signup', accounts.views.signup, name='signup'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('main', accounts.views.main, name='main'),
]