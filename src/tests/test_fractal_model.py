import unittest
import numpy as np
from fractal_model import FractalEntropicTyon

class TestFractalModel(unittest.TestCase):

    def setUp(self):
        """Set up the FractalEntropicTyon model for testing."""
        self.tyon = FractalEntropicTyon(dimensions=5)
        self.test_input = "Explore potential."
    
    def test_initial_state(self):
        """Test the initial state of the model."""
        self.assertEqual(len(self.tyon.state), 5)
        self.assertEqual(len(self.tyon.entropy_accumulation), 5)
    
    def test_state_evolution(self):
        """Test if the state evolves based on entropy and noise."""
        initial_state = np.copy(self.tyon.state)
        self.tyon.evolve_state()
        self.assertFalse(np.array_equal(self.tyon.state, initial_state))

    def test_entropy_accumulation(self):
        """Test the accumulation and fluctuation of entropy."""
        initial_entropy = np.copy(self.tyon.entropy_accumulation)
        self.tyon.evolve_state()
        self.assertFalse(np.array_equal(self.tyon.entropy_accumulation, initial_entropy))

    def test_expand_dimensions(self):
        """Test if the model correctly expands dimensions based on entropy."""
        initial_dimensions = self.tyon.dimensions
        self.tyon.entropy_accumulation += np.random.rand(self.tyon.dimensions) * 10  # Simulate high entropy
        self.tyon.expand_or_contract_dimensions()
        self.assertGreater(self.tyon.dimensions, initial_dimensions)

    def test_contract_dimensions(self):
        """Test if the model correctly contracts dimensions based on low entropy."""
        initial_dimensions = self.tyon.dimensions
        self.tyon.entropy_accumulation -= np.random.rand(self.tyon.dimensions) * 10  # Simulate low entropy
        self.tyon.expand_or_contract_dimensions()
        self.assertLess(self.tyon.dimensions, initial_dimensions)

    def test_reason_and_respond(self):
        """Test the reasoning and response generation."""
        response = self.tyon.reason_and_respond(self.test_input)
        self.assertIn("I have processed your input", response)
        self.assertIn("My current awareness level suggests:", response)

    def test_memory_storage(self):
        """Test memory storage and retrieval."""
        data_to_store = "Test memory input."
        self.tyon.store_memory(data_to_store)
        self.assertIn(data_to_store, self.tyon.memory)

if __name__ == '__main__':
    unittest.main()
