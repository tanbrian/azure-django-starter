from django.views import generic

from .models import Video


class IndexView(generic.ListView):
    template_name = 'videos/index.html'
    context_object_name = 'video_list'

    def get_queryset(self):
        return Video.objects.all()
