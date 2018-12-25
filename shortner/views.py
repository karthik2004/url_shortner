from django.views import View
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404
from analytics.models import clickevent
from.models import shortnerURL
from .forms import submitURL
# Create your views here.


#def shortner_redirect_view(request,shortcode=None,*args,**kwargs):
#     obj= get_object_or_404(shortnerURL,shortcode=shortcode)
#     return HttpResponse("hello {sc}".format(sc=obj.url))



class HomeView(View):
    def get(self,request,*args,**kwargs):
        the_form = submitURL()
        context= {
            "title": "submit url",
            "form": the_form
        }
        return render(request,'shortner/home.html',context)
    def post(selfself,request,*args,**kwargs):

        form=submitURL(request.POST)
        context ={
            "title":"Submit URL",
            "form": form
        }
        template="shortner/home.html"
        if form.is_valid():
            new_url=form.cleaned_data.get('url')
            obj, created=shortnerURL.objects.get_or_create(url=new_url)
            context={
                "object":obj,
                "created":created
            }
            if created:
                template="shortner/success.html"
            else:
                template="shortner/already-exists.html"

        return render(request,template,context)
class shortnerCBview(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        qs = shortnerURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count()!=1 and not qs.exists():
            raise Http404
        obj=qs.first()
        #obj=get_object_or_404(shortnerURL,shortcode=shortcode)
        print(clickevent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

