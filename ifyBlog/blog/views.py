from django.shortcuts import render, redirect
from django.contrib.auth.models import User, login, authenticate
from .forms import LoginForm, SignUpForm, AddArticleForm
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect('home')
            form.save()
            return redirect('login')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('dashboard')
                # login(request, user)
                # return redirect('home')
            form.save()
            return redirect('login')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': 'articles'})

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # Add code to save the email for newsletter subscription
        return redirect('article_list')
       
    return render(request, 'subscribe.html')

@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'dashboard.html', {'articles': articles})


@login_required
def publish_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'publish_article.html', {'form': form})

@login_required
def update_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = ArticleForm(instance=article)
        return render(request, 'update_article.html', {'form': form})
    
@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id, author=request.user)
    if request.method == "POST":
        article.delete()
        return redirect('dashboard')
    return render(request, 'delete_article.html', {'article': article})


@staff_member_required
def admin_dashboard(request):
    users = User.pbjects.all()
    authors = User.objects.filter(is_staff=True)
    articles = Article.objects.all()
    return render(request, 'admin_dashboard.html', {'users':users, 'authors':authors, 'articles': articles})

@staff_member_required
def add_article(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AddArticleForm()
    return render(request, 'add_article.html', {'form': form})

@staff_member_required
def update_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = AddArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        else:
            form = AddArticleForm(instance=article)
        return render(request, 'update_article.html', {'form': form})
    
@staff_member_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        article.delete()
        return redirect('admin_dashboard')
    return render(request, 'delete_article.html', {'article': article})

@staff_member_required
def remove_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        user.delete()
        return redirect('admin_dashboard')
    return render(request, 'remove_user.html', {'user': user})

@staff_member_required
def remove_author(request, author_id):
    author = get_object_or_404(User, pk=author_id, is_staff=True)
    if request.method == "POST":
        author.delete()
        return redirect('admin_dashboard')
    return render(request, 'remove_author.html', {'author': author})