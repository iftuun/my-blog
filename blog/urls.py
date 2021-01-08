from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    #path('', views.post_list, name="post_list"),
    path('', views.PostListView.as_view(), name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', views.post_details, name='post_details'),
    #path('<str:k>', views.post_details, name='post_details')
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/share/<int:post_id>/', views.share_post_email, name='share_post_email')
]