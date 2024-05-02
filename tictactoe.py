import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.start_game()

    def start_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', command=lambda row=i, col=j: self.click(row, col), height=3, width=6)
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, row, col):
        if self.board[row][col] == '' and not self.check_win():
            self.board[row][col] = self.player
            self.buttons[row][col]['text'] = self.player
            if self.check_win():
                messagebox.showinfo("Game Over", "Player " + self.player + " wins!")
                self.window.destroy()
                self.__init__()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_win(self):
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != '':
                return True
        for col in range(len(self.board)):
            check = []
            for row in self.board:
                check.append(row[col])
            if check.count(check[0]) == len(check) and check[0] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            return True
        return False

TicTacToe()