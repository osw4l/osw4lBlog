from django.contrib import admin
from . import models
from . import forms
# Register your models here.


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['titulo', 'created', 'last_update', 'archive']
	actions = ['archivar', 'desarchivar']

	def archivar(self, request, queryset):
		queryset.update(archive=True)

	def desarchivar(self, request, queryset):
		queryset.update(archive=False)

	archivar.short_description = 'archivar los elementos seleccionado/s'
	desarchivar.short_description = 'desarchivar los elementos seleccionado/s'

	def get_actions(self, request):
		actions = super().get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions


@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
	list_display = ['username', 'get_full_name', 'posts']
	form = forms.AutorForm


