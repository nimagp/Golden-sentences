from golds.models import gold
from django.shortcuts import render

# Create your views here.
def gold_list(request):
    posts=gold.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})