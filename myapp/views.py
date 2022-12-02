from django.shortcuts import render
from .models import Post ,Comments, Profile, Tag
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CommentForm, SubscribeForm



# Create your views here.

def index(request):
    post = Post.objects.all()
    top_posts = Post.objects.all().order_by('-view_count')[0:3]
    recent_posts = Post.objects.all().order_by('-last_update')[0:3]
    
    featured_blog = Post.objects.filter(is_featured=True)#it is queryset right now , not an object
    
    subscribe_form = SubscribeForm()
    subscribe_successful = None
    
    if featured_blog:
        featured_blog= featured_blog[0] # if there is multiple blog weonly pick first one
    
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            #this is something that we are initializing within the post request, so if the request is not post this need to have somevalue,, and that will be null ,mention at top
            subscribe_successful = "subscribed successfully"
            #to clear the form
            subscribe_form = SubscribeForm()
            
            
    
    context = {'post': post,'top_posts': top_posts, 'recent_posts':recent_posts , "featured": featured_blog,
               'subscribe_form':  subscribe_form, 'subscribe_success': subscribe_successful}
    return render(request, 'myapp/index.html', context)




def post_page(request, slug):
    post = Post.objects.get(slug = slug)
    
    # post_id = request.POST.get('post_id') #from html
    comments = Comments.objects.filter(post = post , parent= None) #by putting parent = None This willmake sure we only get comments and not replies 
    #commnent form
    form = CommentForm()
#logic of saving of comments in database with linked Post
    if request.POST:
        comment_form = CommentForm(request.POST) #without request.post this will take empty values
        if comment_form.is_valid :
            
            parent_obj = None #initially it is none
            #we will check here  , if our post request has parent then save reply
            if request.POST.get('parent'):
                #save reply
                parent = request.POST.get('parent') #id of comments against which the comments is done
                parent_obj = Comments.objects.get(id= parent) #
                if parent_obj: # if parent object exist ,if there is valid
                    
                    comment_reply = comment_form.save(commit=False)
                    
                    #also linked parent comment against which is posted
                    comment_reply.parent = parent_obj
                    #link it to post
                    comment_reply.post = post # this post is from upper code, slug wala
                    comment_reply.save()
                    return HttpResponseRedirect(reverse('post', kwargs={'slug':slug})) #"post" is url dont get confuse
                    
            
            else: #it is not true that means it is a comment , if request from comment_form u dont get a parent
                comment = comment_form.save(commit=False)
                post_id = request.POST.get('post_id') #from html
                
                post = Post.objects.get(id = post_id)
                comment.post = post
                comment.save()
                #fixing issue of comments submit on refresh
                return HttpResponseRedirect(reverse('post', kwargs={'slug':slug})) #"post" is url dont get confuse
    
    
    # logic view counts
    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count = post.view_count + 1
        
    post.save() 
        
    context = {'post': post, "form":form , 'comments': comments}
    return render(request, 'myapp/post.html', context)



#Tage page
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    top_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-view_count')[0:2]
    recent_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-last_update')[0:2]
    
    more_tags = Tag.objects.all()
    
    
    context = {
        "tag": tag, 
        "top_posts":top_posts,
        "recent_posts": recent_posts,
        'more_tags': more_tags,
    }
    return render(request, 'myapp/tag.html', context)


def author_page(request, slug):
    profile =  Profile.objects.get(slug=slug)
    top_posts = Post.objects.filter(author= profile.user).order_by('-view_count')[0:2]
    recent_posts = Post.objects.filter(author= profile.user).order_by('-last_update')[0:2]
    
    
    context = {
        "profile": profile, 
        "top_posts":top_posts,
        "recent_posts": recent_posts,
    }
    
    return render(request, 'myapp/author.html', context)
    
    