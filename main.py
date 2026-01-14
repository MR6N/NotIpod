import sys
import pygame

# ---------- CONFIG ----------

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
FPS = 60

BG_COLOR = (30, 30, 30)          # Background
MENU_BG_COLOR = (45, 45, 45)     # Left menu panel
TEXT_COLOR = (220, 220, 220)
HIGHLIGHT_COLOR = (100, 200, 255)
TITLE_COLOR = (255, 255, 255)

FONT_NAME = "Arial"
TITLE_FONT_SIZE = 28
MENU_FONT_SIZE = 22

MENU_ITEMS = ["Music", "Video", "Emulator", "Radio Tuner", "Clock"]

STATE_MAIN_MENU = "main_menu"
STATE_MUSIC = "music"
STATE_VIDEO = "video"
STATE_EMULATOR = "emulator"
STATE_RADIO = "radio"
STATE_CLOCK = "clock"


class HandheldApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Handheld Launcher")

        self.clock = pygame.time.Clock()
        self.title_font = pygame.font.SysFont(FONT_NAME, TITLE_FONT_SIZE)
        self.menu_font = pygame.font.SysFont(FONT_NAME, MENU_FONT_SIZE)

        self.running = True
        self.state = STATE_MAIN_MENU
        self.selected_index = 0

    # ----- MAIN LOOP -----

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    # ----- EVENTS -----

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if self.state == STATE_MAIN_MENU:
                    self.handle_menu_input(event)
                else:
                    self.handle_screen_input(event)

    def handle_menu_input(self, event):
        if event.key == pygame.K_UP:
            self.selected_index = (self.selected_index - 1) % len(MENU_ITEMS)
        elif event.key == pygame.K_DOWN:
            self.selected_index = (self.selected_index + 1) % len(MENU_ITEMS)
        elif event.key == pygame.K_RETURN:
            self.activate_menu_item()

    def handle_screen_input(self, event):
        # ESC to go back to main menu from any sub‑screen
        if event.key == pygame.K_ESCAPE:
            self.state = STATE_MAIN_MENU

        # Later: add controls per screen (e.g. music play/pause)
        # if self.state == STATE_MUSIC and event.key == pygame.K_SPACE:
        #     self.toggle_music()
        pass

    def activate_menu_item(self):
        label = MENU_ITEMS[self.selected_index]

        if label == "Music":
            self.state = STATE_MUSIC
        elif label == "Video":
            self.state = STATE_VIDEO
        elif label == "Emulator":
            self.state = STATE_EMULATOR
        elif label == "Radio Tuner":
            self.state = STATE_RADIO
        elif label == "Clock":
            self.state = STATE_CLOCK

    # ----- UPDATE -----

    def update(self):
        # Later: animations, clock ticks, radio scanning, etc.
        pass

    # ----- DRAW -----

    def draw(self):
        self.screen.fill(BG_COLOR)

        if self.state == STATE_MAIN_MENU:
            self.draw_main_menu()
        elif self.state == STATE_MUSIC:
            self.draw_screen("Music", "Here you'll list and play songs.")
        elif self.state == STATE_VIDEO:
            self.draw_screen("Video", "Here you'll browse and play videos.")
        elif self.state == STATE_EMULATOR:
            self.draw_screen("Emulator", "Here you'll launch ROMs.")
        elif self.state == STATE_RADIO:
            self.draw_screen("Radio Tuner", "Here you'll tune FM stations.")
        elif self.state == STATE_CLOCK:
            self.draw_screen("Clock", "Here you'll show time and alarms.")

    def draw_main_menu(self):
        menu_width = 180
        pygame.draw.rect(self.screen, MENU_BG_COLOR, (0, 0, menu_width, SCREEN_HEIGHT))

        title_surface = self.title_font.render("Main Menu", True, TITLE_COLOR)
        self.screen.blit(title_surface, (menu_width + 20, 20))

        start_y = 60
        spacing = 45

        for i, label in enumerate(MENU_ITEMS):
            is_selected = (i == self.selected_index)
            color = HIGHLIGHT_COLOR if is_selected else TEXT_COLOR

            if is_selected:
                highlight_rect = pygame.Rect(
                    10,
                    start_y + i * spacing - 6,
                    menu_width - 20,
                    spacing
                )
                pygame.draw.rect(self.screen, (60, 60, 60), highlight_rect, border_radius=6)

            text_surface = self.menu_font.render(label, True, color)
            self.screen.blit(text_surface, (25, start_y + i * spacing))

    def draw_screen(self, title, subtitle):
        menu_width = 180
        pygame.draw.rect(self.screen, MENU_BG_COLOR, (0, 0, menu_width, SCREEN_HEIGHT))

        back_text = self.menu_font.render("ESC: Back", True, TEXT_COLOR)
        self.screen.blit(back_text, (15, SCREEN_HEIGHT - 35))

        title_surface = self.title_font.render(title, True, TITLE_COLOR)
        self.screen.blit(title_surface, (menu_width + 20, 40))

        subtitle_surface = self.menu_font.render(subtitle, True, TEXT_COLOR)
        self.screen.blit(subtitle_surface, (menu_width + 20, 80))


if __name__ == "__main__":
    app = HandheldApp()
    app.run()
