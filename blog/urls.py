from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='bloglist'),
    path('blog/', views.bloglist, name='bloglist'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/',views.post_delete,name='post_delete'),
    path('editorjs/', include('django_editorjs_fields.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)