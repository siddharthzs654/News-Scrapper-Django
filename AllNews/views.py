from django.shortcuts import render
from django.http import HttpResponse
from requests_html import HTMLSession
# Create your views here.

def todayNews(link):
    News = []
    session = HTMLSession()
    response = session.get(link)
    i = 0
    while(len(News) < 6):
        i+=1

        headfind = f'body > div.container > div > div.card-stack > div:nth-child({i}) > div > div.news-card-title.news-right-box > a > span'
        contentfind = f'body > div.container > div > div.card-stack > div:nth-child({i}) > div > div.news-card-content.news-right-box > div:nth-child(1)'
        imagefind = f'body > div.container > div > div.card-stack > div:nth-child({i}) > div > div.news-card-image'
    
        heading = response.html.find(headfind,first=True)
        content = response.html.find(contentfind,first=True)
        image = response.html.find(imagefind,first=True)

        try:
            News.append({
                'image' : image.attrs['style'].strip("background-image: url('")[:-2],
                'heading' : heading.text,
                'content' : content.text
                })
        except:
            pass
    
    return News[:3], News[3:]



def home(request):
    context = {
        'trendingNews' : todayNews('https://www.inshorts.com/en/read'),
        'worldNews' : todayNews('https://www.inshorts.com/en/read/world'),
        'technologyNews' : todayNews('https://www.inshorts.com/en/read/technology'),
        'sportsNews' : todayNews('https://www.inshorts.com/en/read/sports')
    }
    return render(request, 'AllNews/home.html', context)

