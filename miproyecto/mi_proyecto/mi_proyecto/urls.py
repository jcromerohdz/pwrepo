"""mi_proyecto URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from mi_aplicacicion.views import home, TweetCreateView
from mi_aplicacicion.views import TweetDetailView, TweetListView, TweetUpdateView, TweetDeleteView
# from mi_aplicacicion.views import TweetDetailView, TweetListView, TweetUpdateView
# from mi_aplicacicion.views import TweetDetailView

urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^tweet/create$', TweetCreateView.as_view(), name='TweetCreate'),
    url(r'^tweet/detail/(?P<pk>\d)/edit/$', TweetUpdateView.as_view(), name='TweetUpdate'),
    url(r'^tweet/detail/(?P<pk>\d)/delete/$', TweetDeleteView.as_view(), name='TweetDelete'),
    url(r'^tweet/detail/(?P<id>\d)/$', TweetDetailView.as_view(), name='TweetDetail'),
    url(r'^tweet/list$', TweetListView.as_view(), name='TweetList'),

    # url(r'^tweet/(?P<pk>\d+)/$', TweetDetailView.as_view(), name='TweetDetail'),

    url(r'^admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
