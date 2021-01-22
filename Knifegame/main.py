# game
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption(Title)
        self.running = True
        self.clock = pg.time.Clock()

    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()        #create all sprites
        self.platforms = pg.sprite.Group()
        self.ennemis = pg.sprite.Group()

        for plat in PLATFORM_LIST1:
            p = Platform(*plat, self)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.player = Player(self)
        self.all_sprites.add(self.player)

        self.run()

    def run(self):
        #game loop
        if self.running == False:
            return
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        #game loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()


    def draw(self):     #game loop - draw
        self.screen.fill(bg_color)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def start_screen(self):
        self.screen.fill(bg_color)
        pg.display.flip()

    def GO_screen(self):
        self.screen.fill(bg_color)
        pg.display.flip()


    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.game_font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)



g = Game()
g.start_screen()
while g.running:
    g.new()
    g.GO_screen()

pg.quit()
