from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from  django import forms
import json
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from .models import News, RelatedNews
from .forms import NewsForm, RelTopicForm
from django.http import Http404

def index(request):
    """ Represents the index page """
    last_entries = RelatedNews.objects.all().order_by('-date_added')
    context = {'last_entries':last_entries[:]}
    return render(request, 'main/index.html', context)

@login_required
def news(request):
    """ Represents all topics """
    topics = News.objects.filter(owner=request.user).order_by('created_at')
    context = {'topics':topics}
    return render(request, 'main/news.html', context)

@login_required
def current_topic(request, topic_id):
    """ Shows all topics related current topic """
    current = News.objects.get(id=topic_id)
    if current.owner != request.user:
        raise Http404
    rel_current = current.relatednews_set.all()
    context={'rel_current': rel_current, 'current':current}
    return render(request, 'main/current_topic.html', context)

@login_required
def new_topic(request):
    """ Add a new topic """
    if request.method != 'POST':
        form = NewsForm()
    else:
        form = NewsForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('main:news')
    context = {'form':form}
    return render(request, 'main/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Create new entry related to the current topic """
    topic = News.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = RelTopicForm
    else:
        form = RelTopicForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.news = topic
            new_entry.save()
            return redirect('main:current_topic', topic_id=topic_id)
        
    context = {'form': form, 'topic':topic}    
    return render(request, 'main/new_entry.html', context)   

@login_required
def edit_entry(request, entry_id):
    """ Edit current entry """
    entry = RelatedNews.objects.get(id=entry_id)
    topic = entry.news
    if topic.owner != request.user:
        raise Http404 
    
    if request.method != 'POST':
        form = RelTopicForm(instance=entry)
    else:
        form = RelTopicForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:current_topic', topic_id=topic.id)
        
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'main/edit_entry.html', context)            
