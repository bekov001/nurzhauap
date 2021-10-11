from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from example import settings

THEMES = (
    ('Программирование_programming', 'Программирование'),
    ('Математика_math', 'Математика'),
    ('Русский язык_rus', 'Русский язык'),
    ('Русская литература_ruslit', 'Русская литература'),
    ('Английский_eng', 'Английский')
)


class Profile(AbstractUser):
    username = models.CharField("Имя пользователя", max_length=100, unique=True)
    desc = models.CharField("Описание", max_length=1000,
                            default="Дураки не любят гениальных, "
                                    "ненавидь меня это нормально")
    avatar = models.ImageField("Фото", upload_to="media/avatars",
                               default="media/avatars/avatar.jpg")
    password = models.CharField("Пароль", max_length=500)

    def get_absolute_url(self):
        return f"/profile/{self.id}"


class Category(models.Model):
    theme = models.CharField(max_length=28, choices=THEMES,
                             default='math')

    def __str__(self):
        return self.theme

    def get_absolute_url(self):
        return f"/category/{self.id}"


class Task(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Автор вопроса", blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    title = models.CharField('Название', max_length=50)
    task = models.TextField("Описание", max_length=1500)
    img = models.ImageField(upload_to=r"media", null=True, blank=True)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/post/{self.id}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural ="Задачи"


class Comments(models.Model):
    article = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Вопрос", blank=True, null=True, related_name="comments_task")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Автор комментария", blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name="Текст", max_length=1500)
    img = models.ImageField(upload_to=r"media", null=True, blank=True)
    status = models.BooleanField(verbose_name="Видимость", default=False)
