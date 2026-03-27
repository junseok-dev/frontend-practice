from django.shortcuts import render
from django.conf import settings

def homepage(request):
    videos = [
        {
            'file': 'video_20260320.mp4',
            'title': '요즘 난리난 구글 Stitch #최신뉴스 #테크 #구글 #stitch',
            'youtube': 'https://www.youtube.com/shorts/LFBHDLvL2Yw',
            'date': '2026.03.20',
        },
        {
            'file': 'video_20260313.mp4',
            'title': '요즘 난리난 구글 Stitch #최신뉴스 #테크 #구글 #stitch',
            'youtube': 'https://www.youtube.com/shorts/LFBHDLvL2Yw',
            'date': '2026.03.13',
        },
    ]
    return render(request, 'frontend/homepage.html', {
        'YOUTUBE_API_KEY': settings.YOUTUBE_API_KEY,
        'videos': videos,
    })

def fanpage(request):
    return render(request, 'frontend/fanpage.html')

def chat(request):
    return render(request, 'frontend/chat.html')
