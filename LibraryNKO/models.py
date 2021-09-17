from django.db import models
from rest_framework.authtoken.admin import User


class NCOLibraryCategory(models.Model):
    category= models.CharField(max_length=300, verbose_name="Название категории библиотеки")

    class Meta:
        verbose_name = "Библиотека НКО "

    def __str__(self):
        return f'{self.category}'


class PublicationsNKO(models.Model):
    time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, verbose_name="Заголовок публикации ")
    all_text = models.TextField(null=True, verbose_name="Описание публикации")

    category = models.ForeignKey(NCOLibraryCategory, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Публикации ICNL"

    def __str__(self):
        return f'{self.category}'


class PublicationsFavourite(models.Model):
    public = models.ForeignKey(PublicationsNKO, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Избранное публикации  "

    def __str__(self):
        return self.public.title
