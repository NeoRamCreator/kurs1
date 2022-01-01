from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator

# Create your views here.
from .forms import NewsForm
from .models import *
from .utils import MyMixin


def test1(request):
    objects = ['ob1', 'ob2', 'ob3', 'ob4', 'ob5', 'ob6', 'ob7']
    paginator = Paginator(objects, 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'test_site/test.html', {'page_obj': page_objects})


def test2(request):
    objects = ['ob1', 'ob2', 'ob3', 'ob4', 'ob5', 'ob6', 'ob7']
    paginator = Paginator(objects, 3)

    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'test_site/test2.html', {'page_obj': page_objects})


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'test_site/home_news_list.html'
    context_object_name = 'news'
    mixin_prop = 'hello world'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('главниея страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'test_site/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # template_name = 'test_site/view_news.html'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm  # название созданной формы
    template_name = 'test_site/add_news.html'
    # success_url = reverse_lazy('home')
    raise_exception = True


# def index(request):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#         'categories': categories
#     }
#     return render(request, 'test_site/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'test_site/category.html', {'news': news, 'category': category, 'categories': categories})


def def_view_test_index1(request):
    news = News.objects.all()
    # categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'test_site/test_index1.html', context=context)


# def get_category_test1(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     # categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'test_site/category_test1.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'test_site/view_news.html', {'news_item': news_item})


#
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             news = News.objects.create(**form.cleaned_data)
#             # return redirect('home_t1')
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'test_site/add_news.html', {'form': form})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'test_site/add_news.html', {'form': form})
