from django.conf.urls import url, include
from  . import views
urlpatterns = [
    url(r'^$', 
    	views.PostListView.as_view(), 
    	name='post'),

    url(r'^post_autor/(?P<pk>\d+)/$', 
    	views.PostListView.as_view(), 
    	name='post_autor'),

    url(r'^detalle-post/(?P<pk>\d+)/$', 
    	views.PostDetailView.as_view(),
    	name='detalle_post'),

    url(r'^crear-post/',
    	views.PostCreateView.as_view(),
    	name='crear_post')
]
