# Pure Proportional Navigation (PPN)
A model that simulates the applications for Proportional Navigation and how it operates in real-world environments.

# Installation Instructions
Download the .py file and place to your directory of choice on the host PC. It is recommended that the file be run in its own folder, as the model will output both an .xlsx file in addition to a .jpg file. Run the file from your IDE of choice. The model can be easily modified to get a better understanding of how proportional navigation works. Simply modify the starting variables to see the effect they have on the model. 

It is recommended that this model be run in Spyder 5.1.5 [conda (Python 3.9.7)]. 

# Purpose Disclaimer
The contents of this GitHub repository, including but not limited to the pure_pro_navigation.py, Engagement Scenario.jpg, and engagement_file.xlsx files, were created for educational purposes only. The purpose of this model is to illustrate the guidance laws, physics concepts, and mathematical equations that go into making a PPN model. Any usage of the contents of this GitHub repository (as defined previously) outside of these educational purposes is strictly prohibited. This includes any derivative works.

# What is Proportional Navigation?
Proportional Navigation, (Pro-Nav), is a guidance law employed by some surface-to-air and air-to-air missiles to guide a missile to an intended target. Pro-Nav is based on the fact that two objects are on a collision course with each other when their direct line-of-sight does not change direction as their closing distance approaches zero. With Pro-Nav, the acceleration vector of the missile is always perpendicular to the missile's instantaneous velocity vector. This differs from Pro-Nav's predecessor (Pursuit Guidance), in which the acceleration vector of the missile was always pointed towards the target. Because Pro-Nav's acceleration vector is perpendicular to the instantaneous velocity vector, the missile can calculate a point-of-intercept for itself and the target. This distinction makes Pro-Nav a superior form of guidance, as it allows the missile the ability create a collison course predictively, rather than reactively.

While several different variations of Pro-Nav exist, the type of Pro-Nav modeled here is called Pure Pro-Nav (PPN). While there is a great deal of nomenclature differences between how Pro-Nav is defined in various circles, it is universally agreed upon that the method for determining the acceleration vector is the defining feature for whether a particular Pro-Nav variant is classified as Pure Pro-Nav, True Pro-Nav, Simple Pro-Nav, etc. The model created here defines the acceleration vector normal to the velocity vector as: 

![screen_0](https://user-images.githubusercontent.com/83550613/204161862-dca88b50-5bf8-4b14-8985-d71a7d6a9ec6.jpg)


# How Pure Proportional Navigation (PPN) Works:

Ultimately, the goal in any Pro-Nav model is to quantify the value for the acceleration vector normal to the velocity vector. In order to do this for the PPN model created here, the velocity of the missile, the line-of-sight rate, and the navigational gain must be quantified.

At the start of an engagement, PPN requires that you know the value of sseveral different parameters at the time of launch. A list of these known parameters is shown below:

![screen_1](https://user-images.githubusercontent.com/83550613/204120176-5e495efb-e917-4d59-963e-930c8a4aa1c0.jpg)


With the above information known, the first order of business is to calculate the position of the missile relative to the target given the last known coordinates of the missile and target. The relative position must be found in each axis, which can be solved for given the following:

![screen_2](https://user-images.githubusercontent.com/83550613/204120180-bcd8fd53-e2fa-410e-89a7-79e89c7cc283.jpg)

And similarly, in the X-axis:

![screen_3](https://user-images.githubusercontent.com/83550613/204120190-17f9c39a-9d7b-4002-9e67-b1b87ea99706.jpg)

At this point we have calculated the relative position of the missile to the target, however this was at the previous update with respect to time. From this point forward, this relative position will be referred to as the "old" relative position of the missle to the target. The reasons for this will become apparent momentarily.

In order to proceed, we need to know the new relative position of the missile to the target. In order to get this, we must now re-perform the calculations done in Figures 2a and 2b, albeit with the new target and missile position. In order to obtain the new position of the target and the missile, we can calculate it by doing the following: 

![screen_4](https://user-images.githubusercontent.com/83550613/204145068-54d82259-2523-4843-94ce-6f6ca23254f3.jpg)

And similarly, in the X-axis:

![screen_5](https://user-images.githubusercontent.com/83550613/204145091-f17d906d-cb53-4feb-8ad7-df3bc7bce471.jpg)

It should be noted that, when calculating the new position of the missile, the equations shown in Figures 3a and 3b are applicable to the missile as well. Simply replace the target positions and velocity for the missile position and velocity and the necessary values will be obtained. Remember that the values obtained here are the "new" target and missile positions. 

With the new target and missile positions obtained, the equation used in Figures 2a and 2b can be used to obtain the new relative position of the missile to the target. With this now obtained, we can calculate the closing distance between the missile and the target using the following equation:

![screen_6](https://user-images.githubusercontent.com/83550613/204160692-34fa9f56-f331-4bdf-a10c-164c94fd630f.jpg)

With the closing distance now known, the relative velocity of the missile to the target must be calculated. This can be calculated by doing the following:

![screen_7](https://user-images.githubusercontent.com/83550613/204161335-f2bb932c-d557-4528-8b6a-d35944aa37c2.jpg)

And similarly, in the X-axis:

![screen_8](https://user-images.githubusercontent.com/83550613/204161338-df833741-8760-4783-9f10-fd1e2274b4de.jpg)

With the relative velocity of the missile to the target now known, the Line-of-Sight Rate (LoS Rate) can be calculated. This can be calculated by doing the following:

![screen_9](https://user-images.githubusercontent.com/83550613/204161733-1a718eb8-3409-49b5-a1e7-58bbdb00c745.jpg)

With the LoS Rate now quantified, the acceleration vector normal to the velocity vector can finally be calculated by doing the following:

![screen_10](https://user-images.githubusercontent.com/83550613/204162318-d8b8ca64-7370-4aac-a69e-50a261dc0303.jpg)

Now that the acceleration vector has been defined, several parameters of the missle will need to be updated 

# Acknowledged Limitations of the Model 
Like every mathematical model and simulation, the model for PPN created here is not perfect. There are multiple author-acknowledged limitations of the model including, but not limited to, the following:

1.) The model assumes that the acceleration of the missile is instantaneous. In reality, there would be two accelerations acting on the missile at the very beginning of the engagement. One acceleration vector would point in the direction of the missile's instantaneous velocity vector, and one perpendicular to the instantaneous velocity vector. Once the missile reaches cruising velocity, only one acceleration vector would remain for the remainder of the engagement.

2.) The model assumes both the missile and the target are weightless. In reality, the mass of both plays a non-trivial role in the physics behind the engagement, as well as the viability of the flight profile given the commanded acceleration by the missile and its ability to execute those accelerations 

3.) The model assumes that the target does not accelerate at all following launch. The target does not attempt evasive maneuvers and maintains a constant velocity at all times. Because the acceleration of the target is zero, the model here could technically be considered an Augmented Proportional Navigation (APN) model.  

4.) The model is 2-dimensional and simulates motion only in the X and Z axes. In reality, all 3 axes would need to be modeled and the mathematics to support this becomes more complex.  

# Bibliography

[1] Macfadzean, Robert H. M. “Section 5.4: Proportional Navigation.” Surface-Based Air Defense System Analysis, edited by Robert H. M. Macfadzean, Artech House, Inc., Norwood, MA, 1992, pp. 145–156. 

[2] “Proportional Navigation.” Wikipedia, Wikimedia Foundation, 18 Oct. 2022, https://en.wikipedia.org/wiki/Proportional_navigation#cite_note-1. 

[3] Yanushevsky, Rafael. Modern Missile Guidance. CRC Press, 2008. 
