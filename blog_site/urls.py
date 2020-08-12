from django.urls import path
from .views import create_post, MainPage, GetPost
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('create_post/', create_post, name='create_post'),
    path('read_post/<int:post_id>', GetPost.as_view(), name='read_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

