from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import render_start_page
from .views import render_reg_page
from .views import render_auth_page
from .views import render_lk_page
from .views import render_order_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_start_page, name='render_start_page'),
    path('reg', render_reg_page, name='render_reg_page'),
    path('auth', render_auth_page, name='render_auth_page'),
    path('lk', render_lk_page, name='render_lk_page'),
    path('order', render_order_page, name='render_order_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
