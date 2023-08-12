#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 00:45:03 2023

@author: dev
"""

import numpy as np
import tkinter as tk
from random import randint
import time

x_size = None
y_size = None
num_mines = None
text_size = None
buttons = None
root = None
message_label = None
start_time = None
game_over = None
stopwatch_label = None
flags_label = None

def init():
    global x_size
    global y_size
    global num_mines
    global text_size
    global buttons
    global root
    global message_label
    global start_time
    global game_over
    global stopwatch_label
    global flags_label

    x_size = 16
    y_size = 16
    num_mines = int(0.15*x_size*y_size)
    text_size = 8
    buttons = [[None for _ in range(y_size)] for _ in range(x_size)]
    root = tk.Tk()
    message_label = None
    start_time = None
    game_over = False
    stopwatch_label = None
    flags_label = None

    return

def generate_mines(x_size, y_size, num_mines):

    base_arr = np.zeros((x_size+2, y_size+2), dtype=np.uint8)

    for i in range(num_mines):
        x_rand = randint(1, x_size)
        y_rand = randint(1, y_size)
        base_arr[x_rand, y_rand] = 1
    return base_arr

def generate_hidden_numbers(base_arr, x_size, y_size):
    numbers = np.zeros((x_size+2, y_size+2), dtype=np.uint8)

    for i in range(1, x_size+1):
        for j in range(1, y_size+1):
            if base_arr[i, j]:
                continue
            else:
                numbers[i, j] = sum(sum(base_arr[i-1:i+2, j-1:j+2]))

    numbers = numbers[1:x_size+1, 1:y_size+1]
    return numbers

def unnamed():
    # will check upon clicking if region can be expanded
    return

def return_state(x, y):
    global buttons

    if buttons[x][y].cget("background") == "light gray":
        return "vacant"
    elif buttons[x][y].cget("background") == "sky blue":
        return "flagged"
    elif buttons[x][y].cget("background") == "crimson" or buttons[x][y].cget("background") == "green":
        return "burst"
    elif buttons[x][y].cget("background") == "gray":
        return "disabled zero"
    elif buttons[x][y].cget("background") == "white":
        return "disabled number"

def count_flags():
    global buttons

    flags = 0
    for i in range(x_size):
        for j in range(y_size):
            if buttons[i][j].cget("background") == "sky blue":
                flags += 1
    return flags

def check_win():
    global num_mines

    return count_flags() == num_mines

def burst(base_arr):
    global buttons
    global message_label
    global game_over

    game_over = True

    for i in range(x_size):
        for j in range(y_size):
            if base_arr[i, j] == 1:
                if buttons[i][j].cget("background") == "sky blue":
                    buttons[i][j].config(text="X", bg="light green", disabledforeground="white", state=tk.DISABLED)
                else:
                    buttons[i][j].config(text="X", bg="crimson", disabledforeground="white", state=tk.DISABLED)
                root.update()  # Force an update to apply changes immediately
                time.sleep(5/(x_size*y_size))  # Introduce a delay (in seconds) between bursting cells
            else:
                buttons[i][j].config(state=tk.DISABLED)

    message_label.config(text="Game Over! You Lost....")


def show_numbers(base_arr, numbers, x, y):
    global x_size
    global y_size
    global buttons
    global root

    pixels_to_check = [(x, y)]

    def reveal_next_cell():
        nonlocal pixels_to_check

        if pixels_to_check:
            x, y = pixels_to_check.pop(0)

            if base_arr[x, y] == 0 and buttons[x][y]['state'] != tk.DISABLED:
                if numbers[x, y] == 0:
                    buttons[x][y].config(bg="gray", state=tk.DISABLED)
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < x_size and 0 <= new_y < y_size:
                                pixels_to_check.append((new_x, new_y))
                else:
                    buttons[x][y].config(text=numbers[x, y], bg="white", disabledforeground="green")

            root.after(int(400/(x_size*y_size)), reveal_next_cell)  # Adjust the delay (in milliseconds) as needed

    reveal_next_cell()

def start_stopwatch():
    global stopwatch_label
    global start_time

    # print('stopwatch_label at start_stopwatch', stopwatch_label)
    start_time = time.time()
    update_stopwatch()

def update_stopwatch():
    global stopwatch_label
    global start_time

    if not game_over:  # Check if the stopwatch should continue updating
        current_time = int(time.time() - start_time)
        stopwatch_label.config(text="Time: {}:{}".format(current_time // 60, current_time % 60))
        stopwatch_label.after(1000, update_stopwatch)  # Continue updating every second
    else:
        current_time = int(time.time() - start_time)
        stopwatch_label.config(text="Time: {}:{}".format(current_time // 60, current_time % 60))


def reveal_cell(base_arr, numbers, x, y, left_click=False):
    global x_size
    global y_size
    global buttons
    global flags_label
    global num_mines
    global game_over

    if left_click:  # Left click (reveal)
        if buttons[x][y]['text'] == "F":
            return  # Skip burst if cell is flagged

        # if color of cell is white, do reveal_onclick
        if buttons[x][y].cget("background") == "white":
            reveal_onclick(base_arr, numbers, x, y)

        if base_arr[x, y] == 1:
            burst(base_arr)
            return
        elif numbers[x, y] == 0:
            show_numbers(base_arr, numbers, x, y)
        else:
            buttons[x][y].config(text=numbers[x, y], bg = "white", disabledforeground="green")

    else:  # Right click (flagging)
        if buttons[x][y]['text'] == "":
            buttons[x][y].config(text="F", bg="sky blue", disabledforeground="blue")
        elif buttons[x][y]['text'] == "F":
            buttons[x][y].config(text="", bg="light gray",  disabledforeground="black")

    if check_win():
        message_label.config(text="Congratulations! You won....")
        game_over = True
        for i in range(x_size):
            for j in range(y_size):
                buttons[i][j].config(state=tk.DISABLED)

    flags_label.config(text="Mines caught: {} / {}".format(count_flags(), num_mines))
    return


def reveal_onclick(base_arr, numbers, x, y):
    global buttons

    flags = 0
    for i in range(max(x-1, 0), min(x+2, x_size)):
        for j in range(max(y-1, 0), min(y+2, y_size)):
            if buttons[i][j].cget("background") == "sky blue":
                flags += 1

    if flags == numbers[x, y]:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                new_x, new_y = x + i, y + j
                if (0 <= new_x < x_size) and (0 <= new_y < y_size) and buttons[new_x][new_y].cget("background") != "white":
                    reveal_cell(base_arr, numbers, new_x, new_y, left_click=True)
                    time.sleep(1/(x_size*y_size))

    return



def start():
    global buttons
    global root
    global message_label
    global flags_label
    global stopwatch_label
    global num_mines
    global x_size
    global y_size

    init()

    # choice = simpledialog.askinteger("Game Size", "Choose the game size:\n1. 8x8\n2. 16x16\n3. 16x30", minvalue=1, maxvalue=3)

    # if choice == 1:
    #     x_size = y_size = 8
    #     num_mines = 10
    # elif choice == 2:
    #     x_size = y_size = 16
    #     num_mines = 40
    # elif choice == 3:
    #     x_size = 16
    #     y_size = 30
    #     num_mines = 99
    # else:
    #     print("Invalid choice. Exiting.")
    #     return

    root.title("Minesweeper")

    base_arr = generate_mines(x_size, y_size, num_mines)
    numbers = generate_hidden_numbers(base_arr, x_size, y_size)

    base_arr = base_arr[1:x_size+1, 1:y_size+1]
    num_mines = sum(sum(base_arr))

    # Create buttons and set up the game grid
    for i in range(x_size):
        root.rowconfigure(i, weight=1)
        for j in range(y_size):
            root.columnconfigure(j, weight=1)
            buttons[i][j] = tk.Button(
                root,
                width=4,
                height=2,
                text="",
                command=lambda i=i, j=j: reveal_cell(base_arr, numbers, i, j, left_click=True)
            )

            buttons[i][j].bind("<Button-3>", lambda event, i=i, j=j: reveal_cell(base_arr, numbers, i, j, left_click=False))
            buttons[i][j].grid(row=i, column=j, sticky="nsew")

    side_panel = tk.Frame(root)
    side_panel.grid(row=0, column=y_size, rowspan=x_size + 2, sticky="ns")

    stopwatch_label = tk.Label(side_panel, text="Time: 0", font=("Arial", 14))
    stopwatch_label.pack(pady=10)

    flags_label = tk.Label(side_panel, text="Mines caught: 0 / {}".format(num_mines), font=("Arial", 14))
    flags_label.pack(pady=10)

    # Create the message label
    message_label = tk.Label(root, text="", font=("Arial", 20))
    message_label.grid(row=x_size, columnspan=y_size, sticky="ew")

    # Create a Restart button
    restart_button = tk.Button(root, height=2, text="Restart", font=("Arial", 20), command=restart_game)
    restart_button.grid(row=x_size + 1, columnspan=y_size, sticky="ew")

    # print('stopwatch_label at start', stopwatch_label)
    start_stopwatch()

    root.mainloop()

def restart_game():
    global buttons
    global root
    global message_label
    global flags_label
    global num_mines
    global game_over

    game_over = False

    # Clear the message label
    message_label.config(text="")

    # Destroy old buttons
    for i in range(x_size):
        for j in range(y_size):
            buttons[i][j].destroy()

    # Reset the game state
    start()

    start_stopwatch()
    flags_label.config(text="Flags: 0 / {}".format(num_mines))

# TODO: REMAINING FEATURES
# 4. Select layout and number of mines