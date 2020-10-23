# Add libraries
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
import cart.views
import main.views
import order.views
import shop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('main/', include('main.urls')),
    path('order/', include('order.urls')),
    path('mypage/note/', include('note.urls')),

    # SSL 인증서 확인용
    url(r'^.well-known/acme-challenge/.*$',
        main.views.acme_challenge, name='acme-challenge'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
