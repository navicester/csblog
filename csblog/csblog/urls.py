"""csblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib.auth.views import login as auth_login

from bookmarks.views import main_page, user_page, logout_page, register_page
from django.views.static import serve
# from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView

import os
site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page),
    url(r'^user/(\w+)/$', user_page),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^login/$', auth_login),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register_page),
    # url(r'^register/success/$', direct_to_template, {'template': 'registration/register_success.html'}), 
    url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")), 
    # url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),
    url(r'^site_media/(?P<path>.*)$', serve, {'document_root': site_media}),
]

