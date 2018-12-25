from django.db import models
from shortner.models import shortnerURL
# Create your models here.
class clickeventManager(models.Manager):
    def create_event(self,shortnerinstance):
        if isinstance(shortnerinstance,shortnerURL):
            obj,created = self.get_or_create(shortner_url=shortnerinstance)
            obj.count+= 1
            obj.save()
            return obj.count
        return None
class clickevent(models.Model):
    shortner_url=models.OneToOneField(shortnerURL)
    count=models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects=clickeventManager()

    def __str__(self):
        return "{i}".format(i=self.count)