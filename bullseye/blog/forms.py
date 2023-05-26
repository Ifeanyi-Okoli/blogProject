from django.shortcuts import render
from .models import Post, Category, Comment
from django import forms

# Get choices for category field from the Category model
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

# Create a list of choices for the category field
for item in choices:
    choice_list.append(item)

# Form for creating or updating a post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')
        
        # Set widget attributes for each form field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title_tag here'}),
            'author': forms.Select(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content here'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content here'}),
        }
        

# Form for updating a post
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body',)
        
        # Set widget attributes for each form field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title_tag here'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content here'}),
        }
        
        
# Form for creating a comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
        # Set widget attributes for each form field
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content here'}),
        }
