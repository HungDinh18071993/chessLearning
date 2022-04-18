import pygame
import random
import math

class Chess :
    def __init__(self):
        pygame.init()
        self.xScreen, self.yScreen = 640, 640
        linkBackGround = './data_chess/board.png'
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen))  # Khởi tao kích thước màn hình
        pygame.display.set_caption("Code Learn - Chess")
        self.background = pygame.image.load(linkBackGround)
        self.king_white = pygame.image.load('./data_chess/king_white.png')
        self.queen_white = pygame.image.load('./data_chess/queen_white.png')
        self.bishop_white = pygame.image.load('./data_chess/bishop_white.png')
        self.knight_white = pygame.image.load('./data_chess/knight_white.png')
        self.rook_white = pygame.image.load('./data_chess/rook_white.png')
        self.pawn_white = pygame.image.load('./data_chess/pawn_white.png')
        self.king_black = pygame.image.load('./data_chess/king_black.png')
        self.queen_black = pygame.image.load('./data_chess/queen_black.png')
        self.bishop_black = pygame.image.load('./data_chess/bishop_black.png')
        self.knight_black = pygame.image.load('./data_chess/knight_black.png')
        self.rook_black = pygame.image.load('./data_chess/rook_black.png')
        self.pawn_black = pygame.image.load('./data_chess/pawn_black.png')

        self.green_box = pygame.image.load('./data_chess/green_box.png')
        self.yellow_box = pygame.image.load('./data_chess/yellow_box.png')

        self.gamerunning = True
        self.player = 0
        self.list_quan_co=[1,2,3,4,5,3,2,1,6,6,6,6,6,6,6,6,-1,-2,-3,-4,-5,-3,-2,-1,-6,-6,-6,-6,-6,-6,-6,-6]
        self.list_GT_quan_co=[50,30,30,90,900,30,30,50,10,10,10,10,10,10,10,10,-50,-30,-30,-90,-900,-30,-30,-50,-10,-10,-10,-10,-10,-10,-10,-10]
        self.list_toa_do=[[0,560],[80,560],[160,560],[240,560],[320,560],[400,560],[480,560],[560,560],[0,480],[80,480],[160,480],[240,480],[320,480],[400,480],[480,480],[560,480],[0,0],[80,0],[160,0],[240,0],[320,0],[400,0],[480,0],[560,0],[0,80],[80,80],[160,80],[240,80],[320,80],[400,80],[480,80],[560,80]]
        #--------------su kien click chuot-------------------------
        self.click = 0
        self.list_quan_co_duoc_chon=[]
        self.list_toa_do_cu = []
        self.list_toa_do_moi= []
        self.list_quan_bi_an=[]
        self.list_toa_do_quan_bi_an =[]
        self.list_green_box =[]
        self.kt_da_click =0
        self.chon_lai =False
        #-------------su kien undo-------------------------------
        self.so_lan_click = 1
        self.list_trang_thai =[]
        #------------positive------------------------------
        self.list_positive =[]
        self.VT_can = []
        self.list_quan_co_can = 0
        self.list_first_move =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # kiem tra lan di dau cua tot / vua
        self.so_buoc_dau_tot_vua = 0
        #----------- kiem tra nhap thanh
        self.kt_nhap_thanh_trang = False
        self.kt_nhap_thanh_den = False
        #-------------AI----------------
        self.depth = 1
        self.player_AI = True
        self.bestmove = 10000
        self.bestmove_tam =10000
        self.list_quan_AI =[]
        self.list_toa_do_AI = []
        self.tong_diem = 0
        self.x= 0
        #-----------cac bien tim loi-----------

    def kiemtra(self, list1, list2):
        for t in range(len(list1)):
            if list1[t] == list2:
                return True
        return False
    def undo(self):
        self.kt_da_click = 0
        self.list_green_box =[]
        self.so_lan_click -= 1
        #self.list_positive = []
        if  self.so_lan_click <0 : self.so_lan_click = 0
        if self.list_trang_thai[-1] == 1:
            self.list_toa_do[self.list_quan_bi_an[-1]] =  self.list_toa_do_quan_bi_an[-1]
            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] =  self.list_toa_do_cu[-1]
            self.list_toa_do_cu.pop(-1)
            self.list_toa_do_moi.pop(-1)
            self.list_quan_bi_an.pop(-1)
            self.list_quan_co_duoc_chon.pop(-1)
            self.list_toa_do_quan_bi_an.pop(-1)
            self.list_trang_thai.pop(-1)
            if (self.list_quan_co_duoc_chon[-1] == 4) or (self.list_quan_co_duoc_chon[-1] == 20) or (self.list_quan_co_duoc_chon[-1] == 0) or (self.list_quan_co_duoc_chon[-1] == 16) or (self.list_quan_co_duoc_chon[-1] == 7) or (self.list_quan_co_duoc_chon[-1] == 23) or (self.list_quan_co_duoc_chon[-1] in range(8, 16)) or (self.list_quan_co_duoc_chon[-1] in range(24, 32)):
                self.list_first_move[self.list_quan_co_duoc_chon[-1]] -= 1
        elif self.list_trang_thai[-1] == 0:
            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = self.list_toa_do_cu[-1]
            self.list_toa_do_cu.pop(-1)
            self.list_toa_do_moi.pop(-1)
            self.list_quan_co_duoc_chon.pop(-1)
            self.list_trang_thai.pop(-1)
            if (self.list_quan_co_duoc_chon[-1] == 4) or (self.list_quan_co_duoc_chon[-1] == 20) or (self.list_quan_co_duoc_chon[-1] == 0) or (self.list_quan_co_duoc_chon[-1] == 16) or (self.list_quan_co_duoc_chon[-1] == 7) or (self.list_quan_co_duoc_chon[-1] == 23) or (self.list_quan_co_duoc_chon[-1] in range(8, 16)) or (self.list_quan_co_duoc_chon[-1] in range(24, 32)):
                self.list_first_move[self.list_quan_co_duoc_chon[-1]] -= 1
        elif self.list_trang_thai[-1] == 2 or self.list_trang_thai[-1] == 3 or self.list_trang_thai[-1] == 4 or self.list_trang_thai[-1] == 5 :
            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = self.list_toa_do_cu[-1]
            self.list_toa_do_cu.pop(-1)
            self.list_toa_do_moi.pop(-1)
            self.list_quan_co_duoc_chon.pop(-1)
            if self.list_trang_thai[-1] == 2:
                self.list_toa_do[0][0] -=240
                self.list_first_move[0] -= 1
            if self.list_trang_thai[-1] == 3:
                self.list_toa_do[7][0] += 160
                self.list_first_move[7] -= 1
            if self.list_trang_thai[-1] == 4:
                self.list_toa_do[16][0] -= 240
                self.list_first_move[16] -= 1
            if self.list_trang_thai[-1] == 5:
                self.list_toa_do[23][0] += 160
                self.list_first_move[23] -= 1
            self.list_trang_thai.pop(-1)
            if (self.list_quan_co_duoc_chon[-1] == 4) or (self.list_quan_co_duoc_chon[-1] == 20) or (self.list_quan_co_duoc_chon[-1] == 0) or (self.list_quan_co_duoc_chon[-1] == 16) or (self.list_quan_co_duoc_chon[-1] == 7) or (self.list_quan_co_duoc_chon[-1] == 23) or (self.list_quan_co_duoc_chon[-1] in range(8, 16)) or (self.list_quan_co_duoc_chon[-1] in range(24, 32)):
                self.list_first_move[self.list_quan_co_duoc_chon[-1]] -= 1

    def positive(self):
        # QUAN XE
        if self.list_quan_co_duoc_chon[-1] == 0 or self.list_quan_co_duoc_chon[-1]==7 or self.list_quan_co_duoc_chon[-1]==16 or self.list_quan_co_duoc_chon[-1]==23 :
           #---------------sang phai
           i=1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i<=8 and self.VT_can ==[]) :
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1]]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1]]
                   if self.list_quan_co_duoc_chon[-1] == 0 or self.list_quan_co_duoc_chon[-1]==7 :
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1]]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1]]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 16 or self.list_quan_co_duoc_chon[-1]==23 :
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1]]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1]]) < 16:
                           self.list_quan_co_can = 1

               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i> 1:
               if self.list_quan_co_can == 1 :
                    for j in range(1,i):
                        self.list_positive.append([self.list_toa_do_cu[-1][0]+ j*80, self.list_toa_do_cu[-1][1]])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i-1):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] + j * 80, self.list_toa_do_cu[-1][1]])
               # ---------------len tren
           i = 1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i <= 8 and self.VT_can == []):
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1] - i * 80]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1] - i * 80]
                   if self.list_quan_co_duoc_chon[-1] == 0 or self.list_quan_co_duoc_chon[-1] == 7:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1]- i * 80]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 16 or self.list_quan_co_duoc_chon[-1] == 23:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1]- i * 80]) < 16:
                           self.list_quan_co_can = 1
               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i > 1:
               if self.list_quan_co_can == 1:
                   for j in range(1, i):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1]- j * 80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i-1 ):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1]- j * 80])
               # ---------------xuong duoi
           i = 1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i <= 8 and self.VT_can == []):
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]
                   if self.list_quan_co_duoc_chon[-1] == 0 or self.list_quan_co_duoc_chon[-1] == 7:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 16 or self.list_quan_co_duoc_chon[-1] == 23:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) < 16:
                           self.list_quan_co_can = 1
               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i > 1:
               if self.list_quan_co_can == 1:
                   for j in range(1, i):
                       self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + j * 80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i - 1):
                       self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + j * 80])
               # ---------------sang trai
               i = 1
               self.VT_can = []
               self.list_quan_co_can = 2

               while (i <= 8 and self.VT_can == []):
                   if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) == True:
                       self.VT_can = [self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]
                       if self.list_quan_co_duoc_chon[-1] == 0 or self.list_quan_co_duoc_chon[-1] == 7:
                           if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) >= 16:
                               self.list_quan_co_can = 1
                           elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) < 16:
                               self.list_quan_co_can = 0
                       elif self.list_quan_co_duoc_chon[-1] == 16 or self.list_quan_co_duoc_chon[-1] == 23:
                           if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) >= 16:
                               self.list_quan_co_can = 0
                           elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) < 16:
                               self.list_quan_co_can = 1

                   i += 1
               if self.VT_can == []:  self.list_quan_co_can = 0
               if i > 1:
                   if self.list_quan_co_can == 1:
                       for j in range(1, i):
                           self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1]])
                   elif self.list_quan_co_can == 0:
                       for j in range(1, i - 1):
                           self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1]])


   ##################################################################################################################################
         # QUAN TOT
        if self.list_quan_co_duoc_chon[-1] in range(8, 16) or self.list_quan_co_duoc_chon[-1] in range(24, 32):
            if self.list_quan_co_duoc_chon[-1] in range(8, 16) :
                # --------- di thang
                i = 1
                self.VT_can = []
                if self.list_first_move[self.list_quan_co_duoc_chon[-1]] == 0:
                    self.so_buoc_dau_tot_vua = 2
                elif self.list_first_move[self.list_quan_co_duoc_chon[-1]] >= 1:
                    self.so_buoc_dau_tot_vua = 1
                while (i <= self.so_buoc_dau_tot_vua and self.VT_can == []):
                    if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - i * 80]) == True:
                        self.VT_can = [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - i * 80]
                    i += 1
                if i > 1:
                    for j in range(1, i ):
                        if self.VT_can != [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - j * 80]:
                            self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - j * 80])
                # --------- an cheo
                if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80]) >= 16:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80])
                if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80]) >= 16:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80])
            if self.list_quan_co_duoc_chon[-1] in range(24, 32) :
                # --------- di thang
                i = 1
                self.VT_can = []
                if self.list_first_move[self.list_quan_co_duoc_chon[-1]] == 0:
                    self.so_buoc_dau_tot_vua = 2
                elif self.list_first_move[self.list_quan_co_duoc_chon[-1]] >= 1:
                    self.so_buoc_dau_tot_vua = 1
                while (i <= self.so_buoc_dau_tot_vua and self.VT_can == []):
                    if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) == True:
                        self.VT_can = [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]
                    i += 1
                if i > 1:
                    for j in range(1, i):
                        if self.VT_can != [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + j * 80]:
                            self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + j * 80])
                # --------- an cheo
                if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] + 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] + 80]) < 16:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] + 80])
                if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] + 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] + 80]) < 16:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] + 80])
    ##############################################################################################################
        # QUAN MA
        if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1]==6 or self.list_quan_co_duoc_chon[-1]==17 or self.list_quan_co_duoc_chon[-1]==22 :
           #--------------- huong 1h
           self.list_quan_co_can = 2
           if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]-160]) == True:
               if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1] == 6:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]-160]) >= 16:
                       self.list_quan_co_can = 1
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]-160]) < 16:
                       self.list_quan_co_can = 0
               elif self.list_quan_co_duoc_chon[-1] == 17 or self.list_quan_co_duoc_chon[-1] == 22:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]-160]) >= 16:
                       self.list_quan_co_can = 0
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]-160]) < 16:
                       self.list_quan_co_can = 1
           if self.list_quan_co_can == 1 : self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 160])
           elif self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 160]) == False:
               self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 160])
           #--------------- huong 2h
           self.list_quan_co_can = 2
           if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]-80]) == True:
               if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1] == 6:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]-80]) >= 16:
                       self.list_quan_co_can = 1
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]-80]) < 16:
                       self.list_quan_co_can = 0
               elif self.list_quan_co_duoc_chon[-1] == 17 or self.list_quan_co_duoc_chon[-1] == 22:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]-80]) >= 16:
                       self.list_quan_co_can = 0
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]-80]) < 16:
                       self.list_quan_co_can = 1
           if self.list_quan_co_can == 1 : self.list_positive.append([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]-80])
           elif self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]-80]) == False:
               self.list_positive.append([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]-80])
           #--------------- huong 4h
           self.list_quan_co_can = 2
           if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]+80]) == True:
               if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1] == 6:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]+80]) >= 16:
                       self.list_quan_co_can = 1
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]+80]) < 16:
                       self.list_quan_co_can = 0
               elif self.list_quan_co_duoc_chon[-1] == 17 or self.list_quan_co_duoc_chon[-1] == 22:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]+80]) >= 16:
                       self.list_quan_co_can = 0
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]+80]) < 16:
                       self.list_quan_co_can = 1
           if self.list_quan_co_can == 1 : self.list_positive.append([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]+80])
           elif self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]+80]) == False:
               self.list_positive.append([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]+80])
           #--------------- huong 5h
           self.list_quan_co_can = 2
           if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+160]) == True:
               if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1] == 6:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+160]) >= 16:
                       self.list_quan_co_can = 1
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+160]) < 16:
                       self.list_quan_co_can = 0
               elif self.list_quan_co_duoc_chon[-1] == 17 or self.list_quan_co_duoc_chon[-1] == 22:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+160]) >= 16:
                       self.list_quan_co_can = 0
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+160]) < 16:
                       self.list_quan_co_can = 1
           if self.list_quan_co_can == 1 : self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+160])
           elif self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+160]) == False:
               self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+160])
           #--------------- huong 7h
           self.list_quan_co_can = 2
           if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+160]) == True:
               if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1] == 6:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+160]) >= 16:
                       self.list_quan_co_can = 1
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+160]) < 16:
                       self.list_quan_co_can = 0
               elif self.list_quan_co_duoc_chon[-1] == 17 or self.list_quan_co_duoc_chon[-1] == 22:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+160]) >= 16:
                       self.list_quan_co_can = 0
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+160]) < 16:
                       self.list_quan_co_can = 1
           if self.list_quan_co_can == 1 : self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+160])
           elif self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+160]) == False:
               self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+160])
           #--------------- huong 8h
           self.list_quan_co_can = 2
           if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]+80]) == True:
               if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1] == 6:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]+80]) >= 16:
                       self.list_quan_co_can = 1
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]+80]) < 16:
                       self.list_quan_co_can = 0
               elif self.list_quan_co_duoc_chon[-1] == 17 or self.list_quan_co_duoc_chon[-1] == 22:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]+80]) >= 16:
                       self.list_quan_co_can = 0
                   elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]+80]) < 16:
                       self.list_quan_co_can = 1
           if self.list_quan_co_can == 1 : self.list_positive.append([self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]+80])
           elif self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]+80]) == False:
               self.list_positive.append([self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]+80])
           #--------------- huong 10h
           self.list_quan_co_can = 2
           if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]-80]) == True:
               if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1] == 6:
                   if self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]-80]) >= 16:
                       self.list_quan_co_can = 1
                   elif self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]-80]) < 16:
                       self.list_quan_co_can = 0
               elif self.list_quan_co_duoc_chon[-1] == 17 or self.list_quan_co_duoc_chon[-1] == 22:
                   if self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]-80]) >= 16:
                       self.list_quan_co_can = 0
                   elif self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]-80]) < 16:
                       self.list_quan_co_can = 1
           if self.list_quan_co_can == 1 : self.list_positive.append( [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]-80])
           elif self.kiemtra(self.list_toa_do,  [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]-80]) == False:
               self.list_positive.append( [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]-80])
           #--------------- huong 11h
           self.list_quan_co_can = 2
           if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]-160]) == True:
               if self.list_quan_co_duoc_chon[-1] == 1 or self.list_quan_co_duoc_chon[-1] == 6:
                   if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]-160]) >= 16:
                       self.list_quan_co_can = 1
                   elif self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]-160]) < 16:
                       self.list_quan_co_can = 0
               elif self.list_quan_co_duoc_chon[-1] == 17 or self.list_quan_co_duoc_chon[-1] == 22:
                   if self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]-160]) >= 16:
                       self.list_quan_co_can = 0
                   elif self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]-160]) < 16:
                       self.list_quan_co_can = 1
           if self.list_quan_co_can == 1 : self.list_positive.append( [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]-160])
           elif self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]-160]) == False:
               self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]-160])
    #####################################################################################################################################
        # QUAN TUONG
        if self.list_quan_co_duoc_chon[-1] == 2 or self.list_quan_co_duoc_chon[-1]==5 or self.list_quan_co_duoc_chon[-1]==18 or self.list_quan_co_duoc_chon[-1]==21 :
           #---------------sang phai/ xuong duoi
           i=1
           self.VT_can = []
           self.list_quan_co_can = 2
           while (i<=8 and self.VT_can ==[]) :
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]
                   if self.list_quan_co_duoc_chon[-1] == 2 or self.list_quan_co_duoc_chon[-1]==5 :
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 18 or self.list_quan_co_duoc_chon[-1]==21 :
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) < 16:
                           self.list_quan_co_can = 1

               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i> 1:
               if self.list_quan_co_can == 1 :
                    for j in range(1,i):
                        self.list_positive.append([self.list_toa_do_cu[-1][0]+ j*80, self.list_toa_do_cu[-1][1] + j*80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i-1):
                       self.list_positive.append([self.list_toa_do_cu[-1][0]+ j*80, self.list_toa_do_cu[-1][1] + j*80])
               # ---------------sang trai /len tren
           i = 1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i <= 8 and self.VT_can == []):
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) == True:
                   self.VT_can =  [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]
                   if self.list_quan_co_duoc_chon[-1] == 2 or self.list_quan_co_duoc_chon[-1] == 5:
                       if self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 18 or self.list_quan_co_duoc_chon[-1] == 21:
                       if self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 1
               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i > 1:
               if self.list_quan_co_can == 1:
                   for j in range(1, i):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80 , self.list_toa_do_cu[-1][1]- j * 80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i-1 ):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1]- j * 80])
               # ---------------sang phai / len tren
           i = 1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i <= 8 and self.VT_can == []):
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]
                   if self.list_quan_co_duoc_chon[-1] == 2 or self.list_quan_co_duoc_chon[-1] == 5:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 18 or self.list_quan_co_duoc_chon[-1] == 21:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 1
               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i > 1:
               if self.list_quan_co_can == 1:
                   for j in range(1, i):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] + j * 80, self.list_toa_do_cu[-1][1] - j * 80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i - 1):
                       self.list_positive.append([self.list_toa_do_cu[-1][0]+ j * 80, self.list_toa_do_cu[-1][1] - j * 80])

               # ---------------sang trai/ xuong duoi
               i = 1
               self.VT_can = []
               self.list_quan_co_can = 2

               while (i <= 8 and self.VT_can == []):
                   if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) == True:
                       self.VT_can = [self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]
                       if self.list_quan_co_duoc_chon[-1] == 2 or self.list_quan_co_duoc_chon[-1] == 5:
                           if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) >= 16:
                               self.list_quan_co_can = 1
                           elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) < 16:
                               self.list_quan_co_can = 0
                       elif self.list_quan_co_duoc_chon[-1] == 18 or self.list_quan_co_duoc_chon[-1] == 21:
                           if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) >= 16:
                               self.list_quan_co_can = 0
                           elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) < 16:
                               self.list_quan_co_can = 1

                   i += 1
               if self.VT_can == []:  self.list_quan_co_can = 0
               if i > 1:
                   if self.list_quan_co_can == 1:
                       for j in range(1, i):
                           self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1] + j * 80] )
                   elif self.list_quan_co_can == 0:
                       for j in range(1, i - 1):
                           self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1]+ j * 80])
    ######################################################################################################################################
        # QUAN HAU
        if self.list_quan_co_duoc_chon[-1] == 3 or self.list_quan_co_duoc_chon[-1]== 19:
           #---------------sang phai/ xuong duoi
           i=1
           self.VT_can = []
           self.list_quan_co_can = 2
           while (i<=8 and self.VT_can ==[]) :
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]
                   if self.list_quan_co_duoc_chon[-1] == 3 :
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 19 :
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1] + i*80 ]) < 16:
                           self.list_quan_co_can = 1

               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i> 1:
               if self.list_quan_co_can == 1 :
                    for j in range(1,i):
                        self.list_positive.append([self.list_toa_do_cu[-1][0]+ j*80, self.list_toa_do_cu[-1][1] + j*80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i-1):
                       self.list_positive.append([self.list_toa_do_cu[-1][0]+ j*80, self.list_toa_do_cu[-1][1] + j*80])
               # ---------------sang trai /len tren
           i = 1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i <= 8 and self.VT_can == []):
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) == True:
                   self.VT_can =  [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]
                   if self.list_quan_co_duoc_chon[-1] == 3:
                       if self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 19:
                       if self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index( [self.list_toa_do_cu[-1][0] - i * 80 , self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 1
               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i > 1:
               if self.list_quan_co_can == 1:
                   for j in range(1, i):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80 , self.list_toa_do_cu[-1][1]- j * 80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i-1 ):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1]- j * 80])
               # ---------------sang phai / len tren
           i = 1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i <= 8 and self.VT_can == []):
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]
                   if self.list_quan_co_duoc_chon[-1] == 3:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 19:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 1
               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i > 1:
               if self.list_quan_co_can == 1:
                   for j in range(1, i):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] + j * 80, self.list_toa_do_cu[-1][1] - j * 80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i - 1):
                       self.list_positive.append([self.list_toa_do_cu[-1][0]+ j * 80, self.list_toa_do_cu[-1][1] - j * 80])

               # ---------------sang trai/ xuong duoi
               i = 1
               self.VT_can = []
               self.list_quan_co_can = 2

               while (i <= 8 and self.VT_can == []):
                   if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) == True:
                       self.VT_can = [self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]
                       if self.list_quan_co_duoc_chon[-1] == 3:
                           if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) >= 16:
                               self.list_quan_co_can = 1
                           elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) < 16:
                               self.list_quan_co_can = 0
                       elif self.list_quan_co_duoc_chon[-1] == 19:
                           if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) >= 16:
                               self.list_quan_co_can = 0
                           elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]+ i * 80]) < 16:
                               self.list_quan_co_can = 1

                   i += 1
               if self.VT_can == []:  self.list_quan_co_can = 0
               if i > 1:
                   if self.list_quan_co_can == 1:
                       for j in range(1, i):
                           self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1] + j * 80] )
                   elif self.list_quan_co_can == 0:
                       for j in range(1, i - 1):
                           self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1]+ j * 80])
           #---------------sang phai
           i=1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i<=8 and self.VT_can ==[]) :
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1]]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0]+ i*80, self.list_toa_do_cu[-1][1]]
                   if self.list_quan_co_duoc_chon[-1] == 3:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1]]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1]]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 19 :
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1]]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] + i * 80, self.list_toa_do_cu[-1][1]]) < 16:
                           self.list_quan_co_can = 1

               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i> 1:
               if self.list_quan_co_can == 1 :
                    for j in range(1,i):
                        self.list_positive.append([self.list_toa_do_cu[-1][0]+ j*80, self.list_toa_do_cu[-1][1]])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i-1):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] + j * 80, self.list_toa_do_cu[-1][1]])
               # ---------------len tren
           i = 1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i <= 8 and self.VT_can == []):
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1] - i * 80]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1] - i * 80]
                   if self.list_quan_co_duoc_chon[-1] == 3:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1]- i * 80]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1] - i * 80]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 19:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1] - i * 80]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1]- i * 80]) < 16:
                           self.list_quan_co_can = 1
               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i > 1:
               if self.list_quan_co_can == 1:
                   for j in range(1, i):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1]- j * 80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i-1 ):
                       self.list_positive.append([self.list_toa_do_cu[-1][0] , self.list_toa_do_cu[-1][1]- j * 80])
               # ---------------xuong duoi
           i = 1
           self.VT_can = []
           self.list_quan_co_can = 2

           while (i <= 8 and self.VT_can == []):
               if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) == True:
                   self.VT_can = [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]
                   if self.list_quan_co_duoc_chon[-1] == 3:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) >= 16:
                           self.list_quan_co_can = 1
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) < 16:
                           self.list_quan_co_can = 0
                   elif self.list_quan_co_duoc_chon[-1] == 19:
                       if self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) >= 16:
                           self.list_quan_co_can = 0
                       elif self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + i * 80]) < 16:
                           self.list_quan_co_can = 1
               i += 1
           if self.VT_can == []:  self.list_quan_co_can = 0
           if i > 1:
               if self.list_quan_co_can == 1:
                   for j in range(1, i):
                       self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + j * 80])
               elif self.list_quan_co_can == 0:
                   for j in range(1, i - 1):
                       self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + j * 80])
               # ---------------sang trai
               i = 1
               self.VT_can = []
               self.list_quan_co_can = 2

               while (i <= 8 and self.VT_can == []):
                   if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) == True:
                       self.VT_can = [self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]
                       if self.list_quan_co_duoc_chon[-1] == 3:
                           if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) >= 16:
                               self.list_quan_co_can = 1
                           elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) < 16:
                               self.list_quan_co_can = 0
                       elif self.list_quan_co_duoc_chon[-1] == 19:
                           if self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) >= 16:
                               self.list_quan_co_can = 0
                           elif self.list_toa_do.index([self.list_toa_do_cu[-1][0] - i * 80, self.list_toa_do_cu[-1][1]]) < 16:
                               self.list_quan_co_can = 1

                   i += 1
               if self.VT_can == []:  self.list_quan_co_can = 0
               if i > 1:
                   if self.list_quan_co_can == 1:
                       for j in range(1, i):
                           self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1]])
                   elif self.list_quan_co_can == 0:
                       for j in range(1, i - 1):
                           self.list_positive.append([self.list_toa_do_cu[-1][0] - j * 80, self.list_toa_do_cu[-1][1]])
    ######################################################################################################################################
           # Quan Vua
        if self.list_quan_co_duoc_chon[-1] == 4 or self.list_quan_co_duoc_chon[-1] == 20:
            if self.list_first_move[self.list_quan_co_duoc_chon[-1]] == 0:
                self.so_buoc_dau_tot_vua = 2
            # --------- an cheo
            if self.list_quan_co_duoc_chon[-1] == 4:
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80]) >= 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80]) >= 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - 80]) >= 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - 80])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0]- 80, self.list_toa_do_cu[-1][1] ]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0]- 80, self.list_toa_do_cu[-1][1] ]) >= 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0]- 80, self.list_toa_do_cu[-1][1] ]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0]- 80, self.list_toa_do_cu[-1][1] ])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]]) >= 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+ 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+ 80]) >= 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+ 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+ 80])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+ 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+ 80]) >= 16) or self.kiemtra(self.list_toa_do,[self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+ 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+ 80])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + 80 ]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + 80 ]) >= 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + 80 ]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + 80 ])
                if self.so_buoc_dau_tot_vua == 2 :
                    if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]]) == False and self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]]) == False and self.list_first_move[7] == 0 and  self.list_first_move[4]==0:
                        self.list_positive.append([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]])
                    if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]]) == False and self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]]) == False and self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 240, self.list_toa_do_cu[-1][1]]) == False and self.list_first_move[0] == 0 and self.list_first_move[4] == 0:
                        self.list_positive.append([self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]])
            if self.list_quan_co_duoc_chon[-1] == 20:
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80]) < 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1] - 80])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80]) < 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1] - 80])
                if( self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - 80]) < 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] - 80])
                if( self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0]- 80, self.list_toa_do_cu[-1][1] ]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0]- 80, self.list_toa_do_cu[-1][1] ]) < 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0]- 80, self.list_toa_do_cu[-1][1] ]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0]- 80, self.list_toa_do_cu[-1][1] ])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]]) < 16) or self.kiemtra(self.list_toa_do,[self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+ 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+ 80]) < 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+ 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]+ 80])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+ 80]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+ 80]) < 16) or self.kiemtra(self.list_toa_do,[self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+ 80]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]+ 80])
                if (self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + 80 ]) == True and self.list_toa_do.index([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + 80 ]) < 16) or self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + 80 ]) == False:
                    self.list_positive.append([self.list_toa_do_cu[-1][0], self.list_toa_do_cu[-1][1] + 80 ])
                if self.so_buoc_dau_tot_vua == 2 :
                    if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 80, self.list_toa_do_cu[-1][1]]) == False and self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]]) == False and self.list_first_move[23] == 0 and  self.list_first_move[20]==0:
                        self.list_positive.append([self.list_toa_do_cu[-1][0] + 160, self.list_toa_do_cu[-1][1]])
                    if self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 80, self.list_toa_do_cu[-1][1]]) == False and self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]]) == False and self.kiemtra(self.list_toa_do, [self.list_toa_do_cu[-1][0] - 240, self.list_toa_do_cu[-1][1]]) == False and self.list_first_move[16] == 0 and self.list_first_move[20] == 0:
                        self.list_positive.append([self.list_toa_do_cu[-1][0] - 160, self.list_toa_do_cu[-1][1]])
################################################################################################################################################
########################################### AI AI AI ########## AI AI AI ################ AI AI AI #############################################
    #-----------------------------tinh diem----------------
    def cost_move (self):
        self.tong_diem = 0
        for d in range(len(self.list_toa_do)):
            if self.list_toa_do[d] ==[1000,1000]:
                continue
            else :
                self.tong_diem = self.tong_diem + self.list_GT_quan_co[d]
    #----------------------------mo phong 2
    def mo_phong_2(self,depth,player_AI):
        if depth ==0 :
            self.cost_move()
            return self.tong_diem
        if player_AI == True :
            self.bestmove_5 = -10000

            for w in range(0, 16):
                if self.list_toa_do[w][0] > 640: continue
                self.list_quan_co_duoc_chon.append(w)
                self.list_toa_do_cu.append(self.list_toa_do[w])
                # ------------xoa positive
                self.list_positive = []
                self.positive()
                self.list_quan_co_duoc_chon.pop(-1)
                self.list_toa_do_cu.pop(-1)
                self.list_positive_5 = []
                for z in range(len(self.list_positive)):
                    if self.list_positive[z][0] < 640 and self.list_positive[z][0] >= 0 and self.list_positive[z][1] >= 0 and self.list_positive[z][1] < 640:
                        self.list_positive_5.append(self.list_positive[z])
                if  self.list_positive_5 !=[] :
                    for y in range(len( self.list_positive_5)):
                        self.list_quan_co_duoc_chon.append(w)
                        self.list_toa_do_cu.append(self.list_toa_do[w])
                        if self.kiemtra(self.list_toa_do,  self.list_positive_5[y]) == True:
                            self.list_toa_do_quan_bi_an.append( self.list_positive_5[y])
                            self.list_quan_bi_an.append(self.list_toa_do.index( self.list_positive_5[y]))
                            # ------------undo
                            self.so_lan_click += 1
                            # ------------kt quan bi an
                            self.list_trang_thai.append(1)
                            # ------------xu ly bi an
                            self.list_toa_do_moi.append( self.list_positive_5[y])
                            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] =  self.list_positive_5[y]
                            self.list_toa_do[self.list_quan_bi_an[-1]] = [1000, 1000]
                            # ------------- kiem tra lan di dau cua tot
                            if (w == 4) or (w == 20) or (w == 0) or (w == 16) or (w == 7) or (w == 23) or (w in range (8,16)) or (w in range(24,32)) :
                                self.list_first_move[w] += 1

                        elif self.kiemtra(self.list_toa_do,  self.list_positive_5[y]) == False:
                            self.list_toa_do_moi.append( self.list_positive_5[y])
                            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] =  self.list_positive_5[y]
                            # ------------undo
                            self.so_lan_click += 1
                            # ------------kt quan bi an
                            self.list_trang_thai.append(0)
                            # ------------- kiem tra lan di dau cua tot
                            # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                            if (w == 4) or (w == 20) or (w == 0) or (w == 16) or (w == 7) or (w == 23) or (w in range(8, 16)) or (w in range(24, 32)):
                                self.list_first_move[w] += 1
                            # ------------- kiem tra nhap thanh
                            if self.list_quan_co_duoc_chon[-1] == 4:
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                    self.list_trang_thai[-1] = 2
                                    self.list_toa_do[0][0] += 240
                                    self.list_first_move[0] += 1
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                    self.list_trang_thai[-1] = 3
                                    self.list_toa_do[7][0] -= 160
                                    self.list_first_move[7] += 1
                            if self.list_quan_co_duoc_chon[-1] == 20:
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                    self.list_trang_thai[-1] = 4
                                    self.list_toa_do[16][0] += 240
                                    self.list_first_move[16] += 1
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                    self.list_trang_thai[-1] = 5
                                    self.list_toa_do[23][0] -= 160
                                    self.list_first_move[23] += 1
                        # ------------tinh diem
                        self.bestmove_5 = max(self.bestmove_5, self.mo_phong(depth - 1, False))
                        # ------------undo
                        self.undo()
            return self.bestmove_5
    #----------------------------mo phong------------------
    def mo_phong(self,depth,player_AI):
        if depth ==0 :
            self.cost_move()
            return self.tong_diem
        if player_AI == True :
            self.bestmove_2 = -10000

            for a in range(0, 16):
                if self.list_toa_do[a][0] > 640: continue
                self.list_quan_co_duoc_chon.append(a)
                self.list_toa_do_cu.append(self.list_toa_do[a])
                # ------------xoa positive
                self.list_positive = []
                self.positive()
                self.list_quan_co_duoc_chon.pop(-1)
                self.list_toa_do_cu.pop(-1)
                self.list_positive_3 = []
                for b in range(len(self.list_positive)):
                    if self.list_positive[b][0] < 640 and self.list_positive[b][0] >= 0 and self.list_positive[b][1] >= 0 and self.list_positive[b][1] < 640:
                        self.list_positive_3.append(self.list_positive[b])
                if  self.list_positive_3 !=[] :
                    for c in range(len( self.list_positive_3)):
                        self.list_quan_co_duoc_chon.append(a)
                        self.list_toa_do_cu.append(self.list_toa_do[a])
                        if self.kiemtra(self.list_toa_do,  self.list_positive_3[c]) == True:
                            self.list_toa_do_quan_bi_an.append( self.list_positive_3[c])
                            self.list_quan_bi_an.append(self.list_toa_do.index( self.list_positive_3[c]))
                            # ------------undo
                            self.so_lan_click += 1
                            # ------------kt quan bi an
                            self.list_trang_thai.append(1)
                            # ------------xu ly bi an
                            self.list_toa_do_moi.append( self.list_positive_3[c])
                            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] =  self.list_positive_3[c]
                            self.list_toa_do[self.list_quan_bi_an[-1]] = [1000, 1000]
                            # ------------- kiem tra lan di dau cua tot
                            # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                            if (a == 4) or (a == 20) or (a == 0) or (a == 16) or (a == 7) or (a == 23) or (a in range(8, 16)) or (a in range(24, 32)):
                                self.list_first_move[a] += 1
                        elif self.kiemtra(self.list_toa_do,  self.list_positive_3[c]) == False:
                            self.list_toa_do_moi.append( self.list_positive_3[c])
                            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] =  self.list_positive_3[c]
                            # ------------undo
                            self.so_lan_click += 1
                            # ------------kt quan bi an
                            self.list_trang_thai.append(0)
                            # ------------- kiem tra lan di dau cua tot
                            # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                            if (a == 4) or (a == 20) or (a == 0) or (a == 16) or (a == 7) or (a == 23) or (a in range(8, 16)) or (a in range(24, 32)):
                                self.list_first_move[a] += 1
                            # ------------- kiem tra nhap thanh
                            if self.list_quan_co_duoc_chon[-1] == 4:
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                    self.list_trang_thai[-1] = 2
                                    self.list_toa_do[0][0] += 240
                                    self.list_first_move[0] += 1
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                    self.list_trang_thai[-1] = 3
                                    self.list_toa_do[7][0] -= 160
                                    self.list_first_move[7] += 1
                            if self.list_quan_co_duoc_chon[-1] == 20:
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                    self.list_trang_thai[-1] = 4
                                    self.list_toa_do[16][0] += 240
                                    self.list_first_move[16] += 1
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                    self.list_trang_thai[-1] = 5
                                    self.list_toa_do[23][0] -= 160
                                    self.list_first_move[23] += 1
                        # ------------tinh diem
                        self.bestmove_2 = max(self.bestmove_2, self.mo_phong(depth - 1, False))
                        # ------------undo
                        self.undo()
            return self.bestmove_2
        elif player_AI == False :
            self.bestmove_3 = 10000

            for p in range(16, 32):
                if self.list_toa_do[p][0] > 640: continue
                self.list_quan_co_duoc_chon.append(p)
                self.list_toa_do_cu.append(self.list_toa_do[p])
                # ------------xoa positive
                self.list_positive = []
                self.positive()
                self.list_quan_co_duoc_chon.pop(-1)
                self.list_toa_do_cu.pop(-1)
                self.list_positive_4 = []
                for q in range(len(self.list_positive)):
                    if self.list_positive[q][0] < 640 and self.list_positive[q][0] >= 0 and self.list_positive[q][1] >= 0 and self.list_positive[q][1] < 640:
                        self.list_positive_4.append(self.list_positive[q])

                if self.list_positive_4 !=[] :
                    for k in range(len(self.list_positive_4)):
                        self.list_quan_co_duoc_chon.append(p)
                        self.list_toa_do_cu.append(self.list_toa_do[p])
                        if self.kiemtra(self.list_toa_do, self.list_positive_4[k]) == True:
                            self.list_toa_do_quan_bi_an.append(self.list_positive_4[k])
                            self.list_quan_bi_an.append(self.list_toa_do.index(self.list_positive_4[k]))
                            # ------------undo
                            self.so_lan_click += 1
                            # ------------kt quan bi an
                            self.list_trang_thai.append(1)
                            # ------------xu ly bi an
                            self.list_toa_do_moi.append(self.list_positive_4[k])
                            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = self.list_positive_4[k]
                            self.list_toa_do[self.list_quan_bi_an[-1]] = [1000, 1000]
                            # ------------- kiem tra lan di dau cua tot
                            # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                            if (p == 4) or (p == 20) or (p == 0) or (p == 16) or (p == 7) or (p == 23) or (p in range(8, 16)) or (p in range(24, 32)):
                                self.list_first_move[p] += 1
                        elif self.kiemtra(self.list_toa_do, self.list_positive_4[k]) == False:
                            self.list_toa_do_moi.append(self.list_positive_4[k])
                            self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = self.list_positive_4[k]
                            # ------------undo
                            self.so_lan_click += 1
                            # ------------kt quan bi an
                            self.list_trang_thai.append(0)
                            # ------------- kiem tra lan di dau cua tot
                            # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                            if (p == 4) or (p == 20) or (p == 0) or (p == 16) or (p == 7) or (p == 23) or (p in range(8, 16)) or (p in range(24, 32)):
                                self.list_first_move[p] += 1
                            # ------------- kiem tra nhap thanh
                            if self.list_quan_co_duoc_chon[-1] == 4:
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                    self.list_trang_thai[-1] = 2
                                    self.list_toa_do[0][0] += 240
                                    self.list_first_move[0] += 1
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                    self.list_trang_thai[-1] = 3
                                    self.list_toa_do[7][0] -= 160
                                    self.list_first_move[7] += 1
                            if self.list_quan_co_duoc_chon[-1] == 20:
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                    self.list_trang_thai[-1] = 4
                                    self.list_toa_do[16][0] += 240
                                    self.list_first_move[16] += 1
                                if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                    self.list_trang_thai[-1] = 5
                                    self.list_toa_do[23][0] -= 160
                                    self.list_first_move[23] += 1
                        # ------------tinh diem
                        self.bestmove_3 = min(self.bestmove_3, self.mo_phong_2(depth - 1, True))
                        # ------------undo
                        self.undo()

            return self.bestmove_3


    #-----------------------------AI------------------------
    def AI(self):
        self.depth = 3
        self.player_AI = True
        self.bestmove = 10000
        self.bestmove_tam = 10000
        self.list_quan_AI = []
        self.list_toa_do_AI = []

        for m in range (16,32):
            if self.list_toa_do[m][0] > 640 : continue
            self.list_quan_co_duoc_chon.append(m)
            self.list_toa_do_cu.append(self.list_toa_do[m])
            # ------------xoa positive
            self.list_positive = []
            self.positive()
            self.list_quan_co_duoc_chon.pop(-1)
            self.list_toa_do_cu.pop(-1)
            self.list_positive_2 = []
            for h in range( len(self.list_positive)):
                if self.list_positive[h][0] < 640 and  self.list_positive[h][0] >= 0 and  self.list_positive[h][1] >= 0 and  self.list_positive[h][1] < 640 :
                    self.list_positive_2.append(self.list_positive[h])
            if self.list_positive_2 != []:
                for n in range(len(self.list_positive_2)):
                    self.list_quan_co_duoc_chon.append(m)
                    self.list_toa_do_cu.append(self.list_toa_do[m])
                    if self.kiemtra(self.list_toa_do, self.list_positive_2[n]) == True:
                        self.list_toa_do_quan_bi_an.append(self.list_positive_2[n])
                        self.list_quan_bi_an.append(self.list_toa_do.index(self.list_positive_2[n]))
                        # ------------undo
                        self.so_lan_click += 1
                        # ------------kt quan bi an
                        self.list_trang_thai.append(1)
                        # ------------xu ly bi an
                        self.list_toa_do_moi.append(self.list_positive_2[n])
                        self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = self.list_positive_2[n]
                        self.list_toa_do[self.list_quan_bi_an[-1]] = [1000, 1000]
                        # ------------- kiem tra lan di dau cua tot
                        # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                        if (m == 4) or (m == 20) or (m == 0) or (m == 16) or (m == 7) or (m == 23) or (m in range(8, 16)) or (m in range(24, 32)):
                            self.list_first_move[m] += 1
                    elif self.kiemtra(self.list_toa_do, self.list_positive_2[n]) == False:
                        self.list_toa_do_moi.append(self.list_positive_2[n])
                        self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = self.list_positive_2[n]
                        # ------------undo
                        self.so_lan_click += 1
                        # ------------kt quan bi an
                        self.list_trang_thai.append(0)
                        # ------------- kiem tra lan di dau cua tot
                        # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                        if (m == 4) or (m == 20) or (m == 0) or (m == 16) or (m == 7) or (m == 23) or (m in range(8, 16)) or (m in range(24, 32)):
                            self.list_first_move[m] += 1
                        # ------------- kiem tra nhap thanh
                        if self.list_quan_co_duoc_chon[-1] == 4:
                            if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                self.list_trang_thai[-1] = 2
                                self.list_toa_do[0][0] += 240
                                self.list_first_move[0] += 1
                            if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                self.list_trang_thai[-1] = 3
                                self.list_toa_do[7][0] -= 160
                                self.list_first_move[7] += 1
                        if self.list_quan_co_duoc_chon[-1] == 20:
                            if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                self.list_trang_thai[-1] = 4
                                self.list_toa_do[16][0] += 240
                                self.list_first_move[16] += 1
                            if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                self.list_trang_thai[-1] = 5
                                self.list_toa_do[23][0] -= 160
                                self.list_first_move[23] += 1
                    # ------------tinh diem
                    self.bestmove = min(self.bestmove, self.mo_phong(self.depth, self.player_AI))
                    if self.bestmove_tam > self.bestmove:
                        self.bestmove_tam = self.bestmove
                        self.list_quan_AI.append(self.list_quan_co_duoc_chon[-1])
                        self.list_toa_do_AI.append(self.list_positive_2[n])
                    # ------------undo
                    self.undo()

#######################################################################################################################################################
    def check_win(self):
        if self.list_toa_do[4] == [1000,1000]:
            self.show_score(self.xScreen / 2 - 100, self.yScreen / 2 - 100, " BLACK WIN ", 50)
        if self.list_toa_do[20] == [1000, 1000]:
            self.show_score(self.xScreen / 2 - 100, self.yScreen / 2 - 100, " WHITE WIN ", 50)


    def show_score(self, x, y, scores, size):  # Hiển thị điểm
        font = pygame.font.SysFont("comicsansms", size)
        score = font.render(str(scores), True, (255, 255, 255))
        self.screen.blit(score, (x, y))


#######################################################################################################################################################
    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():  # Bắt các sự kiện
                if event.type == pygame.QUIT:  # sự kiện nhấn thoát
                    self.gamerunning = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.player == 0:
                        pos = pygame.mouse.get_pos()
                        pos_x = pos[0] - pos[0] % 80
                        pos_y = pos[1] - pos[1] % 80
                        if self.click == 0:
                            if self.kiemtra(self.list_toa_do, [pos_x, pos_y]) == True and self.list_toa_do.index([pos_x, pos_y]) < 16:
                                self.click += 1
                                if self.click == 1:
                                    self.list_toa_do_cu.append([pos_x, pos_y])
                                    self.list_quan_co_duoc_chon.append(self.list_toa_do.index([pos_x, pos_y]))
                                    self.list_green_box = [pos_x, pos_y]
                                    self.kt_da_click = 1
                                    self.positive()
                                    print("quan duoc chon:", self.list_quan_co_duoc_chon[-1])

                        if self.click == 1:
                            self.click += 1
                        elif self.click == 2:  # them vao xoa green box sau khi them ham positive move neu click ra ngoai (self.kt_da_click -> 0)
                            pos = pygame.mouse.get_pos()
                            pos_x = pos[0] - pos[0] % 80
                            pos_y = pos[1] - pos[1] % 80
                            # ------------kiem tra quan bi an
                            if self.kiemtra(self.list_toa_do, [pos_x, pos_y]) == True:
                                if self.list_toa_do.index([pos_x, pos_y]) >= 16 and self.kiemtra(self.list_positive, [pos_x, pos_y]) == True:
                                    self.list_toa_do_quan_bi_an.append([pos_x, pos_y])
                                    self.list_quan_bi_an.append(self.list_toa_do.index([pos_x, pos_y]))
                                    self.click = 0
                                    self.player = 1
                                    # -----------green box
                                    self.list_green_box = [pos_x, pos_y]
                                    # ------------undo
                                    self.so_lan_click += 1
                                    # ------------kt quan bi an
                                    self.list_trang_thai.append(1)
                                    # ------------xu ly bi an
                                    self.list_toa_do_moi.append([pos_x, pos_y])
                                    self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = [pos_x, pos_y]
                                    self.list_toa_do[self.list_quan_bi_an[-1]] = [1000, 1000]
                                    # ------------xoa positive
                                    self.list_positive = []
                                    # ------------- kiem tra lan di dau cua tot
                                    # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                                    if ( self.list_quan_co_duoc_chon[-1] == 4) or (self.list_quan_co_duoc_chon[-1] == 20) or (self.list_quan_co_duoc_chon[-1] == 0) or (self.list_quan_co_duoc_chon[-1] == 16) or (self.list_quan_co_duoc_chon[-1] == 7) or (self.list_quan_co_duoc_chon[-1] == 23) or (self.list_quan_co_duoc_chon[-1] in range(8, 16)) or (self.list_quan_co_duoc_chon[-1] in range(24, 32)):
                                        self.list_first_move[self.list_quan_co_duoc_chon[-1]] += 1
                                elif self.list_toa_do.index([pos_x, pos_y]) < 16:

                                    self.kt_da_click = 0
                                    self.list_green_box = []
                                    self.click = 0
                                    # ------------ xoa neu click k hop le
                                    self.list_toa_do_cu.pop(-1)
                                    self.list_quan_co_duoc_chon.pop(-1)
                                    # ------------xoa positive
                                    self.list_positive = []
                            elif self.kiemtra(self.list_toa_do, [pos_x, pos_y]) == False and self.kiemtra(self.list_positive, [pos_x, pos_y]) == True:
                                self.list_toa_do_moi.append([pos_x, pos_y])
                                self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = [pos_x, pos_y]
                                self.click = 0
                                self.player = 1
                                # -----------green box
                                self.list_green_box = [pos_x, pos_y]
                                # ------------undo
                                self.so_lan_click += 1
                                # ------------kt quan bi an
                                self.list_trang_thai.append(0)
                                # ------------xoa positive
                                self.list_positive = []
                                # ------------- kiem tra lan di dau cua tot
                                # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                                if (self.list_quan_co_duoc_chon[-1] == 4) or (self.list_quan_co_duoc_chon[-1] == 20) or (self.list_quan_co_duoc_chon[-1] == 0) or (self.list_quan_co_duoc_chon[-1] == 16) or (self.list_quan_co_duoc_chon[-1] == 7) or (self.list_quan_co_duoc_chon[-1] == 23) or (self.list_quan_co_duoc_chon[-1] in range(8, 16)) or (self.list_quan_co_duoc_chon[-1] in range(24, 32)):
                                    self.list_first_move[self.list_quan_co_duoc_chon[-1]] += 1
                                print("list_buoc_dau = ", self.list_first_move)
                                # ------------- kiem tra nhap thanh
                                if self.list_quan_co_duoc_chon[-1] == 4:
                                    if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                        self.list_trang_thai[-1] = 2
                                        self.list_toa_do[0][0] += 240
                                        self.list_first_move[0] += 1
                                    if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                        self.list_trang_thai[-1] = 3
                                        self.list_toa_do[7][0] -= 160
                                        self.list_first_move[7] += 1
                                if self.list_quan_co_duoc_chon[-1] == 20:
                                    if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                                        self.list_trang_thai[-1] = 4
                                        self.list_toa_do[16][0] += 240
                                        self.list_first_move[16] += 1
                                    if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                                        self.list_trang_thai[-1] = 5
                                        self.list_toa_do[23][0] -= 160
                                        self.list_first_move[23] += 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if self.so_lan_click > 0: self.undo()
            ############################################################################################
            print("list_buoc_dau = ", self.list_first_move)
            if self.kt_da_click !=0 :  self.screen.blit(self.green_box,self.list_green_box)

            if self.list_positive !=[] :
                for t in range(len(self.list_positive)):
                    self.screen.blit(self.yellow_box, self.list_positive[t])

            self.screen.blit(self.rook_white,self.list_toa_do[0])
            self.screen.blit(self.knight_white, self.list_toa_do[1])
            self.screen.blit(self.bishop_white, self.list_toa_do[2])
            self.screen.blit(self.queen_white, self.list_toa_do[3])
            self.screen.blit(self.king_white, self.list_toa_do[4])
            self.screen.blit(self.bishop_white, self.list_toa_do[5])
            self.screen.blit(self.knight_white, self.list_toa_do[6])
            self.screen.blit(self.rook_white, self.list_toa_do[7])
            for x in range(8,16):
                self.screen.blit(self.pawn_white, self.list_toa_do[x])
            self.screen.blit(self.rook_black, self.list_toa_do[16])
            self.screen.blit(self.knight_black, self.list_toa_do[17])
            self.screen.blit(self.bishop_black, self.list_toa_do[18])
            self.screen.blit(self.queen_black, self.list_toa_do[19])
            self.screen.blit(self.king_black, self.list_toa_do[20])
            self.screen.blit(self.bishop_black, self.list_toa_do[21])
            self.screen.blit(self.knight_black, self.list_toa_do[22])
            self.screen.blit(self.rook_black, self.list_toa_do[23])
            for x in range(24, 32):
                self.screen.blit(self.pawn_black, self.list_toa_do[x])
            pygame.display.update()
            self.check_win()
            #-----------------AI implement----------------------------------
            if self.player == 1 :
                self.AI()
                self.list_quan_co_duoc_chon.append(self.list_quan_AI[-1])
                self.list_toa_do_cu.append(self.list_toa_do[self.list_quan_AI[-1]])
                if self.kiemtra(self.list_toa_do, self.list_toa_do_AI[-1]) == True:
                    self.list_toa_do_quan_bi_an.append(self.list_toa_do_AI[-1])
                    self.list_quan_bi_an.append(self.list_toa_do.index(self.list_toa_do_AI[-1]))
                    self.player = 0
                    # ------------undo
                    self.so_lan_click += 1
                    # ------------kt quan bi an
                    self.list_trang_thai.append(1)
                    # ------------xu ly bi an
                    self.list_toa_do_moi.append(self.list_toa_do_AI[-1])
                    self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = self.list_toa_do_AI[-1]
                    self.list_toa_do[self.list_quan_bi_an[-1]] = [1000, 1000]
                    # ------------- kiem tra lan di dau cua tot
                    # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                    if (self.list_quan_co_duoc_chon[-1] == 4) or (self.list_quan_co_duoc_chon[-1] == 20) or (self.list_quan_co_duoc_chon[-1] == 0) or (self.list_quan_co_duoc_chon[-1] == 16) or (self.list_quan_co_duoc_chon[-1] == 7) or (self.list_quan_co_duoc_chon[-1] == 23) or (self.list_quan_co_duoc_chon[-1] in range(8, 16)) or (self.list_quan_co_duoc_chon[-1] in range(24, 32)):
                        self.list_first_move[self.list_quan_co_duoc_chon[-1]] += 1
                elif self.kiemtra(self.list_toa_do, self.list_toa_do_AI[-1]) == False :
                    self.list_toa_do_moi.append(self.list_toa_do_AI[-1])
                    self.list_toa_do[self.list_quan_co_duoc_chon[-1]] = self.list_toa_do_AI[-1]
                    self.player = 0
                    # ------------undo
                    self.so_lan_click += 1
                    # ------------kt quan bi an
                    self.list_trang_thai.append(0)
                    # ------------- kiem tra lan di dau cua tot
                    # ------------- first move cua vua va xe (dung de kiem tra nhap thanh)
                    if (self.list_quan_co_duoc_chon[-1] == 4) or (self.list_quan_co_duoc_chon[-1] == 20) or (self.list_quan_co_duoc_chon[-1] == 0) or (self.list_quan_co_duoc_chon[-1] == 16) or (self.list_quan_co_duoc_chon[-1] == 7) or (self.list_quan_co_duoc_chon[-1] == 23) or (self.list_quan_co_duoc_chon[-1] in range(8, 16)) or (self.list_quan_co_duoc_chon[-1] in range(24, 32)):
                        self.list_first_move[self.list_quan_co_duoc_chon[-1]] += 1
                    # ------------- kiem tra nhap thanh
                    if self.list_quan_co_duoc_chon[-1] == 4:
                        if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                            self.list_trang_thai[-1] = 2
                            self.list_toa_do[0][0] += 240
                            self.list_first_move[0] += 1
                        if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                            self.list_trang_thai[-1] = 3
                            self.list_toa_do[7][0] -= 160
                            self.list_first_move[7] += 1
                    if self.list_quan_co_duoc_chon[-1] == 20:
                        if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == -160:
                            self.list_trang_thai[-1] = 4
                            self.list_toa_do[16][0] += 240
                            self.list_first_move[16] += 1
                        if self.list_toa_do_moi[-1][0] - self.list_toa_do_cu[-1][0] == 160:
                            self.list_trang_thai[-1] = 5
                            self.list_toa_do[23][0] -= 160
                            self.list_first_move[23] += 1
            ##########################################################################################################


if __name__ == "__main__":
    chess = Chess()
    chess.run()
# ham undo :
    #xoa green box sau khi them ham positive move (kt_da_click =0) neu lan click 2 khong hop le
    # them 1 bien kiem tra an quan hay khong de chia lam 2 truong hop (ok)
    # xoa green box (ok)
    # kiem tra theo list_quan_co_duoc_chon de lay lai list_toa_do theo list_toa_do_cu -> remove phan tu cuoi list_toa_do_cu va list_toa_do_moi
    #(pop (-1))
# ham positive :
    # xet theo list_toa_do_moi => quan co gi => xet kha nang => tra ve cac vi tri co the di => them yellow box