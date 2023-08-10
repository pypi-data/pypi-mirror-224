#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.animation import FuncAnimation, PillowWriter 
from matplotlib import cm

import pandas as pd
import numpy as np
from tqdm import tqdm
from random import *
import random
import os #os, ramdom의 경우 기본적으로 주어지기 때문에 setup.py에 하지 않는다.
import warnings

from celluloid import Camera
import seaborn as sns


# In[13]:


warnings.filterwarnings(action='ignore') 


# ## data

# In[15]:


# change path to relative path - only for publishing

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

space_no_ent = pd.read_excel("./sampleData/exp_space2.xlsx", header = None)
space_ent = pd.read_excel("./sampleData/exp_space3.xlsx", header = None)


# In[53]:


def makeSpace(space_x = 10, space_y = 10, DFMap = [None], obstacles = None, chairs = None, FDD = False, entrance = None): #default: x, y = 20m
    '''
    to make indoor space for simulation
    0: none
    1: obstacle
    2: chair
    3: entrance
    
    Parameters
    ----------
    space_x: indoor x size
    space_y: indoor y size
    DFMap: dataframe displaying map
    obstacles: the number of obstacles
    chairs: the number of chairs
    FDD: print FDD (Flow Disturbance Degree) or not
    entrance: location and size of entrance e.g., {'x': [15,15], 'y': [0,3]} -> x: 15 to 15, y: 0 to 3

    Returns
    -------
    DataFrame
        A comma-separated values (csv) file is returned as two-dimensional
        data structure with labeled axes.

    Numeric value
    list

    Examples
    --------
    -- with data --
    >>> space, FDD = makeSpace(DFMap= space_no_ent, FDD = True) # without space
    >>> space, entrance, FDD = makeSpace(DFMap= space_ent, FDD = True) # with space
    
    -- without data --
    >>> space = makeSpace(space_x = 10, space_y = 10) # no obstacle
    >>> space, obstacles_loc = makeSpace(space_x = 10, space_y = 10, obstacles= 10) # deploy obstacles
    >>> space, obstacles_loc = makeSpace(space_x = 10, space_y = 10, obstacles = 10, chairs = 5) # with chairs
    >>> space, entrance, FDD, obstacles_loc = makeSpace(space_x= 15, space_y = 10, obstacles= 10, FDD = True, entrance = {'x': [15,15], 'y': [0,3]}) # with entrance code
    
    '''
    
    
    
    Columns = []
    #print(len(DFMap))
    
    if(len(DFMap) > 1): # if there is Dataframe
        # Identify entrance and extract where. After that, delete entrance from DF and declare space that equals to DF.
        
        # 1) entrance가 DF에 이미 있을 떄. -> entrance_range를 정한다.
               
        if entrance == None: #entrance is entered
            space = DFMap
            entrance = []
            
            for i in range(len(DFMap)):  #len space: space_y / count tem_obstacles until < obatacles
                for j in range(len(DFMap.columns)):
                    if DFMap.iloc[i,j] == 3:
                        entrance.append([j,(-(i -(len(space)-1)))])
                        
            #set entrance_range as a group
            entrance_group = []
            entrance_range = []
            if len(entrance) > 0:
                entrance_group.append(entrance[0]) #initial entrance group member

            for i, ent in enumerate(entrance): 
            #     print(ent)
                if len(entrance)-1 > i:
                    if (abs(ent[0] - entrance[i+1][0]) < 2) and (abs(ent[1] - entrance[i+1][1]) < 2) : # connected Entrance
                        entrance_group.append(entrance[i+1])
                    else:   #no connectedprint
                        entrance_range.append(entrance_group)
                        entrance_group = [entrance[i+1]]
                else: #last one
                    entrance_range.append(entrance_group)
                        
        else:
            space = DFMap
            entrance_range = [entranceRange(entrance, space)]
        
        # 2) entrance가 DF에 없고 manyally하게 주어졌을 때, -> entrance_range = entranceRange(entrance, space) -> 이건 default. 이미 되어 있음.
        # 3) entrance가 DF에 없고 entrance도 manually하게 안 주어졌을 때. -> 이때는 entrance가 없이 simulation하는 것. -> entrance = [] -> 이것도
    else: #No DFMap
        
        #DF가 안주어짐.
        #1) entrance가 manually하게 주어졌을 때, entrance_range = entranceRange(entrance, space) -> 이미 되어 있음.
        #2) entrance가 안주어졌을 때, 입구가 없이 하는 것. -> entrance = [] -> 이미 되어 있음.
        
        
        for i in range(space_y):      # columns
            Columns.append(0)
        oneCol = pd.DataFrame(Columns)
        space = pd.DataFrame(Columns)

        for j in range(space_x-1):      # rows
            space = pd.concat([space, oneCol], axis = 1)    
    
        #Entrance Range
        entrance_range = [entranceRange(entrance, space)]
        #print('entrance_range: ', entrance_range)
    
    if obstacles != None:     #If users want to put obstacles
        space, obstacles_loc = putObstacles(space, obstacles, entrance_range)
        #print("obstacles_loc: ", obstacles_loc)
    
    if chairs != None: #if users want to put chairs
        space = putChairs(space, chairs, obstacles_loc, entrance_range )
    
    if FDD == True: #여기에 Chair도 고려
        FDD_computed = computeFDD(space)
        #print("FDD: ", FDD_computed)
    
    if entrance_range == [] or entrance_range == [[]]: #No Entrance_range
        if FDD == True and obstacles == None:
            return space, FDD_computed
        elif FDD == True and obstacles != None:
            return space, FDD_computed, obstacles_loc
        elif FDD == False and obstacles != None:
            return space, obstacles_loc
        else:
            return space
    else:
        #for ent in entrance_range:  #entrance 2 넣어주기
        #    space.iloc[ent[1], ent[0]] = 2
        # 다시 entrance range 원래대로
        if len(entrance_range) == 1: #one entrance
            for ent in entrance_range[0]:
                ent[1] = -(ent[1] - (len(space)-1)) 
            entrance_range.sort()
        else: #multiple entrance
            None
            
        if FDD == True and obstacles == None:
            return space, entrance_range, FDD_computed
        elif FDD == True and obstacles != None:
            return space, entrance_range, FDD_computed, obstacles_loc
        elif FDD == False and obstacles != None:
            return space, entrance_range, obstacles_loc
        else:
            return space, entrance_range
    
    # put obstacles
    
def entranceRange(entrance, space):
    if entrance == None:
        entrance_range = []
    else:
        entrance['y'][0] = -(entrance['y'][0] - (len(space)-1)) #y는 반대로
        entrance['y'][1] = -(entrance['y'][1] - (len(space)-1))
        entrance['y'].sort()

        entrance_range = [] #entrance_range 설정
        #print(entrance['y'][0], entrance['y'][1])
        for x in range(entrance['x'][0], entrance['x'][1]+1):
            for y in range(entrance['y'][0], entrance['y'][1]+1):
                entrance_range.append([x,y])    
    
    return entrance_range    

def putObstacles(space, obstacles, entrance_range): #N of obstacles
    space_y = len(space)
    space_x = len(space.columns)
    
    tem_obstacles = 0 #temporal number of obstacles
    obstacles_loc = [] #obstacle locations
    
    def randObs():
        obs_x = randint(0, space_x-1)  # random integer from 0 to space_x
        obs_y = randint(0, space_y-1)
        return obs_x, obs_y
        
    while tem_obstacles < obstacles:
        tem_obstacles = 0

        obs_x, obs_y = randObs()
        #print("entrance_range: ", entrance_range)
        #print(obs_x, obs_y)

        while(True): #if obs_xy is in entrance_range: reassign
            if [obs_x, obs_y] in entrance_range:
                obs_x, obs_y = randObs()
            else:
                break
        
        space.iloc[obs_y, obs_x] = 1 #mark 1 as obstacle
        obstacles_loc.append([obs_x, obs_y]) #location
        
        for i in range(len(space)):  #len space: space_y / count tem_obstacles until < obatacles
            for j in range(len(space.columns)):
                if space.iloc[i,j] == 1:
                    tem_obstacles = tem_obstacles + 1
                    
    return space, obstacles_loc


def putChairs(space, chairs, obstacles_loc, entrance_range): #N of chairs
    space_y = len(space)
    space_x = len(space.columns)
    
    tem_chairs = 0 #temporal number of obstacles
    
    def randChairs():
        chair_x = randint(0, space_x-1)  # random integer from 0 to space_x
        chair_y = randint(0, space_y-1)
        return chair_x, chair_y
    
    def randObs():
        obs_x = randint(0, space_x-1)  # random integer from 0 to space_x
        obs_y = randint(0, space_y-1)
        return obs_x, obs_y
    
    while tem_chairs < chairs:
        tem_chairs = 0

        chair_x, chair_y = randChairs()
        #print("entrance_range: ", entrance_range)
        #print(obs_x, obs_y)

        while(True): #if obs_xy is in entrance_range: reassign
            if [chair_x, chair_y] in entrance_range or [chair_x, chair_y] in obstacles_loc: #there should be no entrance and obstacles
                chair_x, chair_y = randObs()
            else:
                break
        
        space.iloc[chair_y, chair_x] = 2 #mark 2 as chair
        
        for i in range(len(space)):  #len space: space_y / count tem_obstacles until < obatacles
            for j in range(len(space.columns)):
                if space.iloc[i,j] == 2:
                    tem_chairs = tem_chairs + 1
                    
    return space

def computeFDD(space):
    space_y = len(space)
    space_x = len(space.columns)
    
    def compute_process(n):
        tem_list = []
        line_list = []
        composite_tem_list = []
        passages = 0
        passage_area = 0

        # Quentify passages
        if(n == 1):
            for i in range(space_y):
                for j in range(space_x):

                    if(space.iloc[i,j] == 1):
                        #print("obstacles: :", j,i)
                        line_list.append(tem_list)
                        tem_list = []
                    else:
                        passage_area = passage_area + 1
                        tem_list.append(j)

                line_list.append(tem_list)
                composite_tem_list.append(line_list)
                tem_list = []
                line_list = []

        else:
            for i in range(space_x):
                for j in range(space_y):

                    if(space.iloc[j,i] == 1):
                        #print("obstacles: :", j,i)
                        line_list.append(tem_list)
                        tem_list = []
                    else:
                        passage_area = passage_area + 1
                        tem_list.append(j)

                line_list.append(tem_list)
                composite_tem_list.append(line_list)
                tem_list = []
                line_list = []


        for i in range(len(composite_tem_list)):
            composite_tem_list[i] = list(filter(None, composite_tem_list[i]))    
            if i == 0:
                passages = passages + len(composite_tem_list[i])
                #print("passages: " , passages)
            else:
                temporal_list = composite_tem_list[i] + composite_tem_list[i-1]
                #print('temporal', temporal_list)
                #print(temporal_list)
                temporal_result = []
                for value in temporal_list:           #위에서부터 쭉 scan. 두줄씩 짝지어서 중복을 제거하여 result에 넣음
                    if value not in temporal_result:
                        temporal_result.append(value)
                #print("composite_tem_list: ", len(composite_tem_list[i]))        
                #print("temporal_list: ", len(temporal_list))
                #print("temporal_result: ", len(temporal_result))
                passages = passages + len(composite_tem_list[i]) - (len(temporal_list) - len(temporal_result))          #현재 한 줄의 개수에서 중복제거한 개수를 뺌.
                #print("passages: " , passages)
                temporal_list = []
                temporal_result = []

        #compute fdd
        fdd = 1 - (passage_area/passages/(space_x*space_y))
        #print("process: ", n, ", number of passages: ", passages, ",fdd = ", fdd)
        return fdd

    fdd1 = compute_process(1)   #1 - from rows to columns
    fdd2 = compute_process(2)   #2 - from columns to rows

    if(fdd1 > fdd2):   #smaller fdd is selected
        fdd = fdd2
    else:
        fdd = fdd1

    #print("fdd = ", fdd)
        
    
    return fdd
    
    


