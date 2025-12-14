
import numpy as np
import slider

VIEW_DISTANCE = 50  # Distance for boid rules

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
