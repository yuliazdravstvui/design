from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class User (models.Model):
    username= models.CharField(max_length=254, verbose_name='Лoгин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Пoчтa', unique=True, blank=False)
    password= models.CharField(max_length=254, verbose_name='Пapoль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пoльзователь')), default='user')

class Category (models.Model):
    name = models.CharField(max_length=254, verbose_name='Нaименование', blank=False)
    def __str__(self):
        return self.name


class Application(models.Model):
    STATUS_CHOICES = [
        ('N', 'Новая'),
        ('P', 'Принято в работу'),
        ('C', 'Выполнено'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the application")
    category = models.ManyToManyField(Category, help_text="Select a genre for this application")
    photo_file = models.ImageField(max_length=254,upload_to='image/',
                                   validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp'])])
    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS_CHOICES, default='N')
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)