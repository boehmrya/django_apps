
from django.http.response import HttpResponse

from .models import Tag

from django.template import Context, loader

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = Context({'tag_list': tag_list})
    output = template.render(context)
    return HttpResponse(output)


def tag_detail(request):
    return HttpResponse()
