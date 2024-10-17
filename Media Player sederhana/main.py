import pygame
import os

pygame.mixer.init()

#List untuk queu lagu
playlist = []

#Untuk mencari lagu di folder
music_directory = #direktori folder musik

#Function untuk mencari lagu di file
def cari_musik(nama_lagu):
    for root, dirs, files in os.walk(music_directory):
        for file in files:
            if nama_lagu.lower() in file.lower() and file.endswith(("mp3", "wav")):
                return os.path.join(root, file)
    return None
    
#Fungsi untuk memutar lagu
def play_music(music_file):
    #Memastikan file musik
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        print(f"{music_file} sedang diputar!")
    else:
        print("File tidak ditemukan!")
 
#Fungsi untuk menghentikan lagu       
def stop_music():
    pygame.mixer.music.stop()
    print("Musik berhenti")
    

#Fungsi untuk men-skip lagu
def skip():
    if playlist:
        next_song = playlist.pop(0)
        play_music(next_song)
    else:
        print("Tidak ada lagu di playlist")

#Fungsi utama,dimana pengguna bisa memilih untuk memulai,menambah,menghentikan,dan keluar dari program
def main():
    print("Silahkan pilih lagu untuk diputar!")
    while True:
        choice = input("Ketik 'play' untuk memulai 'stop' untuk berhenti, 'add' untuk menambah lagu, 'skip' untuk skip lagu, 'view' untuk melihat playlist dan 'exit'. ").lower()
        if choice == "play":
            if playlist:
                current_song = playlist.pop(0)
                play_music(current_song)
            else:
                print("Tidak ada lagu silahkan ditambah!")
         #Pilihan bagi pengguna untuk memasukkan lagu ke dalam playlist       
        elif choice == 'add':
            file_name = input("Masukkan nama lagu yang ingin ditambah (misal Felice.mp3): ")
            full_path = cari_musik(file_name)
            if full_path:
                playlist.append(full_path)
                print(f"Lagu {file_name} berhasil ditambahkan! ")
            else:
                 print("Lagu tidak ditemukan")               
        elif choice == "stop":
            stop_music()
        elif choice == "view":
            print(file_name)
        elif choice == "skip":
            print(f"Skip lagu {file_name}")
            skip()
        elif choice == "exit":
            print("Keluar dari program")
            break
        else:
            print("Tidak valid")
        
if __name__ == "__main__":
    main()
        
            
