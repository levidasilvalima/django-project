from rest_framework import viewsets


# Create your views here.

from .models import Unicorn 
from .serializers import UnicornSerializer

class UnicornViewSet(viewsets.ModelViewSet):

    queryset = Unicorn.objects.all()
    serializer_class = UnicornSerializer