from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from ru import views,urls
from search import urls as search_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urls)),
    path('',include(search_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
