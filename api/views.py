from rest_framework import generics
from .models import CarBrand, Car
from .serializers import CarBrandSerializer, CarSerializer



class CarBrandListCreateView(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarBrandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarListCreateView(generics.ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        brand_id = self.request.query_params.get('brand_id')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if brand_id is not None:
            queryset = queryset.filter(brand_id=brand_id)
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        return queryset


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer