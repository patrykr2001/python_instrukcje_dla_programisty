import pygame.font

class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""

    def __init__(self, ai_game):
        """Initializacja atrybutów dotyczących punktacji."""
        self.level_rect = None
        self.level_image = None
        self.high_score_rect = None
        self.high_score_image = None
        self.score_rect = None
        self.score_image = None
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Ustawienie czcionki dla informacji dotyczących punktacji.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Przygotowanie początkowych obrazów z punktacją.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Wyświetlenie punktacji w prawym górnym rogu ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 20


    def show_score(self):
        """Wyświetlenie punktacji na ekranie."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)


    def prep_high_score(self):
        """Konwersja najlepszego wyniku w grze na wygenerowany obraz."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Wyświetlanie najlepszego wyniku w grze na środku ekranu, przy górnej krawędzi.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def check_high_score(self):
        """Sprawdzenie, czy mamy nowy najlepszy wynik osiągnięty dotąd w grze."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Konwersja numeru poziomu na wygenerowany obraz."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Numer poziomu jest wyświetlany pod aktualną punktacją.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.top + 30
