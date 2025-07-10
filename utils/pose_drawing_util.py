# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 17:16:29 2025

@author: zshaf
"""

import cv2
import mediapipe as mp
import numpy as np
from PIL import Image,ImageFont,ImageDraw

## initialize pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_drawing_styles = mp.solutions.drawing_styles
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

class Draw():
    """Helper class for drawing utils"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = ImageFont.truetype('../data/fonts/arial.ttf', self.height//24, encoding="unic")
        
    def skeleton(self, image, pose_results):
        """draw skeleton on the frame"""
        mp_drawing.draw_landmarks(image, 
                                  pose_results.pose_landmarks, 
                                  mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        return image
    
    def pose_text(self, image, estimated_pose):
        """Add text to image"""
        pil_image = Image.fromarray(image)
        pil_draw = ImageDraw.Draw(pil_image)
        text_width,_ = pil_draw.textsize(estimated_pose.upper(), font = self.font)
        pil_draw.text(((self.width - text_width) / 2, self.height//16 + 20), estimated_pose.upper(),(255,255,255), font = self.font)
        image = np.array(pil_image)
        return image
    
    def overlay(self,image):
        """Draw overlay in the image"""
        alpha = 0.5
        overlay = image.copy()
        cv2.rectangle(overlay, (0,self.height//16), (self.width, self.height//8) , (25,25,25), -1)
        image = cv2.addWeighted(overlay,alpha,image, 1 - alpha,0)
        return image
    
    def draw_line(self, image, coord1, coord2):
        """Draw a line in the image"""
        cv2.line(image, coord1, coord2, thickness=4, color = (255,255,255))
        return image
    
    
        
    