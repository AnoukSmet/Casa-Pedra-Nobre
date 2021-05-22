# Bugs

### Footer was coming out of screen
#### Resolved by removing padding on footer-container

### Toggler Icon Navbar not showing
#### Resolved by adding navbar-dark to navbar and overwriting this

### Date Icon reservation request black
#### ::-webkit-calendar-picker-indicator { filter: invert(1);}

### Logo and some other images not showing


### Email verification link not working
#### Forgot {% load account %} in email_confirm.html

### Error console stripe: Uncaught IntegrationError: Please call Stripe() with your publishable key. You used an empty string.


### Policies not showing on checkout success
#### {% if amenity.category|stringformat:"s" == 'policies' %} <span class="d-block"> {{ amenity }}: {{ amenity.description }}</span>{% endif %}

### Text coming out of hero image on rooms and tourist info
#### Added margin bottom of 1.5rem

### Possible to proceed to checkout without selecting room
#### if 'select-room' in data: else redirect + flash message

### Server 500 error when submitting dates without filling them in
#### if form["check_in"] and form["check_out"]:


### Save info always reading checked 
#### Solve: Boolean($('#id-save-info:checked').val());