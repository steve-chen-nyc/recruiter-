import json,time
from django.shortcuts import render, render_to_response,redirect,get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from social.apps.django_app.default.models import UserSocialAuth
from django.core import serializers
from django.utils import timezone
import datetime
from datetime import timedelta

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
    return render(request, 'bootcamp_recruiter/home.html', {'context': context})

def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required
def query(request,company_name):
    company = Company.objects.get(company_name=company_name)
    handle = company.twitter_handle
    api = get_twitter(request.user)
    statuses = api.GetUserTimeline(screen_name=handle)
    return render(request, 'bootcamp_recruiter/query.html', {'statuses': statuses})

@login_required
def tweet(request):
    status = request.POST.get("status", None)
    response = None

    index = status.index(' ')
    twitter_handle = status[1:index].lower()
    company = Company.objects.get(twitter_handle__icontains=twitter_handle)
    company_name = company.company_name

    api = get_twitter(request.user)

    if checker(status) == False:
        return redirect('/fail')

    else:
        response = api.PostUpdates(status)

    return redirect('query', company_name=company_name)


def checker(string):
    slang_list = ['savage', 'fam', 'synergy', 'totes', 'bottomline', 'hardworker',
                  'dynamic','proactively' ,'obvi' ,'fleek', 'yolo', 'cray', 'cra-cra',
                  'bae', 'whateves', 'obvs', 'ridic', 'feels', 'lit', 'sus',
                  'yeet', 'snatched', 'trash']

    catcher = []
    tweet = string.lower().split()

    for t in tweet:
        if t in slang_list:
            catcher.append(t)

    if len(catcher) >= 1:
        return False


@login_required
def fail(request):
    return render(request, 'bootcamp_recruiter/fail.html', {})


def heroes(request):
    # gets day of the week - selects user
    today = datetime.datetime.now().strftime("%A").lower()
    hero_list = ['jack','kobebryant','rickyrozay','therock','sophiaamoruso','shondarhimes','BarackObama']
    api = get_twitter(request.user)

    if today == 'monday':
        hero_status = hero_list[0]
    elif today == 'tuesday':
        hero_status = hero_list[1]
    elif today == 'wednesday':
        hero_status = hero_list[2]
    elif today == 'thursday':
        hero_status = hero_list[3]
    elif today == 'friday':
        hero_status = hero_list[4]
    elif today == 'saturday':
        hero_status = hero_list[5];
    elif today == 'sunday':
        hero_status = hero_list[6];

    statuses = api.GetUserTimeline(screen_name=hero_status,count=50,include_rts=False)

    # filter tweet to only include from last week
    today = datetime.datetime.today()
    lastweek = today - timedelta(days=7)
    format_lastweek = lastweek.strftime("%b %d")
    new_format = format_lastweek.split()

    # gets tweet with the most amount of favorites and retweets
    tweet_counter = 0
    for s in statuses:
        counter = s.favorite_count + s.retweet_count
        tweet_day = s.created_at.split()
        # if month is not the same - add 30 days to date
        if new_format[0] != tweet_day[1]:
            tweet_day[2] = int(tweet_day[2]) + 30

        if int(tweet_day[2]) > int(new_format[1]) and counter > tweet_counter:
            tweet_counter = counter;
            tweet = s

    return render(request, 'bootcamp_recruiter/holditdown.html', {'tweet': tweet})


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
