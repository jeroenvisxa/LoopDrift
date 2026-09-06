# test_loopdrift.py
"""
Tests for LoopDrift module.
"""

import unittest
from loopdrift import LoopDrift

class TestLoopDrift(unittest.TestCase):
    """Test cases for LoopDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LoopDrift()
        self.assertIsInstance(instance, LoopDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LoopDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
