from django.conf.urls import url
from django.urls import path
from . import views

app_name = "Assure_Me"
urlpatterns = [
    url(r'^$', views.Product_Home_List_View, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
]
