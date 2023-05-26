from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment  # Importing necessary models
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # Importing generic views
from .forms import PostForm, EditForm, CommentForm  # Importing necessary forms
from django.urls import reverse_lazy, reverse  # Importing functions for URL handling

# Define views here

def LikeView(request, pk):
    # View for handling post likes
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    # View for rendering the home page with a list of posts
    model = Post
    template_name = "home.html"
    cats = Category.objects.all()
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        # Get additional context data for the view
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    # View for rendering the category list
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

class CategoryView(ListView):
    # View for rendering category-specific posts
    model = Post
    template_name = "categories.html"
    
    def get_context_data(self, *args, **kwargs):
        # Get additional context data for the view
        category_posts = Post.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["category_posts"] = category_posts                
        return context

class ArticleDetailView(DetailView):
    # View for rendering a detailed view of a single post
    model = Post
    template_name = "article_details.html"
    
    def get_context_data(self, *args, **kwargs):
        # Get additional context data for the view
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        context["cat_menu"] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    # View for adding a new post
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

class AddCommentView(CreateView):
    # View for adding a new comment
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html" 
    
    def form_valid(self, form):
        # Set the post_id for the comment based on the URL parameter
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('Home')

class AddCategoryView(CreateView):
    # View for adding a new category
    model = Category
    # form_class = PostForm
    template_name = "add_category.html"
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'body')
    
class DeletePostView(DeleteView):
    model = Post
    # form_class = EditForm
    template_name = "delete_post.html"
    success_url = reverse_lazy('Home')