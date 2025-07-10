# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:01:09 2025

@author: zshaf
"""

import unittest
from unittest.mock import patch
import argparse
from main import Exercise

class TestExerciseScript(unittest.TestCase):
    
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(video='test_video.mp4', exercise='pushup'))
    @patch('main.Exercise')
    def test_exercise_initialization(self, MockExercise, mock_args):
        """Test if the Exercise class is initialized correctly with given arguments."""
        from main import main  # Import main function if refactored, else run script manually
        main()  # Assuming you refactor the script into a function called main()
        
        MockExercise.assert_called_once_with('test_video.mp4', 'pushup')
        MockExercise.return_value.estimate_exercise.assert_called_once()

if __name__ == '__main__':
    unittest.main()