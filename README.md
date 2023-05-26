# <div style="color:#eb0028">TEDxOpenSource</div>

This is an open-source code for launching a customized website for your TEDx event!

Contributions to this repository are welcome. You can raise issues or resolve current issues by making pull requests.

## How does this work?

To use this website for your purposes, you must first clone this GitHub repository using ```git clone https://github.com/MohammedSB/TEDxOpenSource.git``` in the command line. A **TEDx** folder will be created on your computer that contains all files in this repository. See [this](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for reference.

This website uses [Django](https://www.djangoproject.com/) along with other packages/libraries. Therefore, these packages need to be installed for the server to run correctly. To install all the requirements, run ```pip install -r requirements.txt``` while in this repositories main directory (The **TEDx** folder).

After installing all the requirements, you can run the server from inside that folder using ```python manage.py runserver``` in the command line.

## Customizability

(1) The main, team, and sponsors page should all be changed to match your specific TEDx event. HTML comments are provided to help guide you build on the existing code.

(2) You can change the TEDx logo using the *static\images\logo* path. A TEDx logo generator is provided [here](https://landing-pages.ted.com/tedx-logo-generator/index.html) to help you design your unique TEDx logo.

(3) The website has a fully functional registration system, where attendees can register for your TEDx event using their email and other demographic information. A confirmation email is sent to every registrant using the email tedxopensource@gmail.com. You can change the sender email from settings.py.
See [this] for reference(https://docs.djangoproject.com/en/4.2/topics/email/).

(4) The number of seats in the event is decided by the ```SEAT_COUNT``` variable in apps.py, which can be changed to match your specific event. However, keep in mind that the database will only create new seats if you first run ```python manage.py migrate```. 

<sub>This project was originally part of TEDxKSAUHS 2023 event (*I belong therefore I am*).</sub>