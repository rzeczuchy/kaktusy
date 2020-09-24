from django.urls import path
from . import views
from .views import PostDetail
from django.conf import settings
from django.conf.urls.static import static
 
app_name = 'app'
urlpatterns = [
   path('', views.index, name='index'),
   path('team', views.team, name='team'),
   path('blog', views.blog, name='blog'),
   path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
   path('privacy', views.privacy, name='privacy'),
   path('terms', views.terms, name='terms'),
   path('disclaimer', views.disclaimer, name='disclaimer'),
   path('sent', views.send_inquiry, name='sent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)