# test_riftnexus.py
"""
Tests for RiftNexus module.
"""

import unittest
from riftnexus import RiftNexus

class TestRiftNexus(unittest.TestCase):
    """Test cases for RiftNexus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RiftNexus()
        self.assertIsInstance(instance, RiftNexus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RiftNexus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
