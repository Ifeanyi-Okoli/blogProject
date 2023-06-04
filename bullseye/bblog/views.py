from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

posts = [
    {
        'author': 'Bullseye',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'August 14, 2021'
    }
]



def home(request):
    context = {
        'posts': posts
    }    
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse("<h1>About Page</h1>")    
    return render(request, 'blog/about.html', {'title': 'About Page'})

class PostListView(LoginRequiredMixin, ListView):
    model = posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]


class PostDetailView(LoginRequiredMixin, DetailView):
    model = posts


class PostCreateView(LoginRequiredMixin, CreateView):
    model = posts
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = posts
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
