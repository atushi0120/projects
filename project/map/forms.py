from django.forms import ModelForm
from .models import Article 

class ArticlePostForm(ModelForm):
    class Meta:
        model = Article
        fields = ['user','latitude','longitude','start_date','end_date','title','content','image']