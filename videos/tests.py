from django.test import TestCase

from .models import Video

class VideoModelTestCase(TestCase):
  def setUp(self):
    Video.objects.create(title='This is my title')
  
  def test_created_count(self):
    qs = Video.objects.all()
    self.assertEqual(qs.count(), 1)
