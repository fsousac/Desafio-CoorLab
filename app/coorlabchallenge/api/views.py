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
        # Obtém os dados brutos do corpo da solicitação POST
        dados_brutos = request.body

        try:
            # Converte os dados brutos JSON em um dicionário Python
            dados_json = json.loads(dados_brutos)

            for k in range(len(dados_json)):
                # Cria uma instância do serializador com os dados recebidos
                serializer = self.get_serializer(data=dados_json[k])
                serializer.is_valid(raise_exception=True)

                # Salva os dados no banco de dados
                self.perform_create(serializer)

            # Retorna uma resposta JSON indicando que os dados foram salvos com sucesso
            return JsonResponse({'mensagem': 'Dados salvos com sucesso.'})

        except json.JSONDecodeError:
            # Retorna uma resposta de erro se não for possível analisar o JSON
            return JsonResponse({'erro': 'Erro ao analisar o JSON.'}, status=400)
