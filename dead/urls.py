
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from accounts.views import signup
from dead import settings
from publication.views import index

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

