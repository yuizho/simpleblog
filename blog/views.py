from django.template import Context, loader, RequestContext
from django.views.decorators.csrf import csrf_protect
from models import Content
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.core.urlresolvers import reverse
from forms import PostForm

def index(request):
    content_list = Content.objects.all().order_by('id').reverse()
    """t = loader.get_template('blog/index.html')
    c = RequestContext(request, {
            'content_list':content_list,
            'form':PostForm, 
    })
    return HttpResponse(t.render(c))"""
    #short cut
    return render_to_response('blog/index.html',
                              RequestContext(request,
                                             { 'content_list':content_list,
                                               'form':PostForm,
                                             }))
    

@csrf_protect
def write(request):
    if request.method =='POST':
        content = Content(date = timezone.now())
        form = PostForm(request.POST, instance=content)
        if form.is_valid():
            """b = Content(title=form.cleaned_data['title'], \
                            content=form.cleaned_data['content'], \
                            date=timezone.now())
            b.save()"""
            form.save()
            return HttpResponseRedirect('/blog')
    else:
        form = PostForm()
    content_list = Content.objects.all().order_by('id').reverse()
    return render_to_response('blog/index.html',
                              RequestContext(request,
                                             { 'content_list':content_list,
                                               'form':PostForm,
                                             }))

