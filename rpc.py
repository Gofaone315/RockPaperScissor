import random
import os
import time
import json
import socket

choices = ["rock", "paper", "scissor"]

if not os.path.exists(".config"):
    os.makedirs(".config")

def save_config(scores, filename):
    with open(f'.config/{filename}', 'w') as file:
        json.dump(scores, file, indent=4)
        
def load_local_scores():
    if not os.path.exists('.config/local_scores.json'):
        return {
            "computer": 0,
            name: 0,
        }
    else:
        with open('.config/local_scores.json', 'r') as file:
            return json.load(file)
        
def load_multiplayer_scores():
    if not os.path.exists('.config/multiplayer_scores.json'):
        return {
            name: 0,
            "opponent": 0
        }
    else:
        with open('.config/multiplayer_scores.json', 'r') as file:
            return json.load(file)
        
if not os.path.exists(".username.rpc"):
    name = input("Enter Your Username: ")
    f=open(".username.rpc", "w")
    f.write(name)
else:
    file=open(".username.rpc", "r")
    name = file.read()

local_scores = load_local_scores()
multiplayer_scores = load_multiplayer_scores()

def game_logic():
    print("1. Single Player\n2. Multiplayer\n3. Scores\n4. Exit")
    player_select = input(": ")
    if player_select == "1":
        local_play()
    elif player_select == "2":
        start_multiplayer()
    elif player_select == "3":
        display_scores()
    elif player_select == "4":
        print("GOODBYE!")
        exit()
    else:
        print("Wrong input")
        game_logic()

def local_play():
    user_choice = input("enter Rock/Paper/Scissor: ").lower()
    computer_choice = random.choice(choices)
    time.sleep(0.25)
    print(f"You: {user_choice}\nComputer: {computer_choice}")
    time.sleep(0.25)
    if user_choice == computer_choice:
        print("Tie")
    elif user_choice == "rock" and computer_choice == "scissor":
        print("You Win")
        local_scores[name] += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win")
        local_scores[name] += 1
    elif user_choice == "scissor" and computer_choice == "paper":
        print("You Win")
        local_scores[name] += 1
    else:
        print("You Lose")
        local_scores["computer"] += 1
    save_config(local_scores, "local_scores.json")
    question = input("Play Again? (Y/N): ").lower()
    if question == "y":
        local_play()
    else:
        game_logic()

def start_multiplayer():
    question = input("1. Create Room\n2. Join Room\n: ")
    if question == "1":
        host = "0.0.0.0"
        port = 12345
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen()
        print("Waiting for player 2 to connect...")
        conn, addr = sock.accept()
        print("Player 2 connected!")
        while True:
            player1_choice = input("Enter Rock/Paper/Scissor: ").lower()
            conn.send(player1_choice.encode())
            player2_choice = conn.recv(1024).decode()
            print(f"Player 2: {player2_choice}")
            if player1_choice == player2_choice:
                print("Tie")
            elif player1_choice == "rock" and  player2_choice== "scissor":
                print("You Win")
                multiplayer_scores[name] += 1
            elif player1_choice == "paper" and player2_choice == "rock":
                print("You Win")
                multiplayer_scores[name] += 1
            elif player1_choice == "scissor" and player2_choice == "paper":
                print("You Win")
                multiplayer_scores[name] += 1
            else:
                print("You Lose")
                multiplayer_scores["opponent"] += 1
            save_config(multiplayer_scores, "multiplayer_scores.json")
            
    elif question == "2":
        host = input("Enter host ip address: ")
        port = 12345
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print("Connected to player 1!")
        while True:
            player2_choice = input("Enter Rock/Paper/Scissor: ").lower()
            sock.send(player2_choice.encode())
            player1_choice = sock.recv(1024).decode()
            print(f"Player 1: {player1_choice}")
            if player2_choice == player1_choice:
                print("Tie")
            elif player2_choice == "rock" and  player1_choice== "scissor":
                print("You Win")
                multiplayer_scores[name] += 1
            elif player2_choice == "paper" and player1_choice == "rock":
                print("You Win")
                multiplayer_scores[name] += 1
            elif player2_choice == "scissor" and player1_choice == "paper":
                print("You Win")
                multiplayer_scores[name] += 1
            else:
                print("You Lose")
                multiplayer_scores["opponent"] += 1
            save_config(multiplayer_scores, "multiplayer_scores.json")
    else:
        print("Wrong Input")
        start_multiplayer()

def display_scores():
    print("1. Local Scores\n2. Multiplayer scores\n3. Back")
    ans = input(": ")
    if ans == "1":
        print(local_scores)
        display_scores()
    elif ans == "2":
        print(multiplayer_scores)
        display_scores()
    elif ans == "3":
        game_logic()
    else:
        print("Wrong input")
        display_scores()
       
game_logic()
