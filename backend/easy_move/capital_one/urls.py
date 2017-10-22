from django.conf.urls import url, include
from capital_one import views
urlpatterns = [
    url(r'capital_one/$', views.CapitalOneLogin.as_view(), name='capital_one_login'),
    url(r'send_email/$', views.SendEmail.as_view(), name='send_email'),
]