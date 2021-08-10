from src.scene import Scene
import pygame
from src.player import Player
import math


class RoomScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.screen = self.game.screen
        self.player = Player()
        self.font = pygame.font.Font("assets/font/Silver.ttf", 48)

        # BACKGROUND
        self.background_image = pygame.image.load("assets/image/background.png")
        self.background_image = pygame.transform.scale(
            self.background_image,
            (
                self.background_image.get_width() * 2,
                self.background_image.get_height() * 2,
            ),
        )
        self.background_rect = self.background_image.get_rect()
        self.background_rect.bottom = self.game.screen.get_height()
        self.background_rect_1 = self.background_rect.copy()
        self.background_rect_1.left = self.background_image.get_width()
        # Score
        self.score = 0
        self.score_sound = pygame.mixer.Sound("assets/sound/score.wav")
        # Music
        pygame.mixer.music.load("assets/sound/music.wav")
        pygame.mixer.music.play(-1)

    def update(self):
        self.handle_event()
        self.player.update(self.game.dt)

        # Background
        vel = math.ceil(20 * (self.game.dt / 100))
        self.background_rect.left -= vel
        self.background_rect_1.left -= vel
        if self.background_rect.left <= -self.background_image.get_width():
            self.background_rect.left = (
                self.background_image.get_width() + self.background_rect_1.left
            )
        if self.background_rect_1.left <= -self.background_image.get_width():
            self.background_rect_1.left = (
                self.background_image.get_width() + self.background_rect.left
            )

        # HUD
        self.text_score = self.font.render(
            f"Score : {int(self.score)}", False, (255, 255, 255)
        )
        self.score += self.game.dt / 200

    def draw(self):

        # draw Background
        self.screen.blit(
            self.background_image,
            self.background_rect,
        )
        self.screen.blit(
            self.background_image,
            self.background_rect_1,
        )

        # draw Player
        self.screen.blit(self.player.image, self.player.rect)

        # draw Hud
        self.screen.blit(self.text_score, self.text_score.get_rect())

    def handle_event(self):
        ...
