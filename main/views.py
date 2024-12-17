from rest_framework.views import APIView
from rest_framework.response import Response


class IndexAPIView(APIView):
    data = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    def get(self, request):
        return Response(self.data)


class AboutAPIView(APIView):
    data = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой классный, и какой хороший товар.',
    }

    def get(self, request):
        return Response(self.data)