from django.db import models
from django.forms import ModelForm
from ourcrestmont.itaco.models import *
 
class ProfileForm(ModelForm):
  class Meta:
      model = Foo
      exclude = ('user','score','field3',)