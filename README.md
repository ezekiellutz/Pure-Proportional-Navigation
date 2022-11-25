# Pure Proportional Navigation (PPN)
A model that simulates the applications for Proportional Navigation and how it operates in real-world environments.

# Installation Instructions
Download the .py file and place to your directory of choice on the host PC. It is reccommended that the file be run in its own folder, as the model will output both an .xlsx file in addition to a .jpg file. Run the file from your IDE of choice. The model can be easily modified to get a better understanding of how proportional navigation works. Simply modify the starting variables to see the effect they have on the model. 

It is recommended that this model be run in Spyder 5.1.5 [conda (Python 3.9.7)]. 

# Purpose Disclaimer
The contents of this GitHub repository, including but not limited to the pure_pro_navigation.py, Engagement Scenario.jpg, and engagement_file.xlsx files, were created for educational purposes only. The purpose of this model is to illustrate the guidance laws, physics concepts, and mathematical equations that go into making a PPN model. Any usage of the contents of this GitHub repository (as defined previously) outside of these educational purposes is strictly prohibited. 

# What is Proportional Navigation?
Proportional Navigation, (PN or Pro-Nav), is a guidance law employed by some surface-to-air missiles to guide a missile to an intended target. Pro-Nav is based on the fact that two objects are on a collision course with each other when their direct line-of-sight does not change direction as their closing distance approaches zero. With Pro-Nav, the acceleration vector of the missile is always perpendicular to the missile's instantaneous velocity vector. This differs from Pro-Nav's predecessor (Pursuit Guidance), in which the acceleration vector of the missile was always pointed towards the target. Because Pro-Nav's acceleration vector is perpendicular to the instantaneous velocity vector, the missile can calculate a point-of-intercept for itself and the target. This distinction makes Pro-Nav the superior guidance of choice for missiles seeking to reach their target much faster than if they used Pursuit Guidance.



![Screenshot 2022-11-24 235259](https://user-images.githubusercontent.com/83550613/203910763-5e499967-b767-40e8-a003-c37dd4724d57.jpg)



It is important to note that there are several variations of Pro-Nav that exist. The most notable being Simple Pro-Nav (SPN), Pure Pro-Nav (PPN), True Pro-Nav (TPN), and Augmented Pro-Nav (APN). The model defined in this repository models PPN, which is often cited as one of the best versions of Pro-Nav (being second to APN).
