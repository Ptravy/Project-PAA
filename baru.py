from turtle import window_width
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Labirin Droid")
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
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 1, box_height - 1))

#Create Grid
for i in range(columns):
    arr =[]
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)
    
class Droid_Merah : 
    def __init__(self, x, y):
        self.posisiX = x
        self.posisiY = y
        self.Droid_Merah_PICTURE = pygame.image.load('DroidM.png')

    def check_posisi_baris(self) :
        return self.posisiY
    def check_posisi_kolom(self) :
        return self.posisiX

def cek_tempat_kosong(self,arah_cek,x,y):

    def gambar_(self):
        window.blit(self.Droid_Merah_PICTURE, (self.posisiX * window_width // columns, self.posisiY * window_height // rows))
        
class Droid_Hijau : 
    def __init__(self, x, y):
        self.posisiX = x
        self.posisiY = y
        self.Droid_Hijau_PICTURE = pygame.image.load('DroidH.png')

    def check_posisi_baris(self) :
        return self.posisiY
    def check_posisi_kolom(self) :
        return self.posisiX

def cek_tempat_kosong(self,arah_cek,x,y):

    def gambar_(self):
        window.blit(self.Droid_Hijau_PICTURE, (self.posisiX * window_width // columns, self.posisiY * window_height // rows))
        
def main():
    posisiStartX = 0
    posisiStartY = 0
#Membuat random wall
    for i in range(350) :
        wall_box_x = random.randint(0, columns - 1)
        wall_box_y = random.randint(0, rows - 1)
        wall_box = grid[wall_box_y][wall_box_x]
        wall_box.wall = True
    
#Membuat posisi Start Droid Merah
    for i in range(columns * rows):
        Droid_Merah_box_x = random.randint(0, columns - 1)
        Droid_Merah_box_y = random.randint(0, rows - 1)
        Droid_Merah_box = grid[Droid_Merah_box_y][Droid_Merah_box_x]
        if (grid[Droid_Merah_box_x][Droid_Merah_box_y].wall == False): 
            Droid_Merah_box.start = True
            DroidMerah = Droid_Merah(Droid_Merah_box_x, Droid_Merah_box_y)
            break

#Membuat posisi Start Droid Hijau
    for i in range(columns * rows):
        Droid_Hijau_box_x = random.randint(0, columns - 1)
        Droid_Hijau_box_y = random.randint(0, rows - 1)
        Droid_Hijau_box = grid[Droid_Hijau_box_y][Droid_Hijau_box_x]
        if (grid[Droid_Hijau_box_x][Droid_Hijau_box_y].wall == False): 
            Droid_Hijau_box.start = True
            DroidHijau = Droid_Hijau(Droid_Hijau_box_x, Droid_Hijau_box_y)
            break

    #MAIN PROGRAM ADA DI BAWAH INI
    start = 0
    while True:
        posisiBarisDroidMerah = DroidMerah.check_posisi_baris()
        posisiKolomDroidMerah = DroidMerah.check_posisi_kolom()
        posisiBarisDroidHijau = DroidHijau.check_posisi_baris()
        posisiKolomDroidHijau = DroidHijau.check_posisi_kolom()
        for event in pygame.event.get():
            #Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #setting RGB untuk wall
        window.fill ((0, 0, 0))

        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (20,20,20))
                if box.wall:
                    box.draw(window, (255, 255, 255))

       ###### CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######
        if(start == 0):
            if (grid[Droid_Merah_box_y][Droid_Merah_box_x].start == True):
                    window.blit(DroidMerah.Droid_Merah_PICTURE, (posisiKolomDroidMerah * window_width // columns, posisiBarisDroidMerah * window_height // rows))
        else :
            if (grid[Droid_Merah_box_y][Droid_Merah_box_x].start == True):
                grid[posisiStartY][posisiStartX].draw(window, (20,20,20))
        
        ###### CODE UNTUK POSISI START ADA GAMBAR LALU SETELAH SEARCH POSISI DIGANTI BOX JALAN #######
        if(start == 0):
            if (grid[Droid_Hijau_box_y][Droid_Hijau_box_x].start == True):
                    window.blit(DroidHijau.Droid_Hijau_PICTURE, (posisiKolomDroidHijau * window_width // columns, posisiBarisDroidHijau * window_height // rows))
        else :
            if (grid[Droid_Hijau_box_y][Droid_Hijau_box_x].start == True):
                grid[posisiStartY][posisiStartX].draw(window, (20,20,20))
        
        pygame.display.flip()
        
main()