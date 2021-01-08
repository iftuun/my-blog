from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Post
from .forms import ShareWithEmailForm

'''def post_list(req):
    objects = Post.published.all()
    paginator = Paginator(objects, 5)
    page = req.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not int, deliver first page 
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range, return last page
        posts = paginator.page(paginator.num_pages)

    return render(req, 'blog/post_list.html', {'posts': posts})'''

class PostListView(ListView):
    queryset = Post.objects.all()
    paginate_by = 15
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


def post_details(req, year, month, day, post_slug):
    post = get_object_or_404(Post,
        slug=post_slug,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day)
    return render(req, 'blog/post_details.html', {"post": post})

def share_post_email(req, year, month, day, post_slug, post_id):
    post = get_object_or_404(Post, id = post_id)
    post_url = req.build_absolute_uri(post.get_absolute_url())
    sent = False

    def sendMail(data):
        subject = data['name'] + " has Shared Something With You"
        message = f"{post.title} at {post_url}\n\n{cd['comments']}"
        send_mail(subject, message, 'iftycse028@gmail.com', [cd['to']])


    if req.method == 'GET':
        form = ShareWithEmailForm()
    if req.method == 'POST':
        form = ShareWithEmailForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sendMail(cd)
            sent = True
            
    return render(req, 'blog/share.html', {"form": form, "sent": sent})