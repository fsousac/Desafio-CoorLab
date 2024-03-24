from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import json


class ListTrip(APIView):
    def get(self, request):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_json_path = os.path.join(current_dir, '../../data.json')
        with open(data_json_path, 'r') as file:
            data = json.load(file)
        return Response(data)


class SaveTrip(APIView):
    def post(self, request):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_json_path = os.path.join(current_dir, '../../data.json')
        if os.path.exists(data_json_path):
            with open(data_json_path, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        new_data = request.data
        for k in new_data:
            existing_data['transport'].append(k)
        with open(data_json_path, 'w') as file:
            json.dump(existing_data, file)

        return Response(new_data, status=status.HTTP_201_CREATED)
