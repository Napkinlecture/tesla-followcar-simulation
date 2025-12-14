# Tesla Follow-Car Mode: A Pursuit-Evasion Simulation

## 🚗 Project Overview
This project is a computational investigation into **autonomous vehicle platooning**, inspired by Tesla's proposed "Follow-car mode." It translates principles from **biological pursuit-evasion** (like predator-prey dynamics) into a algorithmic model for multi-vehicle coordination. The core innovation is the replacement of a generic flocking engine with a custom differential equation-based pursuit model to study stability and efficiency in vehicle convoys.

> **Core Contribution:** This isn't a modified flocking demo. It's a **new simulation engine** (`commotion.py`) built within an existing visualization framework to explore a specific automotive application.

## 📋 Table of Contents
- [Inspiration & Objective](#-inspiration--objective)
- [Core Technical Implementation](#-core-technical-implementation)
- [Key Features & Insights](#-key-features--insights)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Results & Discussion](#-results--discussion)
- [Acknowledgements](#-acknowledgements)

## 💡 Inspiration & Objective
The project was sparked by the Tesla community idea for a **"Follow-car mode"** [[Idea #23371]](https://teslaideas.ideascale.com/c/teslaideas/idea/23371), which envisions a system where vehicles can autonomously form efficient, cooperative platoons on highways.

**Primary Objective:** To model and analyze such a system by creating a **pursuit-evasion simulation** where "follower" vehicles (hunters) intelligently track and maintain a safe distance from a "leader" vehicle (prey). The goal is to observe emergent platoon behaviors and measure metrics like stability and convergence time.

## ⚙️ Core Technical Implementation
The simulation's logic is fundamentally different from the original flocking base:
*   **Original Base (`boid.py`):** Used Craig Reynolds' classic Boids algorithm (separation, alignment, cohesion).
*   **This Project (`commotion.py`):** Implements a **custom differential pursuit model** defined by parameters `b₁, b₂, b₃, b₄`. These parameters control the attraction/repulsion forces between agents, directly modeling the strategic decisions in a multi-vehicle pursuit scenario.

**Key Components:**
- **`Agent` Class:** Models each vehicle with properties for position, speed, and role (hunter/prey).
- **`get_directions()`:** Calculates the normalized pursuit vectors based on relative positions.
- **`update_position()`:** Applies the pursuit dynamics to move agents each simulation step.
- **Interactive Safety Control:** The included `slider.py` module allows real-time adjustment of the **"safe distance"** threshold, demonstrating adaptive collision avoidance.

## 🔑 Key Features & Insights
*   **Novel Dynamics:** Explores `b₁, b₂, b₃, b₄` parameter space for tuning platoon behavior (aggressive follow, cautious distance, etc.).
*   **Real-Time Visualization:** Built with **PyGame** to visually demonstrate the pursuit process and the critical "capture" event.
*   **Quantifiable Outcomes:** The simulation provides a basis for measuring:
    *   **Platoon Formation Time:** How quickly followers stabilize behind the leader.
    *   **Safety Compliance:** Percentage of time the "safe distance" constraint is violated.
    *   **Energy Efficiency Potential:** Smooth, cooperative pursuit can model reduced aerodynamic drag and braking in platoons.
*   **Interactive Research Tool:** Serves as a testbed for developing and prototyping cooperative driving algorithms.

## 📁 Project Structure
tesla-followcar-simulation/
├── commotion.py # CORE SIMULATION ENGINE: Pursuit-evasion logic
├── run_tesla.py # Main launcher script
├── requirements.txt # Python dependencies (pygame, numpy)
├── slider.py # Interactive safety distance controller (from base)
├── constants.py # Simulation constants (from base)
└── README.md # This file


## 🚀 Getting Started

### Prerequisites
*   Python 3.7+
*   pip (Python package installer)

### Installation & Running
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Napkinlecture/tesla-followcar-simulation.git
    cd tesla-followcar-simulation
    ```
2.  **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the simulation:**
    ```bash
    # Launcher expects initial (x, y) coordinates for 3 agents
    python run_tesla.py <x1> <y1> <x2> <y2> <x3> <y3>
    ```
    **Example:** `python run_tesla.py 100 200 300 400 500 600`

## 📈 Results & Discussion
Running the simulation demonstrates the viability of using pursuit-evasion rules for vehicle coordination. You can observe:
*   **Emergent Platooning:** Followers naturally converge into a stable formation behind the leader.
*   **Safety-Centric Design:** The "safe distance" slider provides immediate visual feedback on collision avoidance.
*   **Research Foundation:** This model opens avenues for further work on communication protocols, heterogeneous vehicle types, and complex traffic scenarios.

**Simulated Insight:** Preliminary observations suggest that cooperative pursuit rules can lead to more stable and potentially more energy-efficient platoons compared to simple rule-based following, by minimizing oscillatory "slinky" effects.

## 🙏 Acknowledgements
*   **Simulation Framework:** This project utilizes the visualization and UI infrastructure from [Joseph Bakulikira's Flocking Simulation](https://github.com/Josephbakulikira/simple-Flocking-simulation-python-pygame). The core flocking logic (`boid.py`) was replaced for this specialized application.
*   **Conceptual Inspiration:** The "Follow-car mode" concept proposed by the Tesla community [[Idea #23371]](https://teslaideas.ideascale.com/c/teslaideas/idea/23371) provided the foundational idea for this technical exploration.
*   **Academic Inspiration:** Draws upon principles from computational ethology, differential equations, and multi-agent systems.

---
**Built by [Your Name/ Napkinlecture] | [View on GitHub](https://github.com/Napkinlecture/tesla-followcar-simulation)**
