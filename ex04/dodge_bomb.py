import pygame  as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):#引数：こうかとん/爆弾rct, スクリーンrct
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1.1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1.1
    return yoko, tate

def check_bound2(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1.25
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1.25
    return yoko, tate

def gameover():
    screen = pg.display.set_mode((1600, 900))    # 画面を作成
    pg.display.set_caption("爆弾")    # タイトルを作成
    #フォントの用意  
    font = pg.font.SysFont(None, 150)
    #テキストの設定
    text = font.render("GAMEOVER", True, (255,0,0))
    #メインループ
    while True:
        #テキストを描画
        screen.blit(text, (500,400))
        pg.display.update() #描画処理を実行
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 終了イベント
                return

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #練習3
    tori_sfc = pg.image.load("fig/5.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #練習5
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc,(255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    bomb2_sfc = pg.Surface((20, 20))
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc,(0, 0, 255), (10, 10), 10)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = randint(0, scrn_rct.width)
    bomb2_rct.centery = randint(0, scrn_rct.height)

    vx, vy = +1, +1
    wx, wy = +1, +1

    fps = 0

    clock = pg.time.Clock()
    while True:
        #練習2
        scrn_sfc.blit(bg_sfc, bg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #練習4
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: tori_rct.centery -= 1
        if key_lst[pg.K_DOWN]: tori_rct.centery += 1
        if key_lst[pg.K_LEFT]: tori_rct.centerx -= 1
        if key_lst[pg.K_RIGHT]: tori_rct.centerx += 1

        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_lst[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_lst[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_lst[pg.K_UP]:
                tori_rct.centery += 1
            if key_lst[pg.K_DOWN]:
                tori_rct.centery -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        bomb_rct.move_ip(vx,vy) #練習6
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        
        if tori_rct.colliderect(bomb_rct):
            gameover()
            return
        if tori_rct.colliderect(bomb2_rct):
            if a > 10000:
                gameover()
                return
        
        if fps > 10000:
            yk, tt = check_bound2(bomb2_rct, scrn_rct)
            wx *= yk
            wy *= tt
            bomb2_rct.move_ip(wx, wy)
            scrn_sfc.blit(bomb2_sfc, bomb2_rct)
        fps += 2
        
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() #初期化
    main()
    pg.quit() #初期化解除
    sys.exit() #終了