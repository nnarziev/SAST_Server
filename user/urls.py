from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^register/?', views.register_api),
    url(r'^login/?', views.login_api)
]

