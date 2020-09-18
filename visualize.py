#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:19:15 2020

@author: sourabh
"""
import numpy as np
import cv2
import os
import multiview
import pcd
import matplotlib.pyplot as plt

class Visualize():
    
    def __init__(self):
        self.mv = multiview.MultiView()
        self.pcd = pcd.PCD()
    
    
    def birds_eye_view(self,trajectory_history, path="./",thickness=3,show=False):
        trajectory = (trajectory_history[:,0]*3).reshape(-1,1)
        trajectory = np.hstack([trajectory, (trajectory_history[:,2]*3).reshape(-1,1)])
        trajectory = (np.int_(trajectory))//3
        min_horiz = min(trajectory[:,0])
        max_horiz = max(trajectory[:,0])
        min_vertical = min(trajectory[:,1])
        max_vertical = max(trajectory[:,1])
        trajectory_plot = np.zeros((abs(min_vertical)+abs(max_vertical)+50,abs(min_horiz)+abs(max_horiz)+50,3))
        trajectory[:,0] += abs(min_horiz)+25
        trajectory[:,1] += abs(min_vertical)+25
        trajectory_plot[trajectory[:,1],trajectory[:,0]] = 255
        kernel = np.ones((thickness,thickness),np.uint8)
        trajectory_plot = cv2.dilate(trajectory_plot,kernel,iterations = 1)
        cv2.circle(trajectory_plot, (trajectory[0][0], trajectory[0][1]) ,1, (0,255,0), thickness*2);     
        cv2.circle(trajectory_plot, (trajectory[-1][0], trajectory[-1][1]) ,1, (0,0,255), thickness*2)
        if show:
            plt.imshow(trajectory_plot)
            plt.axis('off')
            plt.show()
            # plt.pause(0.1)
            return
        cv2.imwrite(os.path.join(path,"trajectory.jpg"), trajectory_plot)
        
        

        
        
        
        
        
        
        
        
        
        
        