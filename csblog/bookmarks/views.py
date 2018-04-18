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
    template = get_template('main_page.html')
    # variables = Context({
    #     'head_title': u'Django Bookmarks',
    #     'page_title': u'Welcome to Django Bookmarks',
    #     'page_body': u'Where you can store and share bookmarks!'
    # })
    variables = {
        'head_title': u'Django Bookmarks',
        'page_title': u'Welcome to Django Bookmarks',
        'page_body': u'Where you can store and share bookmarks!'
    } 
    output = template.render(variables)
    return HttpResponse(output)    


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')

    bookmarks = user.bookmark_set.all()
    template = get_template('user_page.html')

    # variables = Context({
    #     'username': username,
    #     'bookmarks': bookmarks
    # })
    
    # variables = {
    #     'username': username,
    #     'bookmarks': bookmarks
    # }
    
    # variables = Context({'user': request.user})    
    # output = template.render(variables)
    # return HttpResponse(output)    

    return render_to_response(
        'main_page.html',
        {'user': request.user}
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')    