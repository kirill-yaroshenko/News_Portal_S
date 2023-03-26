from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name: str = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name: str = 'news/create_news.html'

    form_class = ArticlesForm
    

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name: str = 'news/delete_news.html'

    
def news(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/news.html', {'news': news})


def create_news(request):
    error: str = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error: str = 'Неверная форма!'
         
    form = ArticlesForm()

    data: list = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create_news.html', data)
