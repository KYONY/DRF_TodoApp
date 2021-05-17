from django.contrib import admin
from .models import Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
	list_display = ('id','title', 'description', 'time_create', 'time_update','done' )
	list_display_links = ('id','title',)
	search_fields = ('id', 'title','time_create', 'done')
	list_editable = ('done',)
	list_filter = ('done',)



admin.site.register(Todo, TodoAdmin)


admin.site.site_title = 'Админ-панель сайта ToDo'
admin.site.site_header = 'Админ-панель сайта ToDo'