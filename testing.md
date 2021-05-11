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

### **Lighthouse report**
""" Include 2 image performance screenshots """  

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
#### Step 1: Select check-in & check-out
* Display and quality of hero image 
* Date input in hero image + button display

#### Step 2: Display available and unavailable rooms based on availability
* Display of data information from step 1
* Display of available and unavailable rooms
* For each room, the main image will be displayed + the intro text. 


#### Step 3: Show reservation overview to user + reservation form
* Reservation overview, including small overview of the selected room
* Display of reservation form. 


#### Step 4: Show reservation overview to user after payment was successfull. 
* Display of the reservation confirmation


#### Conclusion
Hero image is of high quality and date input fields for check-in and check-out are responsive across devices. 
In order to have enough space for the reservation data, the hero image is 100vh.   
On step 2, the data from step 1 is displayed in a disabled state with a nice button to go back to step 1. 
Rooms are displayed nicely and react responsive across various browsers and devices. 
On small devices, image will be displayed on top of the text. On medium and large devices, the images will be displayed on the left of the text. 

On large devices, reservation overview on the checkout page is displayed on the left with the form on the right. 
On small and medium devices, the reservation overview is displayed on top of the form. 

On the checkout success page, the reservation overview is nicely displayed into various sections. 
The whole reservation process is responsive across browsers and devices. 

### Functionality
#### Step 1: Select check-in & check-out
* Flash message when user tries to select check-in and/or check-out data in the past
* Flash message when user tries to select check-in date after check-out date 
* Button to proceed to next step works as planned
* Limited reservations section to max 28 days ***

#### Step 2: Display available and unavailable rooms based on availability
* For each room I have selected 1 main image which is being displayed for each room
* The user is able to select multiple rooms
* The user is only allowed to select the maximum possible occupancy for each room
* Search again button to go back to step 1 to change the data

#### Step 3: Show reservation overview to user + reservation form
* Overview of reservation data + room overview
* Reservation form that is prefilled when user is logged in
* When user is not logged in, a link to register or login is being displayed below the form
* Save info functionality which saves the user info when logged in 
* Payment form not being displayed when user is the superuser, this was done to allow the property to make reservations for guests without having to go through the payment.
    This can be specifically usefull when guests would try to make a reservation by phone.

#### Step 4: Show reservation overview to user after payment was successfull. 
* Data is structured into different section which all get the correct data. 

### **Lighthouse report**
""" Include 2 image performance screenshots """  

### User Experience
#### User Story: I want to be able to make a reservation on the website itself
The user is able to make a reservation on the website. 
The reservation process is intuitive and easy to use.

#### User Story: I want to be able to choose the exact room in which I want to stay.
On step 2, the user has the choice to select the exact room he/she wants to stay. 
The user is also able to select multiple rooms.

## Gallery
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* Display and quality of the images
* Display of the modal 

#### Conclusion
Images are of high quality and display nicely on the various browsers and devices. 
In the modal, the images are increased to the real size where the quality stays intact. 
On large devices the images are displayed in 4 columns, medium devices on 2 columns and on small devices, they are displayed full width. 
The height of the images is set to auto in order not to compromise the quality of the image. 

### Functionality
In order to implement the modal to view the images on bigger size, I have used a small javascript library, called [Lightbox](https://cdnjs.com/libraries/lightbox2). 
The images are nicely displayed, using an overlay on top of the main page. It includes arrow to scroll through the images and below the images, there is a counter giving the user a sense of where they are in the gallery. 

### Lighthouse report

""" Include 2 images from report """

### User Experience
#### User Story: I want to see a lot of pictures so I can really visualize the place
In total I have displayed around 50 images from the property and the surroundings of the bed & breakfast. 
This helps the user to visualize the place and their potential upcoming stay. 


## Tourist Info
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* Display and quality of hero image
* Display of 3 main buttons to collapse out to show the recommendations
* Display of recommendation card
* Display and responsiveness of recommendation detail page 


#### Conclusion
Hero image is of high quality and displayed nicely across browsers and devices
Buttons resize correctly depending of the device. When clicked on the buttons, the cards are displayed nicely. 
On medium and large devices, they are displayed in 3 columns while on small devices they take up full width of the screen. 

On the recommendation detail page, on medium and large devices, the image is displayed nicely on the left side of the screen with the detailled info on the right.
A small introductory text is displayed on top of the image and text. 
On small devices, the introductory text is displayed on top of image.  Below the image you will find the detailled information. 


### Functionality
I have implemented a 'Add to favourites' functionality that allows the user to add a recommendation to its favourites. 
When the user adds it, the heart displays full and the recommendation will appear on the profile page of the user. 
When the user clicks on the full heart, it will be removed from the favourites and an empty heart will be displayed. 

The heart is being displayed whether the user is logged in or not, but the functionality only works when the user is logged in. 
When the user is not logged in, a modal opens up asking the user if he/she wants to register or login. 

### Lighthouse report
""" Include 2 images """

### User Experience
#### User Story: I want to have some information about the surroundings of the accommodation
The tourist information page provides a lot of information about the surroundings. 
I have split up the information into 3 different categories: places to visit, things to do & where to eat. 
This way the user can specifically scroll through the recommendations he/she is interested in. 


## My Profile 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* Quality and display of hero image 
* Display of contact information of the user + form to edit
* Display of any upcoming or past reservation for user
* Display of the recommendations added to the favourites of the user

#### Conclusion
Hero image is of high quality and displayed nicely across devices and browsers. 
On the top part of the page, on large devices, the reservations are displayed nicely in a 'box' on the left side of the screen and the contact info on the right side. 
Below the favourites are displayed into the same cards as how they are displayed on the tourist info page. 
On small and medium devices, the reservations are displayed at the top of the image with the contact details below. 
Page to update contact displays nicely on the screen. 

### Functionality
Contact information for profile, which is being used to prefill the contact form upon checkout. 
Overview of past and upcoming reservations but the option the view the confirmation page. 
The user will be taken to the checkout success page with a flash message that reminds the user that this is a past confirmation. 
Display of the recommendations that were added to the favourites of the user.

### Lighthouse report
""" Include 2 images """

### User Experience
This page / feature is not often implemented in a website for a bed & breakfast and exceeds the expectations for the user. 
This makes the booking of their holidays a nicer process because it offers a more complete experience.


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