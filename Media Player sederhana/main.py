import pygame
import os

pygame.mixer.init()

#List untuk queu lagu
playlist = []

def play_music(music_file):
    #Memastikan file musik
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        print(f"[music_file] sedang diputar!")
    else:
        print("File tidak ditemukan!")
        
def stop_music():
    pygame.mixer.music.stop()
    print("Musik berhenti")

def main():
    print("Silahkan pilih lagu untuk diputar!")
    while True:
        choice = input("Ketik 'play' untuk memulai 'stop' untuk berhenti, 'add' untuk menambah lagu dan 'exit'. ").lower()
        if choice == "play":
            if playlist:
                current_song = playlist.pop(0)
                play_music(current_song)
            else:
                print("Tidak ada lagu silahkan ditambah!")
        elif choice == 'add':
            file = input("Masukkan nama lagu yang ingin ditambah (misal Felice.mp3): ")
            playlist.append(file)
        elif choice == "stop":
            stop_music()
        elif choice == "exit":
            print("Keluar dari program")
            break
        else:
            print("Tidak valid")
        
if __name__ == "__main__":
    main()
        
            