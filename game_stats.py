class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, settings):
        """Initialize statistics."""
        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        # Start game in inactive state.
        self.game_active = False