import pygame
import numpy as np
import ctypes
import argparse
import slider  # Import the slider module
import boid  # Import the boid module

# Constants
WIDTH, HEIGHT = 1920, 1080
STEP_SIZE = 0.5  # Numerical step for the simulation
AGENT_RADIUS = 16 # Radius for displaying agents
VIEW_DISTANCE = 100  # Distance for boid rules

# Agent speeds and step size (from your equations)
b_1 = 1.0
b_2 = 1.0
b_3 = 2.0
b_4 = 1.0
h = STEP_SIZE

# Function to set the window as always on top
def set_window_always_on_top(window_handle):
    ctypes.windll.user32.SetWindowPos(window_handle, -1, 0, 0, 0, 0, 1)

# Agent class definition
class Agent:
    def __init__(self, x, y, speed, color):
        self.position = np.array([x, y], dtype=float)
        self.speed = speed
        self.color = color

    def update_position(self, dir_h1, dir_h2, dir_prey):
        # Hunter 1
        if self is hunter1:
            if np.linalg.norm(dir_h1) < np.linalg.norm(dir_h2):
                self.position += self.speed * STEP_SIZE * dir_h1 / np.linalg.norm(dir_h1)
            else:
                self.position += self.speed * STEP_SIZE * dir_h2 / np.linalg.norm(dir_h2)
        # Hunter 2
        elif self is hunter2:
            self.position += self.speed * STEP_SIZE * (dir_h1 / np.linalg.norm(dir_h1) + b_4 * dir_h2 / np.linalg.norm(dir_h2))
        #  Prey
        elif self is prey:
            self.position += self.speed * STEP_SIZE * (dir_h2 / np.linalg.norm(dir_h2) - b_4 * dir_h1 / np.linalg.norm(dir_h1))

# Function to calculate the direction vectors
def get_directions(agent1, agent2, agent3):
    P = agent1.position - agent2.position  # Hunter 1 to Hunter 2
    Q = agent1.position - agent3.position  # Hunter 1 to Prey
    R = agent2.position - agent3.position  # Hunter 2 to Prey

    # Normalize the direction vector for the Hunter 1
    if np.linalg.norm(P) < np.linalg.norm(Q) and np.linalg.norm(P) != 0:
        dir_prey = P / np.linalg.norm(P)  # Normalization to unit vector
    else:
        dir_prey = Q / np.linalg.norm(Q)
		
#if np.linalg.norm(Q) != 0 else np.array([0, 0])  # Normalize Q if necessary

    # Normalize the direction vector for the Hunter 2
    dir_h2 = P / np.linalg.norm(P) + R / np.linalg.norm(R) if np.linalg.norm(R) != 0 else np.array([0, 0])  # Normalization

    # Normalize the direction vector for the prey
    dir_h1 = Q / np.linalg.norm(Q) - R / np.linalg.norm(R) if np.linalg.norm(R) != 0 else np.array([0, 0])  # Normalization

    return dir_h1, dir_h2, dir_prey
	
	# Function to calculate boid rules
def calculate_boid_rules(agent, agents):
    separation_force = np.array([0, 0])
    alignment_force = np.array([0, 0])
    cohesion_force = np.array([0, 0])
    num_neighbors = 0

    for other_agent in agents:
        if other_agent is not agent:
            distance = np.linalg.norm(agent.position - other_agent.position)
            if distance < VIEW_DISTANCE:
                # Separation
                if distance < slider.SAFE_DISTANCE:
                    separation_force += (agent.position - other_agent.position) / distance
                # Alignment
                alignment_force += other_agent.direction
                # Cohesion
                cohesion_force += other_agent.position
                num_neighbors += 1

    if num_neighbors > 0:
        alignment_force /= num_neighbors
        cohesion_force /= num_neighbors
        cohesion_force = agent.position - cohesion_force

    return separation_force, alignment_force, cohesion_force

def main():
    global hunter1, hunter2, prey
    
    # Setup Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Boid Touring Simulation v1.0.0")
    set_window_always_on_top(pygame.display.get_wm_info()['window'])

    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("initial_positions", nargs=6, type=int, help="Initial positions (x1, y1, x2, y2, x3, y3)")
    args = parser.parse_args()

    initial_positions = [
        (args.initial_positions[0], args.initial_positions[1]),
        (args.initial_positions[2], args.initial_positions[3]),
        (args.initial_positions[4], args.initial_positions[5]),
    ]

      # Create agents based on user inputs
    hunter2 = Agent(x=initial_positions[2][0], y=initial_positions[2][1], speed=b_1, color=(0, 255, 0))  # green
    prey = Agent(x=initial_positions[1][0], y=initial_positions[1][1], speed=b_2, color=(0, 255, 0))  # green
    hunter1 = Agent(x=initial_positions[0][0], y=initial_positions[0][1], speed=b_3, color=(255, 255, 0))  # yellow

    # Simulation loop
    running = True
    step = 0
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Handle slider events
            slider.handle_slider_event(event, (WIDTH // 2 - slider.SLIDER_WIDTH // 2, HEIGHT // 2 - slider.SLIDER_HEIGHT // 2))

        # Calculate directions for hunters and prey
        dir_h1, dir_h2, dir_prey = get_directions(hunter1, hunter2, prey)

        # Update positions of the agents
        hunter1.update_position(dir_h1, dir_h2, dir_prey)
        hunter2.update_position(dir_h1, dir_h2, dir_prey)
        prey.update_position(dir_h1, dir_h2, dir_prey)

         # Check distances to determine if prey is caught
        if np.linalg.norm(hunter1.position - prey.position) < slider.SAFE_DISTANCE or \
           np.linalg.norm(hunter2.position - prey.position) < slider.SAFE_DISTANCE:
            print("Prey caught!")
            running = False

        # Clear screen and redraw agents
        screen.fill((0, 0, 0))   # Clear screen with white color
        pygame.draw.circle(screen, hunter1.color, (int(hunter1.position[0]), int(hunter1.position[1])), AGENT_RADIUS)
        pygame.draw.circle(screen, hunter2.color, (int(hunter2.position[0]), int(hunter2.position[1])), AGENT_RADIUS)
        pygame.draw.circle(screen, prey.color, (int(prey.position[0]), int(prey.position[1])), AGENT_RADIUS)
		
         # Draw the slider
        slider.draw_slider(screen, (WIDTH // 2 - slider.SLIDER_WIDTH // 2, HEIGHT // 2 - slider.SLIDER_HEIGHT // 2), slider.SAFE_DISTANCE)

        # Update the display
        pygame.display.flip()
        pygame.time.delay(100)  # Delay for a bit to control the frame rate

    pygame.quit()  # Clean up and close the Pygame window

if __name__ == "__main__":
    main()
