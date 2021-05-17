from django.db import models

# Create your models here.

class Todo(models.Model):
	title = models.CharField(max_length=500, verbose_name='Задача')
	description = models.TextField(blank=True, verbose_name='Описание')
	time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
	time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")
	done = models.BooleanField(default=False, verbose_name='Выполнено')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'ToDo'
		verbose_name_plural = 'ToDo'