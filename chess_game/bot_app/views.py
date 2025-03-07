from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from minimax_bot import MinimaxBot # type: ignore
import chess


def play_chess(request):
    return render(request, 'bot_app/chess_game.html')


bot = MinimaxBot()

@csrf_exempt  # Allows POST requests from the front-end
def bot_move(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        fen = data.get('fen')

        # Create a chess board from the FEN
        board = chess.Board(fen)

        # Bot move
        best_move = bot.best_move(board)

        return JsonResponse({'move': best_move.uci()})
