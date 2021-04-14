from django.db import models
from django.http import HttpResponse
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

# from .models import Movie, Actor, Review
# from .serializers import (
#     MovieListSerializer,
#     MovieDetailSerializer,
#     ReviewCreateSerializer,
#     CreateRatingSerializer,
#     ActorListSerializer,
#     ActorDetailSerializer,
# )
# from .service import get_client_ip, MovieFilter


class FirstView(APIView):
    permission_classes = [IsAdminUser]
    filter_backends = (DjangoFilterBackend,)

    def get(self, request):
        return HttpResponse('123')

# class MovieListView(generics.ListAPIView):
#     """Вывод списка фильмов"""
#     serializer_class = MovieListSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = MovieFilter
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         movies = Movie.objects.filter(draft=False).annotate(
#             rating_user=models.Count("ratings",
#                                      filter=models.Q(ratings__ip=get_client_ip(self.request)))
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
#         )
#         return movies
