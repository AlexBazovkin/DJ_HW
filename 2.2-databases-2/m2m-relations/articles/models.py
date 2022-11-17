from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'



class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    # tag = models.ManyToManyField(Tag, related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    # таблица связка между статьей и тегом.
    # Именно здесь должно быть свойство `is_main`
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tags')




