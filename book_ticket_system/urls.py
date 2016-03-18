"""book_ticket_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from booking import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^booking/$', views.userList.as_view()),
    url(r'^booking/(?P<pk>[0-9]+)/$', views.userDetail.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^booking/userRandomFind$', views.userRandomfind.as_view()),
    url(r'^booking/userFind$', views.findUser.as_view()),
    url(r'^booking/ticketFind$', views.findTicket.as_view()),
    url(r'^booking/bookTicket$', views.bookTicket.as_view()),
    url(r'^booking/UpdateTicket/(?P<pk>[0-9]+)/$', views.UpdateTicket.as_view()),
]
