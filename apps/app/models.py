from django.db import models
from django.contrib.auth.models import User
from ckeditor import fields
from django.urls import reverse_lazy
# Create your models here.


class Autor(User):
	class Meta:
		verbose_name='Autor'
		verbose_name_plural='Autores'

	def posts(self):
		return self.post_list().count()

	def post_list(self):
		return Post.objects.filter(autor=self)

	def get_posts_url(self):
		return reverse_lazy('app:post_autor', kwargs={
				'pk': self.pk
			})


class Post(models.Model):
	titulo = models.CharField(max_length=50)
	contenido = fields.RichTextField(config_name='awesome_ckeditor')
	imagen = models.URLField()
	created = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(auto_now=True)
	archive = models.BooleanField(default=False, editable=False)
	autor = models.ForeignKey(Autor, blank=True, null=True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def get_pk(self):
		return {
			'pk': self.pk
		}

	def get_absolute_url(self):
		return reverse_lazy(
			'app:detalle_post', 
			kwargs=self.get_pk()
		)
