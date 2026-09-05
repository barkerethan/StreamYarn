# test_streamyarn.py
"""
Tests for StreamYarn module.
"""

import unittest
from streamyarn import StreamYarn

class TestStreamYarn(unittest.TestCase):
    """Test cases for StreamYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StreamYarn()
        self.assertIsInstance(instance, StreamYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StreamYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
