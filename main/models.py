from django.contrib.auth.models import User
from django.db import models

THEMES = (
    ('programming', 'Программирование'),
    ('math', 'Математика'),
    ('rus', 'Русский язык'),
    ('rus_lit', 'Русская литература'),
    ('eng', 'Английский')
)


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField("Описание", max_length=1500)
    img = models.ImageField(upload_to=r"media", null=True, blank=True)
    theme = models.CharField(max_length=11, choices=THEMES,
                             default='math')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/post/{self.id}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural ="Задачи"


class Comments(models.Model):
    article = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Вопрос", blank=True, null=True, related_name="comments_task")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария", blank=True, null=True)
    create_date = models.DateField(auto_now=True)
    text = models.TextField(verbose_name="Текст", max_length=1500)
    img = models.ImageField(upload_to=r"media", null=True, blank=True)
    status = models.BooleanField(verbose_name="Видимость", default=False)
