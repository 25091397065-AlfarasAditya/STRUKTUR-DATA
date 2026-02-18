"""
PROGRAM GAME OF LIFE - Conway's Game of Life
Dibuat untuk mendemonstrasikan ADT Array
"""

from game_of_life import GameOfLife
import time

def main():
    print("=" * 50)
    print("     🧬 CONWAY'S GAME OF LIFE 🧬     ")
    print("  Simulasi kehidupan dengan ARRAY    ")
    print("=" * 50)
    print("\nAturan SIMPEL:")
    print("1. Hidup (2-3 tetangga) → Tetap hidup")
    print("2. Hidup (0-1 tetangga) → Mati (kesepian)")
    print("3. Hidup (≥4 tetangga) → Mati (overpopulasi)")
    print("4. Mati (3 tetangga) → Hidup (lahir)\n")
    
    # Buat grid 10x10
    game = GameOfLife(10, 10)
    
    # 🔴 CONTOH POLA dari dokumen!
    # Pola blok (stabil)
    print("📌 Contoh 1: POLA BLOK (Stabil)")
    game.set_hidup(4, 4)
    game.set_hidup(4, 5)
    game.set_hidup(5, 4)
    game.set_hidup(5, 5)
    
    # Simulasi 3 generasi
    for gen in range(1, 4):
        print(f"\n🎮 Generasi {gen}:")
        game.tampilkan()
        game.simpan("hasil/generasi.txt", gen)
        game.generasi_berikutnya()
        time.sleep(1)
    
    # Reset game
    print("\n" + "=" * 50)
    print("📌 Contoh 2: POLA GLIDER (Bergerak)")
    game = GameOfLife(10, 10)
    
    # Pola glider
    game.set_hidup(2, 3)
    game.set_hidup(3, 4)
    game.set_hidup(4, 2)
    game.set_hidup(4, 3)
    game.set_hidup(4, 4)
    
    # Simulasi 5 generasi
    for gen in range(1, 6):
        print(f"\n🎮 Generasi {gen}:")
        game.tampilkan()
        game.generasi_berikutnya()
        time.sleep(1)
    
    print("\n✅ Simulasi selesai!")
    print("📁 Hasil tersimpan di folder 'hasil/'")

if __name__ == "__main__":
    main()
