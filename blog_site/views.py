from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm


class MainPage(ListView):
    model = Post
    template_name = 'blog_site/main_page.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['first_post'] = Post.objects.all().order_by('-created_at').first()
        return context

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')[:10]


def create_post(request):
    return render(request, 'blog_site/create_post.html')


class GetPost(DetailView):
    model = Post
    template_name = 'blog_site/full_post.html'
    pk_url_kwarg = 'post_id'


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data['image'])
            print(form.cleaned_data)
            print(request.FILES)
            if request.FILES:
                form.cleaned_data['image'] = request.FILES['image']
            Post.objects.create(**form.cleaned_data)
            return redirect('main_page')
    else:
        form = PostForm()
    return render(request, 'blog_site/create_post.html', {'form': form})
