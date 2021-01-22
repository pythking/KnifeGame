#sprite classes
from settings import *



class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, "idle.png")).convert()
        self.image.set_colorkey(black)
        self.image = pg.transform.scale(self.image, (45, 66))
        self.rect = self.image.get_rect()
        self.pos = vec(200, screen_height - 60)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.acc = vec(0, PLAYER_GRAV)

        if hits:
            if self.vel.y >= 0 and hits[0].rect.left < self.pos.x < hits[0].rect.right and self.rect.centery < hits[0].rect.centery:  # stop on platforms
                self.pos.y = hits[0].rect.top+1
                self.vel.y = 0

        #keys pressed ?
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = +PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION  #friction
        self.vel += self.acc        #motion equations
        self.pos += self.vel + 0.5 * self.acc

        if abs(self.vel.x) < 0.3:
            self.vel.x = 0

        #block player on sides
        if self.pos.x+(self.rect.width/2) > screen_width:
            self.pos.x = screen_width-(self.rect.width/2)
        if self.pos.x-(self.rect.width/2) < 0:
            self.pos.x = (self.rect.width/2)

        self.rect.midbottom = self.pos

    def jump(self):
        #jump only if standing on smth
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = JUMP_HEIGHT



class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, "platform.png")).convert()
        self.image = pg.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass








