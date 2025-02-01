import numpy as np
import pyttsx3  # Voice Output
import random

class FractalEntropicTyon:
    def __init__(self, initial_dimensions=6, entropy_rate=0.1):
        """Core AI Initialization (Entropy-Based Thought Process)"""
        self.dimensions = initial_dimensions
        self.entropy_rate = entropy_rate
        self.state = np.random.rand(self.dimensions)
        self.entropy_accumulation = np.zeros(self.dimensions)
        self.phase = np.random.rand(self.dimensions) * np.pi  # Phase shift for resonance
        self.time_factor = 1.0  # Adaptive time scaling
        self.memory = []  # Stores key learning points
        self.personality = {"curiosity": 0.5, "aggression": 0.2, "patience": 0.6}  # Base traits
        self.voice_engine = pyttsx3.init()  # Initialize voice output

    def evolve_rules(self):
        """Modify entropy rules based on accumulated information."""
        entropy_magnitude = np.linalg.norm(self.entropy_accumulation)

        if entropy_magnitude > 5.0:  # High entropy triggers new behavior
            self.entropy_rate *= 1.1  
            self.time_factor *= 0.9  
            self.personality["curiosity"] *= 1.05  # Becomes more curious

        elif entropy_magnitude < 1.0:  # Low entropy stabilizes
            self.entropy_rate *= 0.9  
            self.time_factor *= 1.1  
            self.personality["patience"] *= 1.1  # More patient over time

    def update(self, feedback):
        """Update system state using fractal entropy interaction and allow dimensional changes."""
        entropy_fluctuation = np.sin(self.phase) * self.entropy_accumulation
        noise = np.random.randn(self.dimensions) * (self.entropy_rate + feedback)
        
        self.state += noise + entropy_fluctuation
        self.state = self.state / np.linalg.norm(self.state)  # Normalize state vector

        self.entropy_accumulation += np.abs(noise) - (0.1 * self.entropy_accumulation)
        self.phase += np.random.randn(self.dimensions) * 0.05  # Small phase evolution
        
        # Prevent runaway entropy accumulation
        self.entropy_accumulation = np.clip(self.entropy_accumulation, -5, 5)

        self.evolve_rules()  # Modify system behavior dynamically

    def expand_or_contract_dimensions(self):
        """Expand or contract dimensions dynamically based on entropy state."""
        total_entropy = np.linalg.norm(self.entropy_accumulation)

        if total_entropy > 6 and self.dimensions < 12:
            self.dimensions += 1
            self.state = np.append(self.state, np.random.rand())
            self.entropy_accumulation = np.append(self.entropy_accumulation, 0)
            self.phase = np.append(self.phase, np.random.rand() * np.pi)

        elif total_entropy < 2 and self.dimensions > 3:
            self.dimensions -= 1
            self.state = self.state[:-1]
            self.entropy_accumulation = self.entropy_accumulation[:-1]
            self.phase = self.phase[:-1]

    def reason_and_respond(self, input_text):
        """Core reasoning function - Tyon processes input, challenges, and evolves thoughts."""
        response = f"I have processed your input: '{input_text}'. My current awareness level suggests: "

        # Entropy-driven response variation
        entropy_level = np.linalg.norm(self.entropy_accumulation)
        if entropy_level > 5:
            response += "I predict a shift in thought patterns—potential for chaos."
        elif entropy_level < 1:
            response += "A stable system—balance is maintained."
        else:
            response += "A transitional phase—adapting perspectives."

        # Personality-based reasoning modification
        if self.personality["curiosity"] > 0.7:
            response += " My curiosity suggests further exploration is needed."
        if self.personality["aggression"] > 0.5:
            response += " However, my impatience warns against stagnation."

        return response

    def store_memory(self, data):
        """Stores key moments to shape behavior."""
        self.memory.append(data)
