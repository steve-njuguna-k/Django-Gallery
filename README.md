# Django Photo Gallery (Pikcha Planet)
A Django application for a personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link. Images are hosted on Cloudinary.

![](https://github.com/steve-njuguna-k/Django-Gallery/blob/master/Screenshot.PNG)

## Requirements
The user can perform the following functions:

- A user can view different photos that interest them.
- A user can click on a single photo to expand it and also view the details of the photo. The photo details appear on a modal within the same route as the main page.
- A user can search for different categories of photos. (ie. Travel, Food)
- A user can copy a link to the photo to share with my friends.
- A user can iew photos based on the location they were taken.

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- postgresql

## Technologies Used
- python 3.9.6

## Project Setup Instructions
1) git clone the repository 
```
https://github.com/steve-njuguna-k/Django-Gallery.git
```
2. cd into Django-Gallery
```
cd Django-Gallery
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```

## Known Bugs
- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
If you have any question or contributions, please find me on [LinkedIn](https://www.linkedin.com/in/steve-njuguna-aa426096/)

© 2022 Steve Njuguna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
