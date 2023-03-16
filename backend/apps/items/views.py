from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import ItemSerializer
from django.http import JsonResponse
from .models import Item
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class ItemList(generics.ListAPIView):
    # Get all posts, limit = 20
    queryset = Item.objects.order_by(
        'created_at').reverse().filter(status='active')
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']

    def get_paginated_response(self, data):
        return Response(data)
    
    def homepage(request):

        return render(request, 'index.html')

    def review(request):

        return render(request, 'review.html')
    
    def writeReview(request):

        return render(request, 'writeReview.html')
    
    def Review(request):

        return render(request, 'Review.html')
    
    def cart(request):

        return render(request, 'cart.html')
    
    

