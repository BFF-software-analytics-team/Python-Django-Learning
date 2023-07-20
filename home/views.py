from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Student
from .forms import PostForm, StudentForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.

def home(request):
    post = Post.objects.all()
    context = {
        'name': 'John Doe',
        'age': 30,
        'post': post
    }
    return render(request, 'home.html', context)

def post_create_update(request):
    if request.method == 'POST':
        # If the form is submitted
        form = PostForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post_id')
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            if post_id:
                # Update existing post
                post = Post.objects.get(pk=post_id)
                post.title = title
                post.content = content
                post.save()
            else:
                # Create a new post
                post = Post.objects.create(title=title, content=content)
            
            return redirect('home')  # Redirect to the post list page after saving
    else:
        # If it's a GET request or there are form errors
        post_id = request.GET.get('post_id')  # Get the post ID from the query string
        if post_id:
            # Edit existing post
            post = Post.objects.get(pk=post_id)
            form = PostForm(instance=post)
        else:
            # Create new post
            form = PostForm()
    
    context = {'form': form}
    return HttpResponse(context)

def index(request):
    return HttpResponse("Index Page")

def email(request):
    return render(request, 'email.html')

def email_validation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            validate_email(email)
            # Email is valid, proceed with your logic
            messages.success(request, 'Email is valid.')
        except ValidationError:
            messages.error(request, 'Invalid email.')
    return render(request, 'validate.html')