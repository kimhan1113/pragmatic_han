from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto; text-align: left;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    # 부트스트랩 text-left class가 안먹혀서 style로 했음!
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']