from django.urls import path
#from . import views
from .views import HomeView, BlogDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView, ForumView
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('forum', ForumView.as_view(), name='forum-posts'), 
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete>', DeletePostView.as_view(), name='delete_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

