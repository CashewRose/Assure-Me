from django.conf.urls import url
from django.urls import path
from . import views

app_name = "Assure_Me"
urlpatterns = [
    url(r'^$', views.initial, name='initial'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^home$', views.home_view, name='home'),
    url(r'^account$', views.account_view, name='account'),
    url(r'^account_edit$', views.account_edit_view, name='account_edit'),
]
