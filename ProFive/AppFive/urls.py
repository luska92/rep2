from django.conf.urls import url
from AppFive import views

app_name = 'AppFive'

urlpatterns=[
url(r'^registration/$', views.register, name = "register"),
url(r'^user_login/$', views.user_login, name='user_login'),
]
