from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(blank=True,
                               verbose_name='Контент')  # атрибут blank означает, что это поле не обязательно к заполнению
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано')  # атрибут auto_now_add означает, что время будет сохранено единожды в момент создания
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Изменено')  # атрибут auto_now означает, что время каждого сохранения записи будут перезаписываться
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey(to='Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']  # Сортировка по полю


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True,
                             verbose_name='Название категории')  # db_index - индексирует это поле, делает это поле более быстрое для поиска

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # Сортировка по полю
