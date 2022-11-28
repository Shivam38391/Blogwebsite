from django.shortcuts import render
from .models import Post ,Comments

from .forms import CommentForm



# Create your views here.

def index(request):
    post = Post.objects.all()
    
    context = {'post': post}
    return render(request, 'myapp/index.html', context)

def post_page(request, slug):
    post = Post.objects.get(slug = slug)
    
    # post_id = request.POST.get('post_id') #from html
    comments = Comments.objects.filter(post = post )
    #commnent form
    form = CommentForm()
#logic of saving of comments in database with linked Post
    if request.POST:
        comment_form = CommentForm(request.POST) #without request.post this will take empty values
        if comment_form.is_valid :
            comment = comment_form.save(commit=False)
            post_id = request.POST.get('post_id') #from html
            
            post = Post.objects.get(id = post_id)
            comment.post = post
            comment.save()
            
    
    
    # logic view counts
    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count = post.view_count + 1
        
    post.save() 
        
    context = {'post': post, "form":form , 'comments': comments}
    return render(request, 'myapp/post.html', context)