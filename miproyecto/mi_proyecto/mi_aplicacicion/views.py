# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView
from django.shortcuts import render

from .forms import TweetModelForm
from .models import Tweet
from .mixin import FormUserNeededMixin


# Create your views here.





def home(request):
    tweets = Tweet.objects.all()

    return render(request, "home.html", context={"msg":"hola django", "tweets":tweets})


# Need to start crud

# Create form
class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/form.html"
    success_url = "admin/"


class TweetDetailView(DetailView):
    template_name = "tweets/tweet_detail.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Tweet.objects.get(id=id)


class TweetListView(ListView):
    template_name = "tweets/tweets_list.html"
    queryset = Tweet.objects.all()
