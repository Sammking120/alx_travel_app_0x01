from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from listings.models import Post # type: ignore

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]