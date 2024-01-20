from django import forms
from app.models import *
from app.views import *

class TopicForm(forms.ModelForm):
    class Meta():       
        model=Topic
        fields='__all__'

class WebPageForm(forms.ModelForm):
    class Meta():
        model=WebPage
        fields='__all__'
        #fields=['topic_name','name','email']
        #exclude=['name','email']
        #labels={'topic_name':'Tn'}
        #widgets={'topic_name':forms.Textarea()}

class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'                                                                          