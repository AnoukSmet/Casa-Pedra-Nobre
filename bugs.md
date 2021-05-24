# Bugs

## Responsiveness

### Footer was coming out on the right side of the screen
Because of this issue, there was a horizontal scroll with a white strip on the side on each page.
This was resolved by removing the padding on the footer-container class.

Conclusion: footer works as intended and is completely responsive.


### Toggler Icon Navbar not showing
When implementing the navigation bar from bootstrap, I removed the navbar-dark as I wanted to apply my own styling. 
This results in the toggler Icon not being displayed on the screen. 
This was resolved by adding navbar-dark class againvto the navbar and overwriting the styling.

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
Changed position top: 30rem and align-items to unset for small and medium devices

## Functionality

### Logo and some other images not showing


### Email verification link not working
Forgot {% load account %} in email_confirm.html

### Error console stripe: Uncaught IntegrationError: Please call Stripe() with your publishable key. You used an empty string.


### Policies not showing on checkout success
{% if amenity.category|stringformat:"s" == 'policies' %} <span class="d-block"> {{ amenity }}: {{ amenity.description }}</span>{% endif %}


### Possible to proceed to checkout without selecting room
If 'select-room' in data: else redirect + flash message

### Server 500 error when submitting dates without filling them in
If form["check_in"] and form["check_out"]:

### Save info always reading checked 
Solve: Boolean($('#id-save-info:checked').val());

### Confirmation email not being sent when comment and eta not filled in (Stripe needed info)
Solve: when not filled in, replace value with N/A

### Confirmation email not being sent when CPN makes reservation
Manually call email function when reservation has no stripe_pid