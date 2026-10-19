from django.http import Http404
from django.shortcuts import render

PRODUCTS = [
    {
        'slug': 'noir',
        'name': 'LINO Noir',
        'image': 'image/prod_noir.jpg',
        'price': 1499,
        'family': 'Woody · Amber · Intense',
        'description': 'A confident, magnetic fragrance with a dark warmth that lingers long after the moment has passed.',
        'top_notes': 'Black pepper, bergamot',
        'heart_notes': 'Cedarwood, warm spices',
        'base_notes': 'Amber, musk, vetiver',
        'tagline': 'For evenings that leave a lasting impression.',
    },
    {
        'slug': 'bloom',
        'name': 'LINO Bloom',
        'image': 'image/prod_bloom.jpg',
        'price': 1499,
        'family': 'Floral · Soft · Radiant',
        'description': 'A luminous floral scent that balances delicate petals with a soft, comforting warmth.',
        'top_notes': 'Fresh citrus, pear',
        'heart_notes': 'Rose, jasmine',
        'base_notes': 'Vanilla, soft musk',
        'tagline': 'A little light, wherever you go.',
    },
    {
        'slug': 'essence',
        'name': 'LINO Essence',
        'image': 'image/prod_essence.jpg',
        'price': 1499,
        'family': 'Fresh · Clean · Modern',
        'description': 'An effortless everyday fragrance with a crisp opening and a smooth, quietly memorable finish.',
        'top_notes': 'Citrus, green notes',
        'heart_notes': 'Aromatic herbs, white florals',
        'base_notes': 'Sandalwood, musk',
        'tagline': 'The beauty of being unmistakably you.',
    },
    {
        'slug': 'royal',
        'name': 'LINO Royal',
        'image': 'image/prod_royal.jpg',
        'price': 1799,
        'family': 'Spiced · Refined · Opulent',
        'description': 'A refined, enveloping composition with a rich character made for your most memorable occasions.',
        'top_notes': 'Saffron, bergamot',
        'heart_notes': 'Rose, amber',
        'base_notes': 'Oud, sandalwood',
        'tagline': 'Wear the moment like a crown.',
    },
    {
        'slug': 'oud',
        'name': 'LINO Oud',
        'image': 'image/prod_oud.jpg',
        'price': 1799,
        'family': 'Oud · Smoky · Luxurious',
        'description': 'A deep, expressive oud fragrance layered with elegant woods and a subtle floral softness.',
        'top_notes': 'Saffron, incense',
        'heart_notes': 'Oud, rose',
        'base_notes': 'Patchouli, amberwood',
        'tagline': 'A timeless signature in every drop.',
    },
    {
        'slug': 'white',
        'name': 'LINO White',
        'image': 'image/prod_white.jpg',
        'price': 1499,
        'family': 'Citrus · Airy · Elegant',
        'description': 'Clean, bright, and beautifully understated, this fresh blend feels like a new beginning.',
        'top_notes': 'Bergamot, mandarin',
        'heart_notes': 'White tea, neroli',
        'base_notes': 'White musk, light woods',
        'tagline': 'A fresh start, captured in a fragrance.',
    },
]

def home(request):
    return render(request, 'home.html', {'products': PRODUCTS})

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html', {'products': PRODUCTS})

def product_detail(request, slug):
    product = next((item for item in PRODUCTS if item['slug'] == slug), None)
    if product is None:
        raise Http404('Product not found')
    return render(request, 'product_detail.html', {'product': product})

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')
