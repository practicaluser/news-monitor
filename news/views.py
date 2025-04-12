# Create your views here.
from rest_framework import viewsets
from .models import Keyword
from .serializers import KeywordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import crawl_naver_news

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

@api_view(['GET'])
def get_news(request):
    keyword = request.GET.get('keyword')
    if not keyword:
        return Response({'error': 'No keyword provided'}, status=400)
    
    results = crawl_naver_news(keyword)
    return Response(results)