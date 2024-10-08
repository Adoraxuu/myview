from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug' 
    #slug_url_kwarg = 'slug' 

from django.template.response import TemplateResponse
def post_detail(request, slug):
    return TemplateResponse(request, 'blog/post_detail.html', {
        'post': get_object_or_404(Post.objects.all(), slug=slug),
    })