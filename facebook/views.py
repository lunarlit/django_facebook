from django.shortcuts import render, redirect
from facebook.models import Article, Comment
# Create your views here.

count = 0


def newsfeed(request):
    articles = Article.objects.all().order_by('-created_at')

    for article in articles:
        article.length = len(article.text)

    return render(request, 'newsfeed.html', {'articles': articles})


def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST['author'],
            text=request.POST['text'],
            password=request.POST['password']
        )
        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'article': article})


def new_feed(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            password=request.POST['password'],
            text=request.POST['content']
        )
        return redirect(f'/feed/{ new_article.pk }')

    return render(request, 'new_feed.html')


def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail')


    return render(request, 'edit_feed.html', {'article': article})


def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()
            return redirect('/')
        else:
            return redirect('/fail')

    return render(request, 'remove_feed.html', {'article': article})


def fail(request):
    return render(request, 'fail.html')


def event(request):

    global count
    count = count + 1
    lucky = "꽝..."

    if count == 7:
        lucky = "당첨!"

    return render(request, 'event.html', {'count': count, 'lucky':lucky})

def profile(request):
    return render(request, 'profile.html')

def play(request):
    return render(request, 'play.html')


def play2(request):
    name = '유승호'
    global count
    count = count + 1
    age = 18

    if age < 19:
        status = '미성년자'
    else:
        status = '성인'

    diary = ['11월 22일','11월  23일','11월 24일']

    return render(request, 'play2.html',{'name':name,
                                         'count':count,
                                         'status':status,
                                         'diary':diary})