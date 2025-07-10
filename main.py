# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:31:32 2025

@author: zshaf
"""

import argparse
from utils.exercises_utils import Exercise
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', required=False, default=int(0),
                        help='Path to video source file', type=str)
    parser.add_argument('-e', '--exercise', required=False, default="predict",
                        help='Type of exercise in video source',
                        type=str, choices=['predict', 'pushup', 'plank', 'squat', 'jumpingjack'])
    
    #Test args parse
    sys.argv = ["main.py", "--video", "data/videos/pushup_input_test.mp4", "--exercise", "pushup"]
    
    args = parser.parse_args()
    video = args.video
    exercise = args.exercise

    pose = Exercise(video, exercise)
    pose.estimate_exercise()

if __name__ == '__main__':
    main()