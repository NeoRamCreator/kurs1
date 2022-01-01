from django.urls import reverse
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})
        # return reverse('view_news', kwargs={'news_id': self.pk})

    class Meta:
        ordering = ['-created_at']

    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'slug': self.slug, })


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'slug': self.slug, })
