from django.db import models


class Rubric(models.Model):
    name = models.CharField('Название', max_length=20, db_index=True)

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Bb(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ('-published',)

    def __str__(self):
        return f'{self.title}'

