from django.shortcuts import render

# Create your views here.
# game/views.py

from django.shortcuts import render
from django.http import HttpResponse
import random

def play_game(request):
    if request.method == 'POST':
        choice = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choice)
        user_choice = request.POST.get('user_choice')
        result = None

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "Congratulations! You win!"
        else:
            result = "Sorry! You lose!"

        return render(request, 'game/play_game.html', {'computer_choice': computer_choice, 'result': result})

    return render(request, 'game/play_game.html')
