# -*- coding: utf-8 -*-
"""
@date: Saturday, November 19th, 2022
@author: Ezekiel Zechariah Lutz
@time: 21:59:34
"""

""""""""""""""""""""""""""""""""""""
"""           Libraries          """
""""""""""""""""""""""""""""""""""""
import pandas as pd
import math
import matplotlib.pyplot as plt

""""""""""""""""""""""""""""""""""""
"""            Lists             """
""""""""""""""""""""""""""""""""""""

                                                # Creates empty lists that will be appended later on in the code. 

list_missile_position_Z = []
list_missile_position_X = []
list_missile_velocity_Z = []
list_missile_velocity_X = []
list_target_position_Z = []
list_target_position_X = []
list_target_velocity_Z = []
list_target_velocity_X = []
list_missile_heading_angle = []
list_closing_distance = []
list_missile_velocity = []
list_perpendicular_acceleration = []
list_time_since_launch= []

""""""""""""""""""""""""""""""""""""
"""     Engagement Parameters    """
""""""""""""""""""""""""""""""""""""

engagement_duration  = 120                       # Duration of the engagement, units in seconds.
dt = 0.1                                         # Delta Time (dt), represents update rate of engagement, units in seconds.
total_updates = int(engagement_duration/dt)      # Total number of updates/data points for the engagement.


    
   
""""""""""""""""""""""""""""""""""""
"""      Parameter Updates       """
""""""""""""""""""""""""""""""""""""
N = 5                                   # Navigation Gain. Sometimes called the "Proportionality Constant",  as called the "Navigation Ratio".
                                        # Unitless integer number, typically between 3-5.

missile_position_Z   =  0                   # Position of the missile in the Z-axis, units in kilometers.
missile_position_X   =  0                   # Position of the missile in the X-axis, units in kilometers.
missile_heading_angle =  1.2                # Angle between the missile velocity vector and the line of sight, units in radians.
missile_velocity   =  1.5435                # Total velocity of the missile, units in kilometers/second.
missile_velocity_Z =  missile_velocity * math.cos(missile_heading_angle)    # velocity of the missile in the Z-axis, units in kilometers/second.
missile_velocity_X =  missile_velocity * math.sin(missile_heading_angle)    # velocity of the missile in the X-axis, units in kilometers/second.


target_position_Z   =  9.144                # Position of the target in the Z-axis, units in kilometers.
target_position_X   =  150                  # Position of the target in the X-axis, units in kilometers.
target_velocity_Z  =  0.033                   # Velocity of the target in the Z-axis, units in kilometers/second.
target_velocity_X  =  0.857                 # Velocity of the target in the X-axis, units in kilometers/second.
target_velocity   = math.sqrt((target_velocity_Z**2 + target_velocity_X**2))    # Total velocity of the missile, units in kilometers/second.

# NOTE: The below are only applied if a disturbance is present in the environment, such as a strong air current that imapcts the velocity of the missile and target.

current_velocity_Z =  0.0                   # Velocity of any disturbances in the Z-axis, units in kilometers/second.
current_velocity_X =  0.0                   # Velocity of any disturbances in the X-axis, units in kilometers/second.
time_since_launch = 0                       # Time since launch of missile, unit in seconds.
  
""""""""""""""""""""""""""""""""""""
"""         Calculations         """
""""""""""""""""""""""""""""""""""""

for i in range(total_updates):
    
    time_since_launch = time_since_launch + dt                   # Updated time since launch of missile, unit in seconds.
    
    rel_pos_prev_Z = (target_position_Z - missile_position_Z)    # Previously known relative position in the interial frame in the Z-axis, units in kilometers.
    rel_pos_prev_X = (target_position_X - missile_position_X)    # Previously known relative position in the interial frame in the X-axis, units in kilometers.
    
  
    
    target_position_Z = target_position_Z + target_velocity_Z*dt # Updated Position of the target in the Z-axis, units in kilometers.
    target_position_X = target_position_X + target_velocity_X*dt # Updated Position of the target in the X-axis, units in kilometers.
    
    missile_position_Z = missile_position_Z + missile_velocity_Z*dt # Updated position of the missile in the Z-axis, units in kilometers.
    missile_position_X = missile_position_X + missile_velocity_X*dt # Updated position of the missile in the X-axis, units in kilometers.
    
    rel_pos_new_Z = (target_position_Z - missile_position_Z)    # Updated relative position in the interial frame in the Z-axis, units in kilometers.
    rel_pos_new_X = (target_position_X - missile_position_X)    # Updated relative position in the interial frame in the X-axis, units in kilometers.
    
    
    R = (((target_position_Z - missile_position_Z)**2)+((target_position_X - missile_position_X)**2))**0.5 # Closing distance to the target, defined here as the distance from the missile to the target. Units in kilometers.
    
    rel_vel_Z = (rel_pos_new_Z - rel_pos_prev_Z)/dt             # Relative velocity in the interial frame in the Z-axis, units in kilometers/second.
    rel_vel_X = (rel_pos_new_X - rel_pos_prev_X)/dt             # Relative velocity in the interial frame in the X-axis, units in kilometers/second.     
    
    Vm = math.sqrt(missile_velocity_Z**2 + missile_velocity_X**2)  # Velocity of the missile, in kilometers/second.
    
    lamba = math.atan2(rel_pos_new_X, rel_pos_new_Z)            # Line-of-Sight (LOS) angle, units in radians.
    
    lamba_dot = ((rel_pos_new_Z*rel_vel_X) - (rel_pos_new_X*rel_vel_Z))/(R**2) # LOS angle rate, the derivative with respect to time of LOS angle. Units in radians/second.
    
    ap = N * Vm * lamba_dot                                     # The overall equation for Pure Proportional Navigation, units in kilometer-radians/second-squared.
    
    
    """"""""""""""""""""""""""""""""""""
    """      Parameter Updates       """
    """"""""""""""""""""""""""""""""""""
    
    missile_position_Z = (missile_position_Z) + (missile_velocity_Z*dt) + (current_velocity_Z*dt)   #Updated missile position in the Z-axis, units in kilometers.
    missile_position_X = (missile_position_X) + (missile_velocity_X*dt) + (current_velocity_X*dt)   #Updated missile position in the X-axis, units in kilometers.
        
    
    Za = -ap * math.sin(missile_heading_angle)                 # Acceleration command to be applied normal to the missile's velocity vector in the Z-axis, units in kilometers/second-squared.
    Xa =  ap * math.cos(missile_heading_angle)                 # Acceleration command to be applied normal to the missile's velocity vector in the X-axis, units in kilometers/second-squared. 
        
    
    missile_velocity_Z = missile_velocity_Z+ Za*dt         # Updated velocity of the missile in the Z-axis, units in kilometers/second.
    missile_velocity_X = missile_velocity_X+ Xa*dt         # Updated velocity of the missile in the Z-axis, units in kilometers/second.
        
    missile_heading_angle = math.atan2(missile_velocity_X, missile_velocity_Z)      # Updated missile heading_angle, units in radians.
        
    target_position_Z = target_position_Z + target_velocity_Z*dt + current_velocity_Z*dt    #Updated missile position in the Z-axis, units in kilometers.
    target_position_X = target_position_X + target_velocity_X*dt + current_velocity_X*dt    #Updated missile position in the X-axis, units in kilometers.
    
    #The commands below append various lists with the value for several variables of interest for each iteration. 
    
    list_missile_position_Z.append(missile_position_Z)
    list_missile_position_X.append(missile_position_X)
    list_missile_velocity_Z.append(missile_velocity_Z)
    list_missile_velocity_X.append(missile_velocity_X)
    list_target_position_Z.append(target_position_Z)
    list_target_position_X.append(target_position_X)
    list_target_velocity_Z.append(target_velocity_Z)
    list_target_velocity_X.append(target_velocity_X)
    list_missile_heading_angle.append(missile_heading_angle)
    list_closing_distance.append(R)
    list_missile_velocity.append(Vm)
    list_perpendicular_acceleration.append(ap)
    list_time_since_launch.append(time_since_launch)
    
    distance_check = math.isclose(R, 0, abs_tol=0.2)      # Creates a "check" variable to see if the closing distance from the missile to the target is less than 1 meter. 
    
    if distance_check == True:                          # If the distance from the missile to the target is within 400 meters, the missile "detonates" and the simulation ends.   
        print("BOOM!")
        break

""""""""""""""""""""""""""""""""""""
"""         DataFrames           """
""""""""""""""""""""""""""""""""""""
    
# Converts the lists used to hold various variables of interest during the engagement into dataframes.

df_missile_position_Z = pd.DataFrame(list_missile_position_Z, columns=['Missile Z-Axis Position (km)'])
df_missile_position_X = pd.DataFrame(list_missile_position_X, columns=['Missile X-Axis Position (km)'])
df_missile_velocity_Z = pd.DataFrame(list_missile_velocity_Z, columns=['Missile Z-Axis Velocity (km/s)'])
df_missile_velocity_X = pd.DataFrame(list_missile_velocity_X, columns=['Missile X-Axis Velocity (km/s)'])
df_target_position_Z = pd.DataFrame(list_target_position_Z, columns=['Target Z-Axis Position (km)'])
df_target_position_X = pd.DataFrame(list_target_position_X, columns=['Target X-Axis Position (km)'])
df_target_velocity_Z = pd.DataFrame(list_target_velocity_Z, columns=['Target Z-Axis Velocity (km/s)'])
df_target_velocity_X = pd.DataFrame(list_target_velocity_X, columns=['Target X-Axis Velocity (km/s)'])
df_missile_heading_angle = pd.DataFrame(list_missile_heading_angle, columns=['Missile Heading Angle (rad)'])
df_closing_distance = pd.DataFrame(list_closing_distance, columns=['Closing Distance (km)'])
df_missile_velocity = pd.DataFrame(list_missile_velocity, columns=['Missile Velocity (km/s)'])
df_perpendicular_acceleration = pd.DataFrame(list_perpendicular_acceleration, columns=['Normal Acceleration (km*rad/s²)'])
df_time_since_launch = pd.DataFrame(list_time_since_launch, columns=['Time since Missile Launch (s)'])


# Joins all dataframes to a master dataframe.
df_master = df_time_since_launch.join(df_missile_position_Z, how='outer')
df_master = df_master.join(df_missile_position_X, how='outer')
df_master = df_master.join(df_closing_distance, how='outer')
df_master = df_master.join(df_target_position_Z, how='outer')
df_master = df_master.join(df_target_position_X, how='outer')
df_master = df_master.join(df_missile_velocity, how='outer')
df_master = df_master.join(df_missile_velocity_Z, how='outer')
df_master = df_master.join(df_missile_velocity_X, how='outer')
df_master = df_master.join(df_target_velocity_Z, how='outer')
df_master = df_master.join(df_target_velocity_X, how='outer')
df_master = df_master.join(df_missile_heading_angle, how='outer')
df_master = df_master.join(df_perpendicular_acceleration, how='outer')


""""""""""""""""""""""""""""""""""""
"""       Export to Excel        """
""""""""""""""""""""""""""""""""""""

# Outputs the master dataframe to an excel spreadsheet that can be reviewed.
                                                              
df_master.to_excel('engagement_file.xlsx', index = False)       


""""""""""""""""""""""""""""""""""""
"""        Plot Creation         """
""""""""""""""""""""""""""""""""""""


fig = plt.plot(list_target_position_X, list_target_position_Z, color='royalblue'), plt.plot(list_missile_position_X, list_missile_position_Z, color='red'), plt.plot(list_missile_position_X[0], list_missile_position_Z[0], color='red', marker='^', markersize='10'), plt.plot(list_target_position_X[0], list_target_position_Z[0], color='royalblue', marker='s', markersize='10'), plt.plot(list_missile_position_X[-1], list_missile_position_Z[-1], color='gold', marker='*', markersize='15'), plt.plot(list_missile_position_X[-1], list_missile_position_Z[-1], color='gold', marker='x', markersize='20')
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")     
plt.ylabel('Altitude (km)')
plt.xlabel('Range (km)')
plt.title('Simulated Engagement')
plt.legend(['Target Aircraft', 'SAM'], loc='lower right')
plt.savefig('Engagement Scenario.jpg', bbox_inches='tight')
plt.show()