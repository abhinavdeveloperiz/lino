import re

from django.test import TestCase
from django.urls import reverse

from .views import PRODUCTS


class HomePageCarouselTests(TestCase):
    def test_homepage_renders_three_manual_swipe_carousel_slides(self):
        response = self.client.get("/")
        html = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(re.findall(r"<img\b[^>]*\bdata-carousel-slide(?:\s|>)", html)), 3)
        self.assertEqual(len(re.findall(r"<button\b[^>]*\bdata-carousel-dot(?:\s|>)", html)), 3)
        self.assertContains(response, 'class="absolute inset-0 bg-black/40"')
        self.assertContains(response, "touchstart")


class ProductPageTests(TestCase):
    def test_navigation_marks_current_page_active_on_desktop_and_mobile(self):
        active_links = {
            'home': '/',
            'about': '/about/',
            'products': '/products/',
            'product_detail': '/products/',
            'contact': '/contact/',
            'cart': '/cart/',
        }
        urls = {
            'home': reverse('home'),
            'about': reverse('about'),
            'products': reverse('products'),
            'product_detail': reverse('product_detail', args=['noir']),
            'contact': reverse('contact'),
            'cart': reverse('cart'),
        }

        for route_name, active_href in active_links.items():
            with self.subTest(route=route_name):
                response = self.client.get(urls[route_name])

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f'<a href="{active_href}" aria-current="page"')
                self.assertEqual(response.content.decode().count(f'<a href="{active_href}" aria-current="page"'), 2)

    def test_wishlist_controls_are_absent_from_storefront(self):
        for url in (reverse('home'), reverse('products'), reverse('product_detail', args=['noir'])):
            with self.subTest(url=url):
                response = self.client.get(url)

                self.assertEqual(response.status_code, 200)
                self.assertNotContains(response, 'toggleWishlist')
                self.assertNotContains(response, 'My Wishlist')
                self.assertNotContains(response, 'M21 8.25c0-2.485')

    def test_homepage_products_link_to_their_detail_pages(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        for product in PRODUCTS:
            self.assertContains(response, reverse('product_detail', args=[product['slug']]))

    def test_product_listing_links_each_product_to_its_detail_page(self):
        response = self.client.get(reverse('products'))
        html = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(re.findall(r'<article\b', html)), len(PRODUCTS))
        self.assertNotContains(response, '>Signature</span>')
        self.assertContains(response, 'class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"')
        self.assertContains(response, 'bg-white p-3 shadow-sm')
        self.assertContains(response, '-mx-3 -mt-3 relative aspect-square overflow-hidden bg-neutral-100')
        self.assertContains(response, 'id="product-search"')
        self.assertContains(response, 'id="family-filter"')
        self.assertContains(response, 'data-search="LINO Noir Woody · Amber · Intense Black pepper, bergamot Cedarwood, warm spices Amber, musk, vetiver"')
        self.assertContains(response, 'No fragrances match your search.')
        for product in PRODUCTS:
            self.assertContains(response, reverse('product_detail', args=[product['slug']]))

    def test_each_product_detail_page_renders_its_product_content(self):
        for product in PRODUCTS:
            with self.subTest(product=product['slug']):
                response = self.client.get(reverse('product_detail', args=[product['slug']]))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, product['name'])
                self.assertContains(response, product['top_notes'])
                self.assertNotContains(response, 'Rated 5 out of 5')
                self.assertNotContains(response, '★★★★★')

    def test_about_page_renders_premium_brand_sections(self):
        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Art of Being Remembered')
        self.assertContains(response, 'Thoughtfully composed')
        self.assertContains(response, 'The first impression')
        self.assertContains(response, 'Explore all fragrances')

    def test_unknown_product_detail_returns_not_found(self):
        response = self.client.get(reverse('product_detail', args=['unknown']))

        self.assertEqual(response.status_code, 404)
