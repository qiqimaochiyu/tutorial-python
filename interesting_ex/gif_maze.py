#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:35:21 2018

@author: macbook
"""

import gifmaze as gm

surface = gm.GIFSurface(width=600, height=400, color_depth=2, bg_color=3)

surface.set_palette([10, 20, 30, 25,255, 255, 255, 40, 255, 50, 60, 70])

anim = gm.Animation(surface)

anim.set_control(speed=20, delay=5, trans_index=3)

maze = anim.create_maze_in_region(cell_size=5, region=8, mask=None)

from gifmaze.algorithms import prim

anim.pad_delay_frame(200)
prim(maze, start=(0, 0))
anim.pad_delay_frame(500)

surface.save('prim.gif')
surface.close()
