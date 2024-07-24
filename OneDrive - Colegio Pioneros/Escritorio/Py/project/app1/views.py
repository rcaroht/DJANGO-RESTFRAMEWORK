from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import bd_raw_data_old, bd_raw_data_new
from .serializers import BdRawDataOldSerializer, BdRawDataNewSerializer
from datetime import date

class BdRawDataOldViewSet(viewsets.ModelViewSet):
    queryset = bd_raw_data_old.objects.all()
    serializer_class = BdRawDataOldSerializer

    @action(detail=False, methods=['post'])
    def transform(self, request):
        raw_data = bd_raw_data_old.objects.all()
        for data in raw_data:
            nombre_completo = f"{data.nombre} {data.apellido}"
            edad_nominal = date.today().year - data.edad.year
            bd_raw_data_new.objects.create(
                nombre_completo=nombre_completo,
                edad_nominal=edad_nominal
            )
        return Response({"status": "Transformación completada"})

class BdRawDataNewViewSet(viewsets.ModelViewSet):
    queryset = bd_raw_data_new.objects.all()
    serializer_class = BdRawDataNewSerializer
