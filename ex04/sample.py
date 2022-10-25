import pygame  as pg
import sys

def main():
    pg.display.set_caption("初めてのPyGame") #タイトルバー
    scrn_sfc = pg.display.set_mode((800, 600)) #Surface

    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 700, 400
    scrn_sfc.blit(tori_sfc, tori_rct) #貼り付け

    pg.display.update()

    clock = pg.time.Clock()
    clock.tick(0.2) #フレームレート
    
    

if __name__ == "__main__":
    pg.init() #初期化
    main()
    pg.quit() #初期化解除
    sys.exit() #終了