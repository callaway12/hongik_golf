from django.conf.urls import url
from django.urls import include, path
import blog.views

urlpatterns =[
    path('', blog.views.home, name='home'),
]