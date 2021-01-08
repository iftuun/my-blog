import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from blog.models import Post
from django.contrib.auth.models import User
from faker import Faker

#posts = Post.objects.get(title="HI")
me = User.objects.get(username="naim")

fk = Faker()

def getSlug(title):
    return title.replace(" ", "-").replace(".", "")

for i in range(50):
    title = fk.paragraph(nb_sentences=1)
    new_post = Post(
        title = title,
        slug = getSlug(title),
        author = me,
        body= fk.paragraph(nb_sentences=10),
        status="published"
    )
    new_post.save()

    print(new_post)