from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .utils import generate_short_url

def index(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_url = generate_short_url()

        url, created = URL.objects.get_or_create(long_url=long_url, defaults={'short_url': short_url})
        if not created:
            short_url = url.short_url

        return render(request, 'shortener/index.html', {'short_url': short_url})

    return render(request, 'shortener/index.html')

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    url.visits += 1
    url.save()
    return redirect(url.long_url)

def stats(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return render(request, 'shortener/stats.html', {'url': url})
