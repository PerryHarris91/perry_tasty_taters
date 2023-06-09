from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review

from rest_framework.response import Response


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.order_by('-created_at').all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item_id']




    def get_paginated_response(self, data):
       return Response(data)



class ReviewAdd(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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
