
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from . sitemaps import Cryptocurrencyinvestorsllc_Static_Sitemap
from django.contrib.sitemaps.views import sitemap


sitemaps =  {
    static : Cryptocurrencyinvestorsllc_Static_Sitemap(),
}

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('faq', views.faq_page, name='faq_page'),
    path('privacy', views.privacy_page, name='privacy_page'),
    path('terms', views.terms_page, name='terms_page'),
    path('contact', views.contact_page, name='contact_page'),
   # path('send_email', views.SendEmail, name='send_email'),

    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('', include('account.urls')),
    path('dlabtech_admin/', admin.site.urls),


   
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)