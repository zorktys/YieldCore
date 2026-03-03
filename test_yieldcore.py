# test_yieldcore.py
"""
Tests for YieldCore module.
"""

import unittest
from yieldcore import YieldCore

class TestYieldCore(unittest.TestCase):
    """Test cases for YieldCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YieldCore()
        self.assertIsInstance(instance, YieldCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YieldCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
