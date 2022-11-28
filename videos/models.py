from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class VideoQuerySet(models.QuerySet):
  def published(self):
    now = timezone.now()
    return self.filter(
      state = Video.VideoStateOptions.PUBLISH,
      publish_timestamp_lte = now
    )

class VideoManager(models.Manager):
  def get_queryset(self):
    return VideoQuerySet(self.model, using=self._db)

class Video(models.Model):
  class VideoStateOptions(models.TextChoices):
    # CONSTANT = DB_VALUE, USER_DISPLAY_VA
    PUBLISH = 'PU', 'Published'
    DRAFT = 'DR', 'Draft'
    # UNLISTED = 'UN', 'Unlisted'
    # Private = 'PR', 'Private'

  title = models.CharField(max_length=220)
  description = models.TextField(blank=True, null=True)
  slug = models.SlugField(blank=True, null=True) #this-is-my-video
  video_id = models.CharField(max_length=220, unique=True)
  active = models.BooleanField(default=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  state = models.CharField(max_length=2, 
  choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT)
  publishtimestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
  objects = VideoManager()

  @property
  def is_published(self): #
    return self.active

  def save(self, *args, **kwargs):
    if self.state==self.VideoStateOptions.PUBLISH and self.publishtimestamp is None:
      print("Save as published")
      self.publishtimestamp = timezone.now()
    elif self.state==self.VideoStateOptions.DRAFT:
      self.publishtimestamp = None

    if self.slug is None:
      self.slug = slugify(self.title)
    super().save(*args, **kwargs)
    


class VideoPublishedProxy(Video):
  class Meta:
    proxy = True
    verbose_name = 'Published Video'
    verbose_name_plural = 'Published Videos'


class VideoAllProxy(Video): # using inheritance we can rename model
  class Meta:
    proxy = True
    verbose_name = 'All Video'
    verbose_name_plural = 'All Videos'