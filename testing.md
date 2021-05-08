# Testing

## Table of contents 
* [Homepage](#homepage)
* [Rooms](#rooms)
* [Reservation](#reservation)
* [Gallery](#gallery)
* [Tourist Info](#tourist-info)
* [My Profile](#my-profile)
* [Navigation](#navigation)
* [Social Media](#social-media)
* [Footer](#footer)
* [Reservations overview for Admin ](#reservations-overview-for-admin )



## Homepage
### **Responsiveness**
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* Quality and display of hero image
* Display of carousel  

#### Conclusion
Hero image looks nice across devices and browers. Image is of high quality.  
Carousel looks well across devices and browers.   
From small devices (from 320px onwards) until tablets, image is display above the text. Carousel resizes the height depending of the content of the slide.
Arrows to go left and right are displayed in the middle of the height of the carousel.   
On large devices, image is being displayed on the left, with the description and button on the right. 

### **Functionality**
Buttons to move left and right in the carousel work as intented.   
Disabled automatic scrolling of the carousel to give the user the control to go to the next slide.   
Indicator below carousel to let the user know how many slides there are and where user is located on that moment. 

### **Lighthouse report**
""" Include 2 image performance screenshots """  

In the beginning the performance was too low, around 60%. This was mainly caused by retrieving the images from AWS.
After some research, I have added metadata to my AWS Bucket to increase the max age for Cache Control. 
This immediately brought my perfomance up to 

### **User Experience**
#### User Story: I want the website to be visually appealing so I can already imagine myself being on holiday there
Drone image from the house with the slight overlay immediately creates a 'Wow' feeling while not overwhelming the user.
When you scroll down to the carousel, you immediately see a sneak peek from each page, give the user the feeling to 'wanting' to keep on exploring. 
This feeling I have recreated across each page in order to not lose the interest of the user. 


#### User Story: I want to have some information about the property and it's location
On the first slide of the carousel, the user can find some information about the property.  
It includes a couple of more known places closeby as well as some info about the house and when it was renovated.   
More info about the bed & breakfast is spread across the website. On the rooms page you can find more info about the rooms, amenities, breakfast, check-in & check-out and so on. 


## Rooms
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* Quality and display of all the images: hero images, room images and breakfast images
* Responsiveness of the additional information text
* Display of the different amenities and policies  

#### Conclusion
The hero image for the rooms shows nicely across the various browsers and devices. 
The image only takes up 60 vh instead of 100vh like on the homepage. This was done to not overhelm the user and already show what this page has to offer.   
When you scroll down the rooms, on large screens, you will see the images of the room on the left side, automatically scrolling through various images.
The text is nicely displayed on the right side with a call to action button to take you to the detail page of that specifc room. 
On small and medium screens, the images are displayed above the text. The rooms are divided by a subtle yellow line. 

Below the rooms the additional information text shows nicely and adjusts according the various devices and browers.
Images show nicely, are of high quality and show the user the complete experience in the bed & breakfast. 
The amenities, activities & experiences and policies are displayed in a nice list varying from 3 columns on large screens to 1 column on small screens. 

### Functionality
In order to make the page more visually appealing, I wanted the carousel for each room type to move at a different speed.
This I have done by setting the data-interval to different amount of seconds.

The buttons to take the user to the detail page of each room work well. Same counts for the buttons on the rooms detail page to take you back to the rooms page. 

### User Experience
#### User Story: I want to see which different rooms the accommodation has to offer
When the user arrives on the website, it will find its way right away to the rooms.
Or via the navigation or through the call to action button in the carousel on the homepage.  
The rooms are nicely displayed on the rooms page with sufficient information about each room.

#### User Story: I want to know what kind of amenities are included in the room
In the description of each room type, most of the specific amenities are described like the products from rituals, hairdryer etc.  
Below the rooms on this page, the user will find a long list of all the other amenities, services and facilities the bed & breakfast offers. 


## Reservation
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?

#### Conclusion


### Functionality
#### Step 1: Select check-in & check-out
* Not possible to select data in the past
* Not possible to proceed with checkout date that is before check in
* Limited reservations section to max 28 days

#### Step 2: Display available and unavailable rooms based on availability
* Ability to select multiple rooms
* Only allowed to select 1 or 2 people per room
* Search again button to go back to step 1 to change the data

#### Step 3: Show reservation overview to user + reservation form
* Overview of reservation data + room overview
* Reservation form that is prefilled when user is logged in
* Payment form not being displayed when user is the superuser

#### Step 4: Show reservation overview to user after payment was successfull. 


### User Experience
#### User Story: I want to be able to make a reservation on the website itself

#### User Story: I want to be able to choose the exact room in which I want to stay.


## Gallery
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?

#### Conclusion

### Functionality
### User Experience
#### User Story: I want to see a lot of pictures so I can really visualize the place


## Tourist Info
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?

#### Conclusion

### Functionality
### User Experience
#### User Story: I want to have some information about the surroundings of the accommodation


## My Profile 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?

#### Conclusion

### Functionality
### User Experience
#### User Story: "Still to write"


## Navigation 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?

#### Conclusion

### Functionality
* Link on homepage to reservation
* Link in carousel on homepage to other pages

### User Experience
#### User Story: I want to have an intuitive navigation so I know right away where I can find which information


## Social Media 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?

#### Conclusion 

### Functionality
### User Experience
#### User Story:


## Footer 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?

#### Conclusion

### Functionality
### User Experience
#### User Story: I want to be able to get in contact with the propery in case I have some questions

#### User Story: I want to know the address and how far / close it is to big cities

## Reservations overview for Admin 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?

#### Conclusion

### Functionality
### User Experience
#### Site owner goals: I want to be able to see all the reservations

#### Site owner goals: I want to have a seperate section for arriving and inhouse reservations

#### Site owner goals: I want to have a seperate section as well for the reservations for the next 7 days so I can plan in advance