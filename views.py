from django.shortcuts import render

from images.models import Image


def home(request):
    images = Image.objects.filter(tags__name__in=["homepage"])[:9]

    return render(request, 'home.html', {'images': images})
    