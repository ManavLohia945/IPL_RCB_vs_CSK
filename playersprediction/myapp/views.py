from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def generate_best_11_players(request):
    if request.method == 'POST':
        # Process JSON data received from the request
        data = json.loads(request.body)
        predicted_players_list = data.get('players', [])
        # Perform any necessary processing here
        return JsonResponse({'status': 'success', 'players': predicted_players_list})
    else:
        # Handle other request methods (e.g., GET)
        return JsonResponse({'message': 'Use POST request to generate best 11 players'})

