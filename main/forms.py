from django import forms
from .models import News, RelatedNews

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title']
        labels = {'title': 'Topic title'}
        
class RelTopicForm(forms.ModelForm):
    class Meta:
        model = RelatedNews
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}

