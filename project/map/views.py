from django.shortcuts import render
from django.http import JsonResponse
from .models import Article
from django.core import serializers
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ArticlePostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Article

class IndexView(TemplateView):
    template_name = 'index.html'

@method_decorator(login_required,name='dispatch')
class CreateArticleView(CreateView):
    form_class = ArticlePostForm
    template_name = "post.html"
    success_url = reverse_lazy('map:post')

    def form_valid(self,form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()
        articles_json = serializers.serialize('json', articles)
        context['articles'] = articles_json
        return context


def delete_article(request, article_id):
    if request.method == 'POST':
        # ここで記事を削除するコードを記述します
        Article.objects.filter(pk=article_id).delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def get_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    data = {
        'fields': {
            'latitude': article.latitude,
            'longitude': article.longitude,
            'start_date': article.start_date.strftime('%Y-%m-%dT%H:%M'),  # 必要に応じて日付のフォーマットを調整
            'end_date': article.end_date.strftime('%Y-%m-%dT%H:%M') if article.end_date else None,
            'title': article.title,
            'content': article.content,
            # 画像フィールドに関するデータを追加する必要があれば追加
        }
    }
    return JsonResponse(data)