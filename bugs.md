# Bugs

## Responsiveness

### Footer was coming out of screen

Resolved by removing padding on footer-container

### Toggler Icon Navbar not showing
Resolved by adding navbar-dark to navbar and overwriting this

### Date Icon reservation request black
::-webkit-calendar-picker-indicator { filter: invert(1);}

### Text coming out of hero image on rooms and tourist info
Added margin bottom of 1.5rem

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