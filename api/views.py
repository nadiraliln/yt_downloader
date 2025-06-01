from rest_framework.decorators import api_view
from rest_framework.response import Response
import yt_dlp

@api_view(['GET'])
def stream_download(request):
    video_url = request.query_params.get('url')
    if not video_url:
        return Response({"error": "No URL provided"}, status=400)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'quiet': True,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            video_url_direct = info['url']
            title = info.get('title', 'video')

        return Response({
            'stream_url': video_url_direct,
            'title': title
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)