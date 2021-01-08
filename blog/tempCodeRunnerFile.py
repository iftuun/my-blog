def post_list(req):
    posts = Post.published.all()
    return render(req, 'blog/post_list.html', {'posts': 999})