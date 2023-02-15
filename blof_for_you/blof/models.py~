from django.db import models
from django.urls import reverse_lazy


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(blank=True,
                               verbose_name='Контент')  # атрибут blank означает, что это поле необязательно к заполнению
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано')  # атрибут auto_now_add означает, что время будет сохранено единожды в момент создания
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Изменено')  # атрибут auto_now означает, что время каждого сохранения записи будут перезаписываться
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey(to='Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']  # Сортировка по полю


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True,
                             verbose_name='Название категории')  # db_index - индексирует это поле, делает это поле более быстрое для поиска

    def get_absolute_url(self):
        return reverse_lazy('list_category',
                            kwargs={
                                'category_id': self.pk})  # Первым аргументом мы передаём название маршрута, вторым необходимый параметр для построения данного маршрута

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # Сортировка по полю
