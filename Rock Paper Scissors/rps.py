def player(prev_play, opponent_history=[]):
  # Append the opponent's last move to the history
  if prev_play:
      opponent_history.append(prev_play)

  # If no history, play "R"
  if not opponent_history:
      return "R"

  # Analyze opponent's move history to predict their next move
  # Default move in case of insufficient data is "R"
  prediction = "R"

  if len(opponent_history) > 2:
      # Look at the last two moves
      last_two = tuple(opponent_history[-2:])

      # Create a dictionary of the frequencies of moves following the last_two
      move_counts = {"R": 0, "P": 0, "S": 0}

      for i in range(len(opponent_history) - 2):
          if tuple(opponent_history[i:i+2]) == last_two:
              next_move = opponent_history[i+2]
              move_counts[next_move] += 1

      # Predict the move the opponent is most likely to play
      prediction = max(move_counts, key=move_counts.get)

  # Counter the predicted move
  counter_moves = {"R": "P", "P": "S", "S": "R"}
  return counter_moves[prediction]
