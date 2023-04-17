"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views as app_views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testPage/', app_views.test),
    path('posts/<int:post_id>', app_views.PostView.as_view(), name='post'),
    # path('posts/<str:post_id>', app_views.test_str),
    path('posts/add', permission_required('app.add_post')(app_views.AddPost.as_view()), name='add'),
    path('posts/', app_views.PostsView.as_view(), name='posts'),
    
]

urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)