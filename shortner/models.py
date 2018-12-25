from django.conf import settings
from django.db import models
from  .utils import code_generator,create_shortcode
#from django.core.urlresolvers import reverse
from django_hosts import reverse
from .validators import validate_dot_com,validate_url
# Create your models here.
SHORTCODE_MAX= getattr(settings,"SHORTCODE_MAX",15)
class shortnerURLmanager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main=super(shortnerURLmanager,self).all(*args,**kwargs)
        qs=qs_main.filter(active=True)
        return qs
    def refresh_shortcodes(self):
        qs= shortnerURL.objects.filter(id__gte=1)
        new_code=0
        for q in qs:
            qs.shortcode=create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_code+=1
        return "newcodes made: {i}".format(i=new_code)
class shortnerURL(models.Model):
    url = models.CharField(max_length=200,validators=[validate_url,validate_dot_com])
    shortcode=models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    objects=shortnerURLmanager()


    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode=create_shortcode(self)
        super(shortnerURL, self).save(*args,**kwargs)


    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode",kwargs={'shortcode':self.shortcode},scheme='http')
        return url_path