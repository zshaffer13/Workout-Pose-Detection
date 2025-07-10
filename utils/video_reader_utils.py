# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 22:45:55 2025

@author: zshaf
"""

import cv2

class VideoReader:
    """Helper class for video utils"""
    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)
        self._total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self._current_frame = 0
        
    def read_frame(self):
        """Read a Frame"""
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret is False or frame is None:
                return None
            self._current_frame += 1 
        else:
            return None
        return frame
    
    def read_n_frame(self, num_frames =1):
        """Read n number of frames"""
        frames_list = []
        for _ in range(num_frames):
            if self.cap.isOpened():
                ret,frame = self.cap.read()
                if ret is False or frame is None:
                    return None
                frames_list.append(frame)
                self._current_frame +=1
            else:
                return None
        return frames_list
    
    def is_opened(self):
        """Check if video capture is opened"""
        return self.cap.isOpened()
    
    def get_frame_width(self):
        """Get width of frame"""
        return self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    
    def get_frame_height(self):
        """Get height of frame"""
        return self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    def get_video_fps(self):
        """Get FPS of video"""
        return self.cap.get(cv2.CAP_PROP_FPS)
    
    def get_current_frame(self):
        """Get current frame of video"""
        return self._current_frame
    
    def get_total_frame(self):
        return self._total_frames
    
    def release(self):
        return self._total_frames
    
    def __del__(self):
        self.release()