from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class Cryptocurrencyinvestorsllc_Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['about_page', 'contact_page','home_page','faq_page','privacy_page','terms_page']

    def location(self, item):
        return reverse(item)




