
from django.urls import path
from django_silly_adminplus import views

from django_silly_adminplus.config import SILLY_ADMINPLUS as conf

urlpatterns = [
    path(conf['DSAP_PREFIX'] + 'adminplus/', views.adminplus, name='adminplus'),
]
