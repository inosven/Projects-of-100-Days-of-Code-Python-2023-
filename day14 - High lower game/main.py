from art import logo, vs
from game_data import data
import random
from replit import clear

two_candidates = random.sample(data, 2)
score = 0
points = 0

def compare():
  global score
  if two_candidates[0]["follower_count"] > two_candidates[1]["follower_count"]:
    score += 1
    return score
  elif two_candidates[0]["follower_count"] == two_candidates[1][
      "follower_count"]:
    new_candidate()
    return score
  else:
    return -1


def new_candidate():
  two_candidates[1] = random.choice(data)


def game():
  global score
  global points
  print(logo)
  if points == -1:
    print(f"Sorry, that's wrong. Final score: {score}.")
    return
  elif points != 0:
    print(f"You're right! Current score: {score}.")

  print(
    f"Compare A：{two_candidates[0]['name']}, a {two_candidates[0]['description']}, from {two_candidates[0]['country']}"
  )
  print(vs)
  print(
    f"Against B：{two_candidates[1]['name']}, a {two_candidates[1]['description']}, from {two_candidates[1]['country']}"
  )
  A_or_B = input("Who has more followers? Type 'A' or 'B': ")
  if A_or_B == "B":
    two_candidates[0], two_candidates[1] = two_candidates[1], two_candidates[0]
  points = compare()
  new_candidate()
  clear()

  game()


game()
