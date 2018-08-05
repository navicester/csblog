# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from django.template import RequestContext
from django.shortcuts import render_to_response, render

from bookmarks.forms import *
from bookmarks.models import *

def main_page(request):
    ################ 1
    # output = u'''
    #     <html>
    #         <head><title>%s</title></head>
    #         <body>
    #             <h1>%s</h1><p>%s</p>
    #         </body>
    #     </html>
    # ''' % (
    #     u'Django Bookmarks',
    #     u'Welcome to Django Bookmarks',
    #     u'Where you can store and share bookmarks!'
    # )
    # return HttpResponse(output)

    ################ 2
    # template = get_template('main_page.html')
    # variables = Context({
    #     'head_title': u'Django Bookmarks',
    #     'page_title': u'Welcome to Django Bookmarks',
    #     'page_body': u'Where you can store and share bookmarks!'
    # })

    # variables = {
    #     'head_title': u'Django Bookmarks',
    #     'page_title': u'Welcome to Django Bookmarks',
    #     'page_body': u'Where you can store and share bookmarks!'
    # } 

    # variables = {'user': request.user}

    # output = template.render(variables)
    # return HttpResponse(output) 

    return render_to_response(
        'main_page.html',
        {'user': request.user}
        )


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')

    bookmarks = user.bookmark_set.all()
    template = get_template('user_page.html')
    
    # variables = {
    #     'username': username,
    #     'bookmarks': bookmarks
    # }
    
    # output = template.render(variables)
    # return HttpResponse(output)    

    return render_to_response(
        'main_page.html',
        {
            'username': username,
            'bookmarks': bookmarks
        }
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')    

def register_page(request):
    print request.method
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
                )
            # return HttpResponseRedirect('/')
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    # variables = RequestContext(request, {
    #     'form': form
    #     })
    variables = {
        'form': form
        }   
    # return render_to_response(
    #     'registration/register.html',
    #     context={'form': form}, 
    #     context_instance=RequestContext(request)
    #     )   
    # The context_instance parameter in render_to_response was deprecated in Django 1.8, and removed in Django 1.10.
    # The solution is to switch to the render shortcut, which automatically uses a RequestContext. 
    return render(request,
        'registration/register.html',
        {'form': form}
        )       

def bookmark_save_page(request):
    if request.method == 'POST':
        form = BookmarkSaveForm(request.POST)
        if form.is_valid():
            # Create or get link.
            link, dummy = Link.objects.get_or_create(
                url=form.cleaned_data['url']
            )
            # Create or get bookmark.
            bookmark, created = Bookmark.objects.get_or_create(
                user=request.user,
                link=link
            )
            # Update bookmark title.
            bookmark.title = form.cleaned_data['title']
            # If the bookmark is being updated, clear old tag list.
            if not created:
                bookmark.tag_set.clear()
            # Create new tag list.
            tag_names = form.cleaned_data['tags'].split()
            for tag_name in tag_names:
                tag, dummy = Tag.objects.get_or_create(name=tag_name)
                bookmark.tag_set.add(tag)
            # Save bookmark to database.
            bookmark.save()
            return HttpResponseRedirect(
                '/user/%s/' % request.user.username)

    else:
        form = BookmarkSaveForm()
    
    variables = {"form": form}
    return render(
            request,
            'bookmark_save.html',
            variables
        )
