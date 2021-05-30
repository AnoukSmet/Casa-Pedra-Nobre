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
* [Reservations overview for Admin ](#reservations-overview-for-admin)


All the html files have been passed without any issue through the [HTML Validator](https://validator.w3.org/).
All the css files have been passed without any issue through the [CSS Validator](https://jigsaw.w3.org/css-validator/).
All the javascript files have been passed without any issue throught the [Javascript Validator](https://jshint.com/).


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
Button 'Book now' within hero image works as planned and takes the user to the reservation page.
Buttons to move left and right in the carousel work as intented.   
Disabled automatic scrolling of the carousel to give the user the control to go to the next slide.   
Indicator below carousel to let the user know how many slides there are and where user is located on that moment. 
Link within the carousel work as planned and redirects the user to the corresponding page.

Due to the image being full view height, the user might not realize there is more information on this page.
To make this clear to the user, I have added a small arrow, pointing down, right below the book now button.
The user can also click on this button which will take him/her to the carousel down on the page.

### **Lighthouse report**
#### Homepage Desktop
![Lighthouse report Desktop Home](/images-readme/home-desktop.png)
#### Homepage Mobile
![Lighthouse report Mobile Home](/images-readme/home-mobile.png)

In the beginning the performance was too low, around 60%. This was mainly caused by retrieving the images from AWS.
After some research, I have added metadata to my AWS Bucket to increase the max age for Cache Control. 
This immediately brought my perfomance up to 81%.

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
#### Rooms Desktop
![Lighthouse report Desktop Rooms](/images-readme/rooms-desktop.png)
#### Rooms Mobile
![Lighthouse report Mobile Rooms](/images-readme/rooms-mobile.png)

#### Room Detail Desktop
![Lighthouse report Desktop Room Detail](/images-readme/rooms-detail-desktop.png)
#### Room Detail Mobile
![Lighthouse report Mobile Room Detail](/images-readme/rooms-detail-mobile.png)

### User Experience
#### User Story: I want to see which different rooms the accommodation has to offer
When the user arrives on the website, it will find its way right away to the rooms page.
User can go via the navigation or through the call to action button in the carousel on the homepage.  
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
* Check out date automatically updates when user fills in check in date to check in date + 1
* Button to proceed to next step works as planned
* Limited reservations section to maximum 28 days

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
* User is allowed to fill in numbers as well as letters on ETA field. This allow answers like 'Between 14h00 and 15h00'

#### Step 4: Show reservation overview to user after payment was successfull. 
* Overview of reserved room is being displayed with the relevant information concerning the reservations
* Policies are correctly being displayed to remind guests


For the reservation procedure, they are still quite some points of improvement that I see for the future. 
Currently this website is very weak for overbooking possibilities. Ideally right before the payment is taken, an additional check in database should be performed.
This to prevent that the booking can go through while it might be booked by someone else 2 minutes before. 

What would be convenient for the future as well, is that when the user fills in check-in and check-out date and selects a room, that this room would be reserved for about 10/15 minutes.
This reduces the chance that the room wouldn't be available anymore upon checkout. 

### **Lighthouse report**

#### Reservation step 1 Desktop
![Lighthouse report Desktop Reservation Step 1](/images-readme/reservation-step-1-desktop.png)
#### Reservation step 1 Mobile
![Lighthouse report Mobile Reservation Step 1](/images-readme/reservation-step-1-mobile.png)

#### Reservation step 2 Desktop
![Lighthouse report Desktop Reservation Step 2](/images-readme/reservation-step-2-desktop.png)
#### Reservation step 2 Mobile
![Lighthouse report Mobile Reservation Step 2](/images-readme/reservation-step-2-mobile.png)

#### Checkout Desktop
![Lighthouse report Desktop Checkout](/images-readme/checkout-desktop.png)
#### Checkout Mobile
![Lighthouse report Mobile Checkout](/images-readme/checkout-mobile.png)

#### Checkout Success Desktop
![Lighthouse report Desktop Checkout Success](/images-readme/checkout-success-desktop.png)
#### Checkout Success Mobile
![Lighthouse report Mobile Checkout Success](/images-readme/checkout-success-mobile.png)

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

#### Gallery Desktop
![Lighthouse report Desktop Gallery](/images-readme/gallery-desktop.png)
#### Gallery Mobile
![Lighthouse report Mobile Gallery](/images-readme/gallery-mobile.png)


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

For each recommendation, I gathered more info related to the recommendation. For restaurants for example, I display the type of cuisine, opening hours etc.
There is also a link to the website corresponding with the recommendation and a link to google maps where the exact route from the bed & breakfast to the specific recommendation is displayed. 

### Lighthouse report

#### Tourist Info Desktop
![Lighthouse report Desktop Tourist Info](/images-readme/tourist-info-desktop.png)
#### Tourist Info Mobile
![Lighthouse report Mobile Tourist Info](/images-readme/tourist-info-mobile.png)

#### Recommendation Detail  Desktop
![Lighthouse report Desktop Recommendation Detail](/images-readme/recommendation-detail-desktop.png)
#### Recommendation Detail Mobile
![Lighthouse report Mobile Recommendation Detail](/images-readme/recommendation-detail-mobile.png)

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

#### Profile Desktop
![Lighthouse report Desktop Profile](/images-readme/profile-desktop.png)
#### Profile Mobile
![Lighthouse report Mobile Profile](/images-readme/profile-mobile.png)

### User Experience
This page / feature is not often implemented in a website for a bed & breakfast and exceeds the expectations for the user. 
This makes the booking of their holidays a nicer process because it offers a more complete experience.


## Navigation 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* Display of nav links on large devices
* Display of the logo 
* Display of hamburger icon on small and medium devices
* Buttons throughout the website 

#### Conclusion
On large screens, the logo is nicely centered on the navbar with on each side 3 nav links. 
The profile navlink contains a dropdown which display nicely on the right side of the screen. 
On medium and small devices, the navigation collapses and a hamburger icon is displayed on the right side of the screen. 
Here the image is nicely displayed on the left, that counts as well for the navlinks in the dropdown.   
Navigation is responsive across various browsers and devices. 

### Functionality
All the navlinks in the navigation bar work as intented and take the user to the corresponding page. 
When the user clicks on the logo, he/she will be redirected to the homepage / welcome page.   
In order to highligh the navlink where the user was located, I had to compare the request.url to the corresponding url of that specific navlink. 
If true, active class was added to the navlink. This way the highlighting of the active navlink works as planned. 

### Lighthouse report
![Lighthouse report Desktop](/images-readme/)
![Lighthouse report Mobile](/images-readme/)

### User Experience
#### User Story: I want to have an intuitive navigation so I know right away where I can find which information
The navigation is nicely displayed and is intuitive to use for the user. 
The links are self explanatory so the user knows what he/she can expect when clicking on it.
Across the website beside the main navigation, you have various buttons as well that lets you navigate through the website. 



## Social Media 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* Quality and display of background image
* Display of social media icons

#### Conclusion 
The social media section display nicely across various browsers and devices.
The text is well readible due to the overlay on the image. 
Icons are self explanatory to the user. 

### Functionality
The links in the social media works as intented and takes the user the corresponding website.
They open in a separate tab so the user is not redirectd away from the website. 

### User Experience
The social media section helps to interact more with the (potential) guest. 
They can start following the bed & breakfast on Instagram, become friends on facebook or read reviews on Tripadvisor.
It engages the user more and this way he/she can stay up to date about the latest news. 
This section is being displayed on various (not all) pages. 


## Footer 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* General responsiveness of the footer
* Display of the 3 different parts of the footer

#### Conclusion
After removing the padding of the footer container, the footer displays nicely across browsers and devices.
On large and medium devices, the footer has 3 columns with the logo in the middle and contact info on each side of the logo.
On small devices, the contact info takes up full width of the screen with the logo displayed in the middle.

### Functionality
When the user clicks on the logo, he/she will be redirected to the homepage / welcome page.
The email icon will open up a new email for the user with the email of the bed & breakfast already filled.
Clicking on the whatsapp icon will open whatsapp when the user has it installed or open the page to download whatsapp if not. 
It will open right away a chat, with the mobile number of the bed & breakfast.


### User Experience
#### User Story: I want to be able to get in contact with the propery in case I have some questions
In the footer, the user has various ways of reaching out to the bed & breakfast: email / phone / whatsapp .
As it is standard convention to have this information in the footer, the user will have no difficulties to locate this information. 
The footer is displayed on each page which makes it easier for the user to reach out.

#### User Story: I want to know the address and how far / close it is to big cities
The full address is mentioned in the footer.   
Additional information concerning the location can be found across the website.
For example: 
* In the welcome slide of the carousel on the homepage
* Distance to various nice cities and tourist attractions for each recommendation in the tourist info page. 
 

## Reservations overview for Admin 
### Responsiveness
#### Where did I test?
Test on various devices: MacBook Pro / iPhone 6S / Acer / iPhone 8 / iPhone 11 / iPad.   
Test on various browers: Google Chrome, Safari, Opera & Firefox

#### What did I test?
* Display of the reservations
* Responsiveness of the various tables on the page

#### Conclusion
The reservations are displayed nicely into various tables, giving sufficient information to the admin. 
The tables respond well to various devices and browsers. 
On smaller devices, a horizontal scroll is implemented to the user can still view all the necessary information.


### Functionality
The reservations are split up in various sections:
* Arrivals Today
* Departures Today
* Inhouse guests
* Arrivals next 7 days
* All upcoming reservations
* All past reservations

The first 3 sections are expanded by default so the admin can right away see the most important information. 
Each reservation has a link to the confirmation that was sent to the user, containing all the info of the reservation. 
Here a flash message is displayed to remind the admin that this email was sent to the guest as confirmation. 

In order to implement the tables, I have used the [DataTables jQuery plug-in](https://datatables.net/).
By calling the datatables function, you right away get a nice interactive table with pagination, search functionality, ordering functionality and you can choose how many entries per page you want to see. 

After carefull consideration I decided to include a modal asking the superuser to confirm if he/she wants to proceed with the deleting of the reservations. 
This to avoid that reservations are removed by accident. The modal works as planned and mentions the reservation number and full name of the reservation to the admin.

For this page I still see a lot of possible improvements in order to make this a good user experience for the superuser. 
Examples of this are:
* Possibility to edit reservations
* When deleting reservations, confirmation email send to user including infomation about possible pay back of paid amount. 
* Include a status of cancelled in case the admin doens't want to delete the reservation but mark them as cancelled instead. 

### Lighthouse report
#### View reservations Desktop
![Lighthouse report Desktop View Reservations](/images-readme/view-reservations-desktop.png)
#### Homepage Mobile
![Lighthouse report Mobile View Reservations](/images-readme/view-reservations-mobile.png)


Performance is lower than it should be, especially on mobile devices. This is mainly caused by the Datatables CDN.

### User Experience
#### Site owner goals: I want to be able to see all the reservations
On this page the owners can easily see all the reservations, displayed in various categories. 
The tables make it easy for the admin to navigate through the reservations. 

#### Site owner goals: I want to have a seperate section for arriving and inhouse reservations
#### Site owner goals: I want to have a seperate section as well for the reservations for the next 7 days so I can plan in advance
In order to meet this goal of the site owner, I have created a seperate section on the page for arrivals today and arrivals for the next 7 days.



## GENERAL CONCLUSION

Webiste is respnsiveness across various devices and browers, creating a good user experience for the user. 
On point of performance, I still see some oppportunities to have this improved:
* Working with svg format for my images to make them more responsive
* Minifying my files
* Improving database queries (for example: only compare new reservation request to reservations that could interfere (+ / - 28 days ) instead of to all reservations
