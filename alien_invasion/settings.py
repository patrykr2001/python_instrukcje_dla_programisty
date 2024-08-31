class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjacja ustawień gry."""
        self.alien_points = None
        self.fleet_direction = None
        self.alien_speed_factor = None
        self.bullet_speed_factor = None
        self.ship_speed_factor = None

        # Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku.
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Ustawienia dotyczące obcego.
        self.alien_drop_speed_factor = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = 2.5
        self.alien_speed_factor = 1.5
        # 1 prawo, -1 lewo
        self.fleet_direction = 1

        # Punktacja
        self.alien_points = 50



    def increase_speed(self):
        """Zmiana ustawień dotyczących prędkości."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points *= int(self.alien_points * self.score_scale)

