import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"  # Joueur humain commence toujours
        self.board = [""] * 9  # Tableau représentant le plateau de jeu
        self.game_mode = None  # Mode de jeu : "HvH" (Humain vs Humain) ou "HvAI" (Humain vs IA)
        self.buttons = []  # Liste des boutons du plateau
        self.create_menu()

    def create_menu(self):
        """Crée le menu principal pour choisir le mode de jeu."""
        self.clear_window()
        label = tk.Label(self.root, text="Choisissez le mode de jeu", font=("Arial", 16))
        label.pack(pady=20)

        btn_hvh = tk.Button(self.root, text="Humain vs Humain", font=("Arial", 14), command=lambda: self.start_game("HvH"))
        btn_hvh.pack(pady=10)

        btn_hvai = tk.Button(self.root, text="Humain vs IA", font=("Arial", 14), command=lambda: self.start_game("HvAI"))
        btn_hvai.pack(pady=10)

    def start_game(self, mode):
        """Démarre une nouvelle partie avec le mode sélectionné."""
        self.game_mode = mode
        self.current_player = "X"
        self.board = [""] * 9
        self.clear_window()
        self.create_board()

    def create_board(self):
        """Crée le plateau de jeu."""
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 30), width=5, height=2,
                               command=lambda idx=i: self.on_button_click(idx))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def clear_window(self):
        """Efface tous les widgets actuels de la fenêtre."""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.buttons = []

    def on_button_click(self, idx):
        """Gère le clic sur une case du plateau."""
        if self.board[idx] == "" and not self.check_winner():
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player, state=tk.DISABLED)
            if self.check_winner():
                self.end_game(f"Le joueur {self.current_player} a gagné!")
            elif "" not in self.board:
                self.end_game("Match nul!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.game_mode == "HvAI" and self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        """Fait jouer l'IA en tant que joueur 'O'."""
        empty_indices = [i for i, val in enumerate(self.board) if val == ""]
        if empty_indices:
            # Stratégie simple : choix aléatoire parmi les cases vides
            idx = random.choice(empty_indices)
            self.board[idx] = "O"
            self.buttons[idx].config(text="O", state=tk.DISABLED)
            if self.check_winner():
                self.end_game("L'IA a gagné!")
            elif "" not in self.board:
                self.end_game("Match nul!")
            else:
                self.current_player = "X"

    def check_winner(self):
        """Vérifie si un joueur a gagné."""
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Lignes
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colonnes
            (0, 4, 8), (2, 4, 6)              # Diagonales
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def end_game(self, message):
        """Termine la partie et affiche un message."""
        messagebox.showinfo("Fin de partie", message)
        self.create_menu()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
    