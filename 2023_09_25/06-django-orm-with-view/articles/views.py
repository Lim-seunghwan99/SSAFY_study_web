from django.shortcuts import render, redirect
from .models import Article # 같은 위치에 있으면 .

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles" : articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk) # 왼쪽 : 테이블 컬럼 / 오른쪽 : 
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 1
    # article = Article()
    # article.title = request.GET.get('title')
    # article.content = request.GET.get('content')
    # article.save() # 남기려고 하면 저장을 해줘야 한다
    
    # 2 // 앞으로 쓸것!! (유효성 검사 => 저장)
    article = Article(title=title, content=content)
    article.save()
    
    # 3 /// 유효성 검사를 할  타이밍이 없다... 
    # Article.object.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    return redirect('articles:index')

def delete(request, pk):
    # 몇번 게시글을 삭제할 것인지 조회
    article = Article.objects.get(pk=pk)
    # 조회한 게시글을 삭제
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 수정하고자하는 게시글을 조회
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)