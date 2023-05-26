from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView
urlpatterns = [
    # path('', views.home, name="Home"),  #function based view
    path('', HomeView.as_view(), name="Home"),  #class based view
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),  #class based view
    path("add_post/", AddPostView.as_view(), name="add_post"),  #class based view
    path("add_category/", AddCategoryView.as_view(), name="add_category"),  #class based view
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update_post"),  #function based view
    path("article/<int:pk>/delete", DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView.as_view(), name= 'category'),
    path("category-list", CategoryListView, name = 'category-list'),
    path("like/<int:pk>", LikeView, name = 'like_post'),
    path("article/<int:pk>/comment", AddCommentView.as_view(), name = 'add_comment'),
]
