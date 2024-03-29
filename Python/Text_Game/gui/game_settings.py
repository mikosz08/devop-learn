from pygame import font

WIN_WIDTH, WIN_HEIGHT = 900, 500
FPS = 30
WIN_TITLE = "text_game"
TEXT_FONT_DEFAULT = font.get_default_font()
TEXT_FONT_CONSOLAS = "Consolas"

# TEXT & COLORS:
C_WHITE     = (255, 255, 255)
C_BLACK     = (0, 0, 0)
C_RED       = (255, 0, 0)
C_GREEN     = (0, 255, 0)
C_BLUE      = (0, 0, 255)
C_YELLOW    = (255, 255, 0)
C_CYAN      = (0, 255, 255)
C_MAGENTA   = (255, 0, 255)
C_SILVER    = (192, 192, 192)
C_GREY      = (128, 128, 128)
C_MAROON    = (128, 0, 0)
C_OLIVE     = (128, 128, 0)
C_GREEN     = (0, 128, 0)
C_PURPLE    = (128, 0, 128)
C_TEAL      = (0, 128, 128)
C_NAVY      = (0, 0, 128)

ANTIALIASING_THRESHOLD = 15

# CORDS:
POS_OFFSET = 35
WINDOW_CENTER_POS = (WIN_WIDTH/2, WIN_HEIGHT/2)

WINDOW_BOTTOM_RIGHT_POS = (WIN_WIDTH - POS_OFFSET, WIN_HEIGHT - POS_OFFSET)
WINDOW_BOTTOM_LEFT_POS = (POS_OFFSET, WIN_HEIGHT - POS_OFFSET)

WINDOW_TOP_RIGHT_POS = (WIN_WIDTH - POS_OFFSET, POS_OFFSET)
WINDOW_TOP_LEFT_POS = (POS_OFFSET, POS_OFFSET)

WINDOW_TOP_POS = (WIN_WIDTH/2, POS_OFFSET)
WINDOW_BOTTOM_POS = (WIN_WIDTH/2, WIN_HEIGHT - POS_OFFSET)

WINDOW_RIGHT_POS = (WIN_WIDTH - POS_OFFSET, WIN_HEIGHT/2)
WINDOW_LEFT_POS = (POS_OFFSET, WIN_HEIGHT/2)

WIN_POSITIONS = (
    WINDOW_TOP_LEFT_POS,
    WINDOW_TOP_POS,
    WINDOW_TOP_RIGHT_POS,
    WINDOW_RIGHT_POS,
    WINDOW_BOTTOM_RIGHT_POS,
    WINDOW_BOTTOM_POS,
    WINDOW_BOTTOM_LEFT_POS,
    WINDOW_LEFT_POS,
    WINDOW_CENTER_POS
)


def adjust_pos(pos, width=0, height=0) -> tuple:
    return (pos[0] + width, pos[1] + height)
