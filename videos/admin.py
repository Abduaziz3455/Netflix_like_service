from django.contrib import admin

# Register your models here.
from .models import VideoPublishedProxy, VideoAllProxy

class VideoAllAdmin(admin.ModelAdmin):
  list_display = ['title', 'video_id', 'id', 'is_published']
  search_fields = ['title']
  list_filter = ['active'] # right filtr navbar
  readonly_fields = ['id']
  
  # def published(self, obj): #
  #   return obj.active

admin.site.register(VideoAllProxy, VideoAllAdmin)


class VideoProxyAdmin(admin.ModelAdmin):
  list_display = ['title', 'video_id']
  search_fields = ['title']
  # list_filter = ['video_id']
  class Meta:
    model = VideoPublishedProxy
  
  # filter for only active videos
  def get_queryset(self, request):
    return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoPublishedProxy, VideoProxyAdmin)