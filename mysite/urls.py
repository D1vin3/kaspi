"""mysite URL Configuration

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
from mysite import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^greeting/$', views.GreetingView.as_view(), name='greeting'),
    url(r'^detail/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^drf/$', views.DRFView.as_view(), name='drf'),


]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['html', 'json'])
