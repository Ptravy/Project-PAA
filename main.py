from asyncio.windows_events import NULL
import time
from tkinter import messagebox, Tk
from turtle import window_width
import pygame
import sys
import random

# Ukuran Maps/Canvas 600x600
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Labirin Teknik")

# Membuat dan menggati logo/icon screen
icon = pygame.image.load("logo.jpg")
pygame.display.set_icon(icon)

# Membuat Ukuran Kotak 50x50 Cell
columns = 50
rows = 50

box_width = window_width // columns
box_height = window_height // rows
grid = []

class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 2, box_height - 2))

# Create Grid
for i in range(columns):
    arr =[]
    for j in range(rows):
        arr.append(Box(i, j))
        grid.append(arr)

# VARIABLE CONSTANT POSISI DROID DARI SUDUT PANDANG 2D
ATAS = 1
BAWAH = -1
KANAN = 2
KIRI = -2

# VARIABLE CEK SISI DROID
DEPAN_DROID = 1
KIRI_DROID = 2
KANAN_DROID = 3
BELAKANG_DROID = 4

class Courier : 
    def __init__(self, x, y):
        self.posisiX = x
        self.posisiY = y
         
        # KLIK ARAH UNTUK MENJALANKAN DROID
        self.Arah_Droid = ATAS 
        self.Arah_Droid = BAWAH
        self.Arah_Droid = KANAN
        self.Arah_Droid = KIRI
        self.Kurir_PICTURE = pygame.image.load('DroidM.png')

    def check_arah_kepala(self) :
        return self.Arah_Droid
    def check_posisi_baris(self) :
        return self.posisiY
    def check_posisi_kolom(self) :
        return self.posisiX

    def majukan_courier(self):
        if (self.Arah_Droid == ATAS):
            self.posisiY -= 1
        elif(self.Arah_Droid == BAWAH):
            self.posisiY += 1
        elif(self.Arah_Droid == KIRI):
            self.posisiX -= 1
        elif(self.Arah_Droid == KANAN):
            self.posisiX += 1
            
    def putar_belakang(self):
        if (self.Arah_Droid == ATAS):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 180)
            self.Arah_Droid = BAWAH
        elif(self.Arah_Droid == KANAN):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 180)
            self.Arah_Droid = KIRI
        elif(self.Arah_Droid == BAWAH):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 180)
            self.Arah_Droid = ATAS
        elif(self.Arah_Droid == KIRI):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 180)
            self.Arah_Droid = KANAN

    def putar_kanan(self):
        if (self.Arah_Droid == ATAS):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, -90)
            self.Arah_Droid = KANAN
        elif(self.Arah_Droid == KANAN):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, -90)
            self.Arah_Droid = BAWAH
        elif(self.Arah_Droid == BAWAH):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, -90)
            self.Arah_Droid = KIRI
        elif(self.Arah_Droid == KIRI):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, -90)
            self.Arah_Droid = ATAS
            
    def putar_kiri(self):
        if (self.Arah_Droid == ATAS):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 90)
            self.Arah_Droid = KIRI
        elif(self.Arah_Droid == KANAN):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 90)
            self.Arah_Droid = ATAS
        elif(self.Arah_Droid== BAWAH):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 90)
            self.Arah_Droid = KANAN
        elif(self.Arah_Droid == KIRI):
            self.Kurir_PICTURE = pygame.transform.rotate(self.Kurir_PICTURE, 90)
            self.Arah_Droid = BAWAH

    def cek_tempat_kosong(self,arah_cek,x,y):
        
        if (self.Arah_Droid == ATAS):
            if (arah_cek == DEPAN_DROID):
                if (grid[x][y-1].wall != True ):
                    return True
            if (arah_cek == KANAN_DROID):
                if (grid[x+1][y].wall != True ):
                    return True
            if (arah_cek == BELAKANG_DROID):
                if (grid[x][y+1].wall != True ):
                    return True
            if (arah_cek == KIRI_DROID):
                if (grid[x-1][y].wall != True ):
                    return True
        
        if (self.Arah_Droid == KANAN):
            if (arah_cek == DEPAN_DROID):
                if (grid[x+1][y].wall != True ):
                    return True
            if (arah_cek == KANAN_DROID):
                if (grid[x][y+1].wall != True ):
                    return True
            if (arah_cek == BELAKANG_DROID):
                if (grid[x-1][y].wall != True ):
                    return True
            if (arah_cek == KIRI_DROID):
                if (grid[x][y-1].wall != True ):
                    return True
        
        if (self.Arah_Droid == BAWAH):
            if (arah_cek == DEPAN_DROID):
                if (grid[x][y+1].wall != True ):
                    return True
            if (arah_cek == KANAN_DROID):
                if (grid[x+1][y].wall != True ):
                    return True
            if (arah_cek == BELAKANG_DROID):
                if (grid[x][y-1].wall != True ):
                    return True
            if (arah_cek == KIRI_DROID):
                if (grid[x-1][y].wall != True ):
                    return True
        
        if (self.Arah_Droid == KIRI):
            if (arah_cek == DEPAN_DROID):
                if (grid[x-1][y].wall != True ):
                    return True
            if (arah_cek == KANAN_DROID):
                if (grid[x][y-1].wall != True ):
                    return True
            if (arah_cek == BELAKANG_DROID):
                if (grid[x+1][y].wall != True ):
                    return True
            if (arah_cek == KIRI_DROID):
                if (grid[x][y+1].wall != True ):
                    return True

    # def gambar_courier(self, xInput,yInput):
    #     self.posisiX = xInput
    #     self.posisiY = yInput
    #     window.blit(self.Kurir_PICTURE, (xInput * window_width // columns, yInput * window_height // rows))
    def gambar_courier(self):
        window.blit(self.Kurir_PICTURE, (self.posisiX * window_width // columns, self.posisiY * window_height // rows))

def main():
    begin_search = False
    posisiStartX = 0
    posisiStartY = 0

    posisi_finis_kolom= 0
    posisi_finis_baris = 0

# Membuat Dinding acak
    for i in range(270) :
        wall_box_x = random.randint(0, columns - 1)
        wall_box_y = random.randint(0, rows - 1)
        wall_box = grid[wall_box_y][wall_box_x]
        wall_box.wall = True

 # Membuat posisi Start Courier
    for i in range(columns * rows):
        kurir_box_x = random.randint(0, columns - 1)
        kurir_box_y = random.randint(0, rows - 1)
        kurir_box = grid[kurir_box_y][kurir_box_x]
        if (grid[kurir_box_x][kurir_box_y].wall == False): 
            kurir_box.start = True
            kurirUtama = Courier(kurir_box_x, kurir_box_y)
            break
    
# Membuat Target Finish
    for i in range(columns * rows):
        target_box_x = random.randint(0, columns - 1)
        target_box_y = random.randint(0, rows - 1)
        if(grid[target_box_x][target_box_y].wall == False):
            target_box = grid[target_box_x][target_box_y]
            break
    
    target_box.target = True
    target_box_set = True
    target = pygame.image.load('DroidH.png')
    posisi_finis_kolom = target_box_x
    posisi_finis_baris = target_box_y
    pencarian = 0
        
    # MAIN PROGRAM ADA DI BAWAH INI
    start = 0
    while True:
        posisiBarisCourier = kurirUtama.check_posisi_baris()
        posisiKolomCourier = kurirUtama.check_posisi_kolom()

        for event in pygame.event.get():
            #Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Start Algorithm
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True
                
        # Garis Tepi Kotak
        window.fill ((0, 0, 0))

        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (20,20,20))
                if box.wall:
                    box.draw(window, (255, 165, 0))
                # if box.start:
                #     # window.blit(kurir, (i * window_width // columns, j * window_height // rows))
                if box.target:
                    box.draw(window, (20, 20, 20))
                    window.blit(target, (i * window_width // columns, j * window_height // rows))
        
        ###### CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######
        if(start == 0):
            if (grid[kurir_box_y][kurir_box_x].start == True):
                    window.blit(kurirUtama.Kurir_PICTURE, (posisiKolomCourier * window_width // columns, posisiBarisCourier * window_height // rows))
        else :
            if (grid[kurir_box_y][kurir_box_x].start == True):
                grid[posisiStartY][posisiStartX].draw(window, (20,20,20))
        ###### END CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######

    
        if (begin_search) :
            # all main searching function start here
            # kurirUtama.gambar_courier(posisiKolomCourier, posisiBarisCourier)
            
            kurirUtama.gambar_courier()
            test = 1

                        ###### START CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######
            if(start == 0):
                start = 1
            
            if (start == 1):
                posisiStartX = posisiKolomCourier
                posisiStartY = posisiBarisCourier
                start = 2

            # posisi sampai di droid hijau
            if (posisiBarisCourier == posisi_finis_baris and posisiKolomCourier == posisi_finis_kolom):
                
                for i in range(columns * rows):
                    target_box_x = random.randint(0, columns - 1)
                    target_box_y = random.randint(0, rows - 1)
                    if(grid[target_box_x][target_box_y].wall == False):
                        target_box = grid[target_box_x][target_box_y]
                        break
    
                target_box.target = True
                target_box_set = True
                target = pygame.image.load('DroidH.png')
                posisi_finis_kolom = target_box_x
                posisi_finis_baris = target_box_y
                
                pencarian = pencarian + 1
               
            # kurirUtama.putar_belakang()
            # print(kurirUtama.check_arah_kepala())

            # yg bug : 1, 3, 7

            # 1 posisi kurir di bawah dan kanan bendera 
            if (posisiBarisCourier > posisi_finis_baris and posisiKolomCourier > posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == ATAS):
                    #depan , kiri, kanan, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()

                elif (kurirUtama.check_arah_kepala() == KIRI):
                    # depan, kanan, kiri, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                
                elif (kurirUtama.check_arah_kepala() == KANAN):
                    # kiri, belakang, depan, kanan
                    if(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()

                elif (kurirUtama.check_arah_kepala() == BAWAH):
                   # kanan, belakang, depan, kiri
                    if(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    
            # 2 posisi kurir selalu di kiri dan di bawah bendera
            elif (posisiBarisCourier > posisi_finis_baris and posisiKolomCourier < posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == ATAS):
                    # depan, kanan, belakang, kiri
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
    
                elif (kurirUtama.check_arah_kepala() == KIRI): 
                    # kanan, belakang, kiri, depan
                    if(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()

                elif (kurirUtama.check_arah_kepala() == KANAN):
                    # depan, kiri, kanan, blekang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                
                elif (kurirUtama.check_arah_kepala() == BAWAH):
                    # kiri, belakang, depan, kanan
                    if(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
            # 3 poisis kurir di kanan dan di atas bendera
            if (posisiBarisCourier < posisi_finis_baris and posisiKolomCourier  > posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == ATAS):
                    # kiri, belakang, depam, kanan
                    if(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()

                elif (kurirUtama.check_arah_kepala() == KIRI):
                    #depan, kiri, kanan, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
    
                elif (kurirUtama.check_arah_kepala() == KANAN):
                    # kanan, belakang, depan, kiri
                    if(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    if(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()

                elif (kurirUtama.check_arah_kepala() == BAWAH):
                   # deapan, kanan, kiri, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()

            #4 posisi kurir selalu di kiri dan di atas bendera
            elif (posisiBarisCourier < posisi_finis_baris and posisiKolomCourier < posisi_finis_kolom): 
                if (kurirUtama.check_arah_kepala() == ATAS):
                    # kanan,belakang, depan, kiri
                    if(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
        
                elif (kurirUtama.check_arah_kepala() == BAWAH):
                    # depan, kiri, belakang, kanan
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()

                elif (kurirUtama.check_arah_kepala() == KIRI):
                    # kiri, belakng, kanan, depan
                    if(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
  
                elif (kurirUtama.check_arah_kepala() == KANAN):
                    # depan, kanan, kiri, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                
            #5 kurir selalu di atas dan se kolom dengan bendera
            if (posisiBarisCourier < posisi_finis_baris and posisiKolomCourier == posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == KIRI):
                    #kiri, depan, belakang, kanan
                    if(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                
                elif (kurirUtama.check_arah_kepala() == KANAN):
                    #kanan, depan, belakang, kiri
                    if(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()

                elif (kurirUtama.check_arah_kepala() == ATAS):
                    # belakang, kanan, kiri, depan
                    if(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
 
                elif (kurirUtama.check_arah_kepala() == BAWAH):
                   # depan, kiri, kanan, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()

            #6 kurir selalu di bawah dan se kolom dengan bendera
            elif (posisiBarisCourier > posisi_finis_baris and posisiKolomCourier == posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == KIRI):
                   # kanan, belakang, depan, kiri
                    if(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()

                elif (kurirUtama.check_arah_kepala() == KANAN):
                    # kiri, depan,belakan, kanan
                    if(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()

                elif (kurirUtama.check_arah_kepala() == ATAS):
                    # depan, kanan, kiri, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()

                elif (kurirUtama.check_arah_kepala() == BAWAH):
                    # belakang, kanan, kiri, depan
                    if(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                
            #7 posisi kurir selalu di sebelah kanan dan se baris dengan bendera
            if (posisiBarisCourier == posisi_finis_baris and posisiKolomCourier > posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == ATAS):
                    # kiri, depan, kanan, belakang
                    if(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()

                elif (kurirUtama.check_arah_kepala() == BAWAH):
                    # kanan, depan, kiri, belakang
                    if(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
           
                elif (kurirUtama.check_arah_kepala() == KIRI):
                    # depan, kanan, belakang, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == KANAN):
                    # belakang, kanan, depan, kiri
                    if(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
              
            #8 posisi kurir selalu di sebelah kiri dan se baris dengan bendera
            elif (posisiBarisCourier == posisi_finis_baris and posisiKolomCourier < posisi_finis_kolom):
                if (kurirUtama.check_arah_kepala() == ATAS):
                    # kanan, depan, belakang, kiri
                    if(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                
                elif (kurirUtama.check_arah_kepala() == BAWAH):
                    # kiri, depan, belakang, kanan
                    if(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()

                elif (kurirUtama.check_arah_kepala() == KIRI):
                    # belakang, kanan, kiri, depan
                    if(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()

                elif (kurirUtama.check_arah_kepala() == KANAN):
                    # depan, kanan, kiri, belakang
                    if (kurirUtama.cek_tempat_kosong(DEPAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.majukan_courier()
                    elif(kurirUtama.cek_tempat_kosong(KIRI_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kiri()
                    elif(kurirUtama.cek_tempat_kosong(KANAN_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_kanan()
                    elif(kurirUtama.cek_tempat_kosong(BELAKANG_DROID, posisiKolomCourier, posisiBarisCourier)):
                        kurirUtama.putar_belakang()

            if(pencarian == 1):
                        
                window.blit(target, (target_box_x * window_width // columns, target_box_y * window_height // rows))
                print("Droid Merah Telah Menemukan Posisi Droid Hijau")
                time.sleep(3)
                return False
            
            time.sleep(1)
    
        pygame.display.flip()

main()