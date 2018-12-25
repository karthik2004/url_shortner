from django import forms
from .validators import validate_url,validate_dot_com


class submitURL(forms.Form):
    url = forms.CharField(label='submit',validators=[validate_url,validate_dot_com])


  #  #def clean(self):
       # cleaned_data=super(submitURL,self).clean()
       # print(cleaned_data)
   # def clean_url(self):
   #     url=self.cleaned_data['url']
        #print(url)
   #    url_validator = URLValidator()
   #     try:
   #        url_validator(url)
   #     except:
   #         raise forms.ValidationError("Invalid URL")
   #     return url