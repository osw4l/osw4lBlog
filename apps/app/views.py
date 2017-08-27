from django.shortcuts import render
from apps.utils.views import ListView, DetailView, BaseCreateView
from . import models, forms
from django.urls import reverse_lazy
# Create your views here.


class PostListView(ListView):
	model = models.Post
	template_name = 'posts.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['autores'] = models.Autor.objects.all() 
		return context 

	def get_queryset(self):
		try:
			if self.kwargs['pk']:
				print(self.kwargs['pk'])
				return self.model.objects.filter(autor_id=self.kwargs['pk'])
		except:
			print('error')
		return self.model.objects.all()


class PostDetailView(DetailView):
	model = models.Post
	template_name = 'post_detail.html'


class PostCreateView(BaseCreateView):
	form_class = forms.PostForm
	template_name = 'create_post.html'
	success_url = reverse_lazy('app:post')

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		if hasattr(self.request.user, 'autor'):
			kwargs['autor'] = self.request.user.autor
		return kwargs
