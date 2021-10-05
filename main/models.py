from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

THEMES = (
    ('Программирование_programming', 'Программирование'),
    ('Математика_math', 'Математика'),
    ('Русский язык_rus', 'Русский язык'),
    ('Русская литература_ruslit', 'Русская литература'),
    ('Английский_eng', 'Английский')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to=r"media/avatars", default=r"https://raw.githubusercontent.com/twbs/icons/main/icons/person-fill.svg",blank=True)

    def get_avatar(self):
        # variable PATH_TO_DEFAULT_STATIC_IMAGE depends on the enviroment
        # on development, it would be something like "localhost:8000/static/default_avatar.png"
        # on production, it would be something like "https://BUCKET_NAME.s3.amazonaws.com/static/default_avatar.png"
        return self.avatar if self.avatar else "/media/avatars/ava.svg"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор вопросы", blank=True,
                               null=True)
    title = models.CharField('Название', max_length=50)
    task = models.TextField("Описание", max_length=1500)
    img = models.ImageField(upload_to=r"media", null=True, blank=True)
    data = models.DateTimeField(auto_now=True)
    theme = models.CharField(max_length=28, choices=THEMES,
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
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name="Текст", max_length=1500)
    img = models.ImageField(upload_to=r"media", null=True, blank=True)
    status = models.BooleanField(verbose_name="Видимость", default=False)
