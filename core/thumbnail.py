from django.http import HttpResponse, Http404
from django.core.cache import cache
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
import urllib.request
from PIL import Image
import io
import hashlib

@require_GET
@cache_control(max_age=86400, public=True)
def thumbnail_view(request):
    """
    GET /api/thumbnail/?url=<image_url>&w=600&h=750&q=72
    Fetches an image by URL, resizes it with Pillow, caches and returns JPEG.
    """
    url = request.GET.get('url', '').strip()
    try:
        w = min(int(request.GET.get('w', 600)), 1200)
        h = min(int(request.GET.get('h', 750)), 1500)
        q = min(int(request.GET.get('q', 72)), 90)
    except (ValueError, TypeError):
        w, h, q = 600, 750, 72

    if not url:
        raise Http404("url parameter required")

    cache_key = 'thumb_' + hashlib.md5(f"{url}_{w}_{h}_{q}".encode()).hexdigest()
    cached = cache.get(cache_key)
    if cached:
        return HttpResponse(cached, content_type='image/jpeg')

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as resp:
            raw_data = resp.read()
    except Exception:
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(url)

    try:
        img = Image.open(io.BytesIO(raw_data)).convert('RGB')
        img.thumbnail((w, h), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format='JPEG', quality=q, optimize=True, progressive=True)
        thumbnail_bytes = buf.getvalue()
    except Exception:
        return HttpResponse(raw_data, content_type='image/jpeg')

    cache.set(cache_key, thumbnail_bytes, 3600)
    return HttpResponse(thumbnail_bytes, content_type='image/jpeg')
