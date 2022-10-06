from django import forms
from .models import Blog
from django.core.exceptions import ValidationError
import re


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        """
        В этом методе мы получаем уже очищенные данные внутри словаря clean_title по ключу 'title'(это наименование поля).
        Дальше проверка не начинается ли эта строка с цифры. Если начинается, тогда исключение. Если
        """
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
