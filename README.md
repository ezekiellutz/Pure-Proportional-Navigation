# Pure Proportional Navigation (PPN)
A model that simulates the applications for Proportional Navigation and how it operates in real-world environments.

# Installation Instructions
Download the .py file and place to your directory of choice on the host PC. It is reccommended that the file be run in its own folder, as the model will output both an .xlsx file in addition to a .jpg file. Run the file from your IDE of choice. The model can be easily modified to get a better understanding of how proportional navigation works. Simply modify the starting variables to see the effect they have on the model. 

It is recommended that this model be run in Spyder 5.1.5 [conda (Python 3.9.7)]. 

# Purpose Disclaimer
The contents of this GitHub repository, including but not limited to the pure_pro_navigation.py, Engagement Scenario.jpg, and engagement_file.xlsx files, were created for educational purposes only. The purpose of this model is to illustrate the guidance laws, physics concepts, and mathematical equations that go into making a PPN model. Any usage of the contents of this GitHub repository (as defined previously) outside of these educational purposes is strictly prohibited. 

# What is Proportional Navigation?
Proportional Navigation, (Pro-Nav), is a guidance law employed by some surface-to-air and air-to-air missiles to guide a missile to an intended target. Pro-Nav is based on the fact that two objects are on a collision course with each other when their direct line-of-sight does not change direction as their closing distance approaches zero. With Pro-Nav, the acceleration vector of the missile is always perpendicular to the missile's instantaneous velocity vector. This differs from Pro-Nav's predecessor (Pursuit Guidance), in which the acceleration vector of the missile was always pointed towards the target. Because Pro-Nav's acceleration vector is perpendicular to the instantaneous velocity vector, the missile can calculate a point-of-intercept for itself and the target. This distinction makes Pro-Nav a superior form of guidance, as it allows the missile the ability create a collison course predictively, rather than reactively.

While several different variations of Pro-Nav exist, the type of Pro-Nav modeled here is called Pure Pro-Nav (PPN). 

# How Pure Proportional Navigation (PPN) Works:



![Screenshot 2022-11-24 235259](https://user-images.githubusercontent.com/83550613/203910763-5e499967-b767-40e8-a003-c37dd4724d57.jpg)

![Untitled](https://user-images.githubusercontent.com/83550613/204049827-25c9a2d0-66cf-4fcf-a390-f562ff889d1e.png)


#Limitations of the Model (WIP

1.) Assumes that the acceleration of the missile is instantaneous
2.) Does not model the masses of the 
3.) Assumes that the target does not maneuver after missile launch
4.) Only models motion in 2 mutually perpendicular axes. 

# Bibliography

[1] Macfadzean, Robert H. M. “Section 5.4: Proportional Navigation.” Surface-Based Air Defense System Analysis, edited by Robert H. M. Macfadzean, Artech House, Inc., Norwood, MA, 1992, pp. 145–156. 
[2] “Proportional Navigation.” Wikipedia, Wikimedia Foundation, 18 Oct. 2022, https://en.wikipedia.org/wiki/Proportional_navigation#cite_note-1. 
[3] Yanushevsky, Rafael. Modern Missile Guidance. CRC Press, 2008. 
