from rest_framework.viewsets import ModelViewSet

from core.models import Autor, autor
from core.serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer