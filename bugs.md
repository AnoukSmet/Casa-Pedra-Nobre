# Bugs

## Responsiveness

### Footer was coming out on the right side of the screen
Because of this issue, there was a horizontal scroll with a white strip on the side on each page.
This was resolved by removing the padding on the footer-container class.

Conclusion: footer works as intended and is completely responsive.


### Toggler Icon Navbar not showing
When implementing the navigation bar from bootstrap, I removed the navbar-dark as I wanted to apply my own styling. 
This results in the toggler Icon not being displayed on the screen. 
This was resolved by adding navbar-dark class again to the navbar and overwriting the styling.

Conclusion: Toggler icon is displayed on the screen while still implementing personalised design.

### Date Icon on the reservation request form displayed in black instead of white color
![Datepicker-black](/images-readme/bug-datepicker-black.png)

Resolved by adding the following code: 

```
    ::-webkit-calendar-picker-indicator {
    filter: invert(1);
}
```

Conclusion: The color of the calendar icon in the datepicker now displays in the color white which is more in line with the design.

### Text coming out of hero image on various pages like reservation form
![Datepicker-black](/images-readme/bug-herotext.png)

I have resolved this responsiveness issue by adding the following:

```
    @media (min-height: 320px) {
        #reservation {
            overflow-y: scroll;   
        }
        #reservation-hero-text {
            top: 95%;
        }
    }

    @media (min-height: 530px) {
        #reservation {
            overflow-y: hidden;   
        }
        #reservation-hero-text {
            top: 60%;
        }
    }
```

This resolved the issue for mobile devices in horizontal mode for the reservation page.
To resolve this responsiveness issue for the other page, I have decreased the font-size and added a margin-bottom. 

Conclusion: the fix described above has resolved the responsiveness issue.   
For the reservations page, this might not be the best user experience to have the scroll but it is a much better user experience than before. 

### Arrows carousel homepage
I have positioned the next and previous arrow for the carousel on the homepage on the middle (vertically) of the slide. 
Due to the different lengths in content, the arrows change position. For large devices this is okay but for small and medium devices, this is not very user friendly. 

Therefor I have change the position top to 30 rem and align-items to unset for small and medium devices.

```
.carousel-control-next {
    justify-content: flex-end;
    align-items: unset;
    top: 30rem;
}
 .carousel-control-prev {
    justify-content: flex-start;
    align-items: unset;
    top: 30rem;
 }

```

Via media queries I set the top to 50% and align items to center to be vertically aligned in the middle of the content for large devices.

Conclusion: with this fix it is much easier to navigatie through the carousel for the user on small and medium devices. 

## Functionality

### Logo and some other images not showing
After creating my account on AWS and storing my media files and static files I had some issues with some images not being displayed on the live website. 
Initially it were the images that were not stored in the database like the images from the breakfast on the rooms page. 
This was resolved by call the image with the {{ MEDIA_URL }} (example: <img src="{{ MEDIA_URL }}breakfast_room.jpg" alt="breakfast-room" class="d-block">)

After making some updates on the images, some images were again not being displayed, this time it was caused by forgetting to remove the disable static in my heroku environment variables. 
This was causing for my updates not being saved on AWS. By removing this, the static files were collected correctly and my updates were displaying nicely on the screen.

Conclusion: Fix has resolved the issue and all images are nicely being displayed on the live website.

### Email verification link not working
Emails that are sent to the user in order to verify their accounts was not working.
After various research I noticed I didn't load the {% load account %} tag in email_confirm.html.
When I added this, the issue was resolved and the user can now easily verify its account. 

Conclusion: bug has been resolved and email verification is now working properly. 

### Error console stripe: Uncaught IntegrationError: Please call Stripe() with your publishable key. You used an empty string.
This error was appearing in the console as the Stripe Public Key was not recognised when the admin was completing the checkout form. 
This is normal because when the admin make a reservation, they don't need to go through the payment step. 
In order to prevent this error from happening, I have wrapped the loading the stripe elements js in an if statement. 
If the user is a superuser, I don't load the js file as it is not needed then. 

Conclusion: the fix explained above resolved the error that was displaying in the console. I'm not 100% sure if there isn't a better solution for now, this is the best solution for my knowledge.

### Policies not showing on checkout success
On the checkout success page I wanted to display the policies once again so the user is reminded when the check-in + check-out is etc. 
I was using a for loop to loop through the amenities and when the amenity category was equal to policies, I wanted to display the policy.
For quite some time this was not working. After some research, I converted the amenity.category to a stringformat by using the following code:
```
{% if amenity.category|stringformat:"s" == 'policies' %} 
    <span class="d-block"> {{ amenity }}: {{ amenity.description }}</span>{
% endif %}
```

Now the if statement works and only the amenities with the category policies are being displayed on the checkout success screen.

Conclusion: Bug has been resolved and policies are nicely being displayed on the checkout success page. 

### Possible to proceed to checkout without selecting room
The user was able to continue to the checkout page without selecting a room. 
On the checkout page, there was then an empty room overview which doens't look nice. 
In order to not allow the user to proceed to the checkout without selecting a room, I first check if the user has selected on of the rooms. 
If not, the user page will not be allowed to proceed and a flash message will explain the error to the user. 

Conclusion: The user can only proceed to the checkout page when he/she selected at least one room. Fix has resolved the issue. 

### Server 500 error clicking 'Show availability' without filling in the checkin and checkout
The user shouldn't be able to proceed to the reservations detail page without filling in the check-in and check-out date. 
In order to check this, I have implemented an if statement that check if it has been filled in.
If not, the user is not able to proceed to the next step and a flash messages is displayed informing the user what went wrong. 

Conclusion: server error 500 does not appear anymore and user is informed correctly what he/she did wrong. 

### Duplicate rooms
On the reservation detail page where the available and unavailable rooms are beings displayed, a lot of duplicate rooms were showing. 
This was caused by me comparing the reservation request data (Check in and check out) to all the existing reservations in the system. 
If the data didn't overlap, the room was added to the available rooms and when the data overlapped, the room was added to the unavailable rooms. 

Even if the room had already been added to unavailable rooms, it was still being added to available rooms. 
First I removed all the duplicates by looping through them and only if the room is not in the new list, add it. 
Then I also check if the room is available, if it is already in unavailable rooms. If it is, I remove it from the available rooms. 

This resolves the issue. I am aware that there is still room for improvement like only comparing to a limited amount of relevant reservations instead of comparing to all reservations. 
The performance of this query will decrease the more reservations the bed & breakfast has. 

Conclusion: the bug has been resolved and for the scope of the website, the fix is a good solution which has no impact on the performance for the user. 

### Save info always reading checked 
By default I have checked the 'Save Info' box on the checkout page. 
Somehow I was not getting the correct value of the checkbox when the form was submitted, it always returned True. 
When I set the default to False, I was always returning False. 

I have updated the code in stripe elements js file to 'Boolean($('#id-save-info:checked').val());'

Conclusion: the above fix has resolved the bug and the correct value of the checkbox is returned.

### Confirmation email not being sent when comment and eta not filled in
The confirmation email was not being sent whenever the user didn't fill in the comment and/or eta in the checkout form.
This error was caused by me including the comment and eta in the stripe Payment Intent (for in case reservation needs to be created when user for example closes the browser).

I didn't want to make this information mandatory for the user as it didn't make much sense. 
Instead I check the value of these 2 fields before submitting and when the user hasn't filled in any comment or eta, I add the value 'N/A' to the field.

Now there is always a value which results in Stripe not throwing an error. 

Conclusion: Bug has been resolved and confirmation emails are sent even when comment and eta are not filled in.

### Confirmation email not being sent when CPN makes reservation
When the superuser / admin makes a reservation for the guests, the stripe payment step is being skipped.
Therefor the send email function is never called when the admin makes a reservation. 

In order to still send a confirmation email to the user so the owner of the b&b doesn't have to do this manually,
I added the send mail function to the checkout views and on the checkout success function I call that function whenever the reservation doesn't have a stripe pid.

Conclusion: email is always sent to the guest, even when admin makes the reservation for them.  
The email itself also checks for the pid and if it is not there, guest is informed that the payment will be done at the property.

### Accordion on tourist-info page

When click the first button on the tourist info page, the recommendations nicely appear below. 
When you then scroll down and click the second button, the first one collapses again and second one shows all the relevant recommendations. 
The issue here is that the user has to scroll back up in order to start on top as currently the last recommendations of that specific topic are being displayed.

Conclusion: currently I didn't manage to encounter a solution yet for this issue. This will be further researched and implemented at a later stage. 