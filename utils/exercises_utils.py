# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 17:37:02 2025

@author: zshaf
"""

import sys

from utils.pose_util.pose import Pose, Pushup, Plank, Squat, Jumpingjack
from utils.video_reader_utils import VideoReader

class Exercise():
    """Class for exercises"""
    def __init__(self, filename:str, exercise:str) -> None:
        self.video_reader = VideoReader(filename)
        if exercise == "predict":
            exercise = "pose"
        self.exercise = exercise.lower().capitalize()
    
    def estimate_exercise(self):
        """Run the estimator"""
        pose_estimator = getattr(sys.modules[__name__], self.exercise)
        pose_estimator = pose_estimator(self.video_reader)
        pose_estimator.estimate() if self.exercise == 'Pose' else pose_estimator.measure()