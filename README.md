# <div style="color:#eb0028">TEDxOpenSource</div>

This is an opensource code for launching a customized website for your own TEDx event!

Contributions to this repo are welcome. You can raise issues or resolve current issues by making pull requests.

## How does this work?

(1) The main, team, and sponsers page should all be changed to match your specific TEDx event. HTML comments are provided to help guide you build on the exisiting code.

(2) You can change the TEDx logo using the *static\images\logo* path. A TEDx logo generator is provided [here](https://landing-pages.ted.com/tedx-logo-generator/index.html) to help you design your unique TEDx logo.

(3) The website has a fully functional registeration system, where attendees can register using their email and other demographic information. A confirmation email is sent to every registrant using the email tedxopensource@gmail.com. You can change the sender email from settings.py.
See [this for reference](https://docs.djangoproject.com/en/4.2/topics/email/)

(4) The number of seats in the event is decided by the ```SEAT_COUNT``` variable in apps.py. However, keep in mind that the database will only create new seats if you first run ```python manage.py migrate```.

(5) This website uses Django along with other packages/libraries. Therefore, these packages need to be installed for the server to run correctly. To install all the requirements, run ```pip install -r requirements.txt``` while in this repositories main directory.

<sub>This project was originally part of TEDxKSAUHS 2023 event (I belong therefore I"am)</sub>