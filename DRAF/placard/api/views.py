from rest_framework import generics, permissions, pagination
from rest_framework.response import Response

from placard.models import Placard
from .permissions import IsOwnerOrReadOnly
from .serializers import PlacardSerializer

class PlacardPageNumberPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 20

    def get_paginated_response(self, data):
        author = False
        user = self.request.user
        if user.is_authenticated:
            author = True
        context = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'author': author,
            'results': data,
        }
        return Response(context)



class PlacardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Placard.objects.all()
    serializer_class    = PlacardSerializer
    lookup_field        = 'slug'
    permission_classes  = [IsOwnerOrReadOnly]



class PlacardListCreateAPIView(generics.ListCreateAPIView):
    queryset            = Placard.objects.all()
    serializer_class    = PlacardSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class    = PlacardPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


