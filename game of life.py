import os
import time
import copy

# ==========================================
# 1. ADT ARRAY 2D
# ==========================================
class Array2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Inisialisasi grid dengan nilai 0 (mati)
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, r, c, value):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            self.grid[r][c] = value

    def get_cell(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c]
        return 0

# ==========================================
# 2. LOGIKA GAME OF LIFE
# ==========================================
class GameOfLife:
    def __init__(self, rows, cols):
        self.current_gen = Array2D(rows, cols)
        self.rows = rows
        self.cols = cols

    def seed_glider(self):
        """Mengisi pola dasar 'Glider' untuk simulasi"""
        coords = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        for r, c in coords:
            self.current_gen.set_cell(r, c, 1)

    def count_neighbors(self, r, c):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0: continue
                count += self.current_gen.get_cell(r + i, c + j)
        return count

    def next_generation(self):
        new_gen = Array2D(self.rows, self.cols)
        
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.count_neighbors(r, c)
                state = self.current_gen.get_cell(r, c)

                # Aturan Conway's Game of Life
                if state == 1 and (neighbors < 2 or neighbors > 3):
                    new_gen.set_cell(r, c, 0) # Mati
                elif state == 0 and neighbors == 3:
                    new_gen.set_cell(r, c, 1) # Hidup
                else:
                    new_gen.set_cell(r, c, state) # Tetap
        
        self.current_gen = new_gen

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.current_gen.grid:
            print("".join([" █ " if cell else " . " for cell in row]))
        print("\nTekan Ctrl+C untuk berhenti.")

# ==========================================
# RUNNER
# ==========================================
if __name__ == "__main__":
    game = GameOfLife(15, 20)
    game.seed_glider() # Memulai dengan pola glider

    try:
        while True:
            game.display()
            game.next_generation()
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nSimulasi selesai.")
