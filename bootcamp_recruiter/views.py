import json

from django.shortcuts import render, render_to_response,redirect,get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from social.apps.django_app.default.models import UserSocialAuth

from .models import Company
from rest_framework import viewsets
from bootcamp_recruiter.serializers import CompanySerializer

import twitter
from twitter import TwitterError

# Create your views here.
def home(request):
    names = Company.objects.all()
    return render(request, 'bootcamp_recruiter/home.html', {'names': names})

def company_detail(request,name):
    company_name = get_object_or_404(Company,company_name=name)
    return render(request, 'bootcamp_recruiter/company_detail.html', {'company_name': company_name})

def login(request):
    context = RequestContext(request, {'request': request, 'user': request})
    return render(request, 'bootcamp_recruiter/login.html', {'context': context})

def logout(request):
    auth_logout(request)
    return redirect('/')

def query(request,company_name):
    company = Company.objects.get(company_name=company_name)
    handle = company.twitter_handle
    api = get_twitter(request.user)
    statuses = api.GetUserTimeline(screen_name=handle)
    return render(request, 'bootcamp_recruiter/query.html', {'statuses': statuses})

def tweet(request):
    status = request.POST.get("status", None)
    my_status = '#SXSWin3Words' + ' ' + status
    api = get_twitter(request.user)
    response = None

    if status:
        response = api.PostUpdates(my_status)

    return redirect('/query')

def get_twitter(user):
    consumer_key = settings.SOCIAL_AUTH_TWITTER_KEY
    consumer_secret = settings.SOCIAL_AUTH_TWITTER_SECRET
    access_token_key = settings.TWITTER_ACCESS_TOKEN
    access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET

    usa = UserSocialAuth.objects.get(user=user, provider='twitter')
    if usa:
        access_token = usa.extra_data['access_token']
        if access_token:
            access_token_key = access_token['oauth_token']
            access_token_secret = access_token['oauth_token_secret']

    if not access_token_key or not access_token_secret:
        raise Exception('No user for twitter API call')

    api = twitter.Api(
        base_url='https://api.twitter.com/1.1',
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret)

    return api

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
