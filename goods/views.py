from django.views.generic import DetailView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.exceptions import NotFound
from .models import Products
from .serializers import ProductSerializer
from .utils import q_search


class CatalogAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        on_sale = self.request.query_params.get('on_sale', None)
        order_by = self.request.query_params.get('order_by', None)
        query = self.request.query_params.get('q', None)

        # Фильтрация
        if category_slug == "all":
            goods = super().get_queryset()
        elif query:
            goods = q_search(query)
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)

        if not goods.exists():
            raise NotFound("Товары не найдены")

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)

        return goods


class ProductAPIView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"


# class ProductView(DetailView):
#
#     slug_url_kwarg = "product_slug"
#     context_object_name = "product"
#
#     def get_object(self, queryset=None):
#         product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
#         return product
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.object.name
#         return context