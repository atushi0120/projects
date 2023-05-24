from django.db import models
from accounts.models import CustomUser

class Article(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name='ユーザー')
    latitude = models.FloatField(verbose_name='緯度')
    longitude = models.FloatField(verbose_name='経度')
    start_date = models.DateTimeField(verbose_name='開始日付')
    end_date = models.DateTimeField(verbose_name='終了日付',blank = True, null = True)
    title = models.CharField(max_length=255,verbose_name='記事名')
    content = models.TextField(verbose_name='コンテンツ')
    image = models.ImageField(upload_to='photos',verbose_name='画像イメージ', blank = True, null = True)
    def __str__(self):
        return self.title


# Create your models here.
