from django.template import Context, loader, RequestContext
from django.views.decorators.csrf import csrf_protect
from models import Content
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.core.urlresolvers import reverse


def index(request):
    content_list = Content.objects.all().order_by('id').reverse()
    t = loader.get_template('blog/index.html')
    c = RequestContext(request, {
            'content_list':content_list,
    })
    return HttpResponse(t.render(c))

@csrf_protect
def write(request):
    try:
        b = Content(title=request.POST['title'], \
                        content=request.POST['content'], \
                        date=timezone.now())
        b.save()
    except:
        pass
    return HttpResponseRedirect('/blog')



