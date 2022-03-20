from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import render_start_page, render_order_page_test
from .views import render_reg_page
from .views import render_auth_page
from .views import render_lk_page
from .views import render_order_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', render_start_page, name='render_start_page'),
    path('order_test', render_order_page_test, name='render_order_page_test'),
    path('auth/', include('django.contrib.auth.urls')),
    path('lk', render_lk_page, name='render_lk_page'),
    path('order', render_order_page, name='render_order_page'),
    path('', include('recipes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
