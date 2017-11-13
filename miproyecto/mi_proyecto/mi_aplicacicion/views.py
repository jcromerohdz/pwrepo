# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
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
    template_name = "tweets/create_view.html"
    success_url = "/tweet/list"
    login_url = "/admin"

class TweetUpdateView(UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    success_url = "/tweet/list"

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("TweetList")


class TweetDetailView(DetailView):
    template_name = "tweets/tweet_detail.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Tweet.objects.get(id=id)


class TweetListView(ListView):
    template_name = "tweets/tweets_list.html"
    # queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(content__icontains=query) |
                            Q(user__username__icontains=query)
                          )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        print context
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("TweetCreate")
        return context
