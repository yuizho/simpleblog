from models import Content
from django.forms import ModelForm, Textarea
from django.utils import timezone

class PostForm(ModelForm):
    class Meta:
        model = Content
        fields =('title', 'content')
        widgets = {
            'content': Textarea(attrs={'cols': 40, 'rows': 5}),
            }


