import pygame

# Slider GUI Constants
NUM_HUNTERS = 2  # Initial number of hunters
WIDTH, HEIGHT = 200, 200
SLIDER_WIDTH = 800
SLIDER_HEIGHT = 20
SLIDER_COLOR = (255, 255, 255)
SLIDER_THUMB_RADIUS = 3
SLIDER_THUMB_COLOR = (0, 255, 255)
TEXT_COLOR = (0, 255, 255)
FONT_SIZE = 22

# Initial safe distance value
SAFE_DISTANCE = 2.0

def draw_slider(screen, slider_pos, slider_value):
    """Draws the slider on the screen."""
    x, y = slider_pos
    slider_rect = pygame.Rect(x, y, SLIDER_WIDTH, SLIDER_HEIGHT)
    pygame.draw.rect(screen, SLIDER_COLOR, slider_rect)

    # Calculate thumb position
    thumb_x = x + (slider_value / 100) * SLIDER_WIDTH - SLIDER_THUMB_RADIUS
    thumb_y = y + SLIDER_HEIGHT // 2 - SLIDER_THUMB_RADIUS
    thumb_rect = pygame.Rect(thumb_x, thumb_y, 2 * SLIDER_THUMB_RADIUS, 2 * SLIDER_THUMB_RADIUS)
    pygame.draw.circle(screen, SLIDER_THUMB_COLOR, thumb_rect.center, SLIDER_THUMB_RADIUS)

    # Draw text for slider value
    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render(f"Safe Distance: {slider_value}", True, TEXT_COLOR)
    screen.blit(text, (x, y - FONT_SIZE - 5))

# ... (rest of your slider.py code)

def handle_slider_event(event, pos):
    """Handles slider events, updating SAFE_DISTANCE, NUM_HUNTERS, and handling button clicks."""
    global SAFE_DISTANCE, NUM_HUNTERS
    x, y = pos
    # Handle SAFE_DISTANCE slider
    if x >= pos[0] and x <= pos[0] + SLIDER_WIDTH and y >= pos[1] and y <= pos[1] + SLIDER_HEIGHT:
        if event.type == pygame.MOUSEBUTTONDOWN:
            SAFE_DISTANCE = (event.pos[0] - x) / SLIDER_WIDTH * 100
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            SAFE_DISTANCE = (event.pos[0] - x) / SLIDER_WIDTH * 100
    # Handle NUM_HUNTERS slider (assuming it's positioned below the SAFE_DISTANCE slider)
    elif x >= pos[0] and x <= pos[0] + SLIDER_WIDTH and y >= pos[1] + SLIDER_HEIGHT + 10 and y <= pos[1] + SLIDER_HEIGHT + 10 + SLIDER_HEIGHT:
        if event.type == pygame.MOUSEBUTTONDOWN:
            NUM_HUNTERS = int((event.pos[0] - x) / SLIDER_WIDTH * (MAX_HUNTERS - 2)) + 2  # Adjust range as needed
            NUM_HUNTERS = min(NUM_HUNTERS, MAX_HUNTERS)  # Cap at MAX_HUNTERS
            NUM_HUNTERS = max(NUM_HUNTERS, 2)  # Ensure minimum of 2 hunters
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            # Calculate the new number of hunters based on the slider position
            new_num_hunters = int((event.pos[0] - x) / SLIDER_WIDTH * (MAX_HUNTERS - 2)) + 2
            # Increment or decrement by 1, depending on the direction of the mouse movement
            if new_num_hunters > NUM_HUNTERS:
                NUM_HUNTERS += 1
            elif new_num_hunters < NUM_HUNTERS:
                NUM_HUNTERS -= 1
            NUM_HUNTERS = min(NUM_HUNTERS, MAX_HUNTERS)  # Cap at MAX_HUNTERS
            NUM_HUNTERS = max(NUM_HUNTERS, 2)  # Ensure minimum of 2 hunters

    # Handle "Add Hunter" button click
    elif x >= pos[0] + SLIDER_WIDTH + 10 and x <= pos[0] + SLIDER_WIDTH + 10 + BUTTON_WIDTH and y >= pos[1] and y <= pos[1] + BUTTON_HEIGHT:
        if event.type == pygame.MOUSEBUTTONDOWN:
            NUM_HUNTERS += 1
            NUM_HUNTERS = min(NUM_HUNTERS, MAX_HUNTERS)  # Cap at MAX_HUNTERS

    return SAFE_DISTANCE, NUM_HUNTERS
