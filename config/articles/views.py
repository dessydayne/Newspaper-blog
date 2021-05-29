# articles/views.py
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import (CreateView, UpdateView, DeleteView) # new
from django.urls import reverse_lazy # new
from .models import Article


class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body', 'author',)

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    #success_url = reverse_lazy('article_detail')

class ArticleDeleteView(DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

		

# Create your views here.
