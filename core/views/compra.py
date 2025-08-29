from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models import Compra
from core.serializers import (
    CompraCreateUpdateSerializer,
    CompraListSerializer,
    CompraSerializer,
)


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name='administradores').exists():
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CompraCreateUpdateSerializer
        if self.action == 'list':
            return CompraListSerializer
        return CompraSerializer

    def perform_create(self, serializer):
        # garante que sempre salva o usuário logado
        serializer.save(usuario=self.request.user)
