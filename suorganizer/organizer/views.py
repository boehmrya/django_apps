
from django.shortcuts import (get_object_or_404, redirect, render)
from django.views.generic import View
from .models import Startup, Tag
from .forms import (NewsLinkForm, StartupForm, TagForm)
from .utils import (ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin)
from django.core.urlresolvers import reverse_lazy


class StartupList(View):
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'startup_list': Startup.objects.all()})


class StartupDetail(View):
    template_name = 'organizer/startup_detail.html'

    def get(self, request, slug):
        startup = get_object_or_404(Startup, slug__iexact=slug)
        return render(
            request,
            'organizer/startup_detail.html',
            {'startup': startup})


class TagList(View):
    template_name = 'organizer/tag_list.html'

    def get(self, request):
        return render(
            request,
            'organizer/tag_list.html',
            {'tag_list': Tag.objects.all()})


class TagDetail(View):
    template_name = 'organizer/tag_detail.html'

    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(
            request,
            'organizer/tag_detail.html',
            {'tag': tag})


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = 'organizer/tag_form_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')
    template_name = 'organizer/tag_confirm_delete.html'


class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


class StartupUpdate(ObjectUpdateMixin, View):
    form_class = StartupForm
    model = Startup
    template_name = 'organizer/startup_form_update.html'


class StartupDelete(ObjectDeleteMixin, View):
    model = Startup
    success_url = reverse_lazy('organizer_startup_list')
    template_name = 'organizer/startup_confirm_delete.html'


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'


class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name = 'organizer_newslink_form_update.html'

    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        content = {
            'form': self.form_class(instance = newslink),
            'newslink': newslink,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        bound_form = self.form_class(request.POST, instance = newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {
                'form': bound_form,
                'newslink': newslink,
            }
            return render(request, self.template_name, context)


class NewsLinkDelete(View):
    template_name = 'organizer/newslink_confirm_delete.html'

    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk = pk)
        return render(
            request,
            self.template_name,
            {'newslink': newslink})

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk = pk)
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)
