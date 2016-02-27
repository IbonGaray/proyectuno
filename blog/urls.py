from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.uno, name='uno'),
    url(r'^dos/$', views.dos, name='dos'),
    url(r'^gijon/gastos/$', views.gijonGastos, name='gijonGastos'),
    url(r'^cuatrocuatro/$', views.cuatrocuatro, name='cuatrocuatro'),
]
