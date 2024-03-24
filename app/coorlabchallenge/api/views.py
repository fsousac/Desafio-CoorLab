import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Trip
from .serializers import TripSerializer


class ListTrip(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class SaveTrip(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def create(self, request, *args, **kwargs):
        dados_brutos = request.body

        try:
            dados_json = json.loads(dados_brutos)

            for k in range(len(dados_json)):
                serializer = self.get_serializer(data=dados_json[k])
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)

            return JsonResponse({'mensagem': 'Dados salvos com sucesso.'})

        except json.JSONDecodeError:
            return JsonResponse({'erro': 'Erro ao analisar o JSON.'}, status=400)
