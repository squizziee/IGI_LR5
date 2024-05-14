from django.db import models


class NewsArticle(models.Model):
    title = models.CharField('Title of the article', max_length=200)
    spoiler = models.CharField('Text for preview of the article', max_length=200, default="default spoiler")
    cover = models.ImageField('Cover image for article')
    author = models.CharField('Author name', max_length=50)
    text = models.TextField('Full text of the article')
    date = models.DateField('Date on which article was posted')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News article"
        verbose_name_plural = "News articles"
