from django.template import Context, loader, RequestContext
from models import Content
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.core.urlresolvers import reverse
from forms import PostForm

def index(request):
    content_list = Content.objects.all().order_by('id').reverse()
    return render_to_response('blog/index.html',
                              RequestContext(request,
                                             { 'content_list':content_list,
                                               'form':PostForm,
                                             }))

def write(request):
    if request.method =='POST':
        content = Content(date = timezone.now())
        form = PostForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = PostForm()
    content_list = Content.objects.all().order_by('id').reverse()
    return render_to_response('blog/index.html',
                              RequestContext(request,
                                             { 'content_list':content_list,
                                               'form':PostForm,
                                             }))

