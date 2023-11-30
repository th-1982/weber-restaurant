# Weber Restaurant - Booking Website

(Developer: Theresa Wolff)

![Mockup image]()

**Live Site:**

[Live webpage]()

**Link to Repository:**

[Repository]()

**Developed by: Theresa Wolff**

## Table of Content

* [The Weber Restaurant-Booking Website](#the-weber-restaurant-booking-website)
* [Table of Content](#table-of-content)
* [Overview](#overview)
* [User Experience - UX](#user-experience---ux)
  * [Strategy](#strategy)
  * [Scope](#scope)
  * [Structure](#structure)
  * [Skeleton](#skeleton)
  * [Surface](#surface)
    - [Color Scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Visual Effects](#visual-effects)
* [Agile Methodology](#agile-methodology)
* [Features](#features)
  * [Existing Features](#existing-features)
    - [Create bookings](#create-bookings)
    - [Menu](#menu)
    - [Staff bookings management](#staff-bookings-management)
  * [Future Feature Considerations](#future-feature-considerations)
* [Responsive Layout and Design](#responsive-layout-and-design)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Python packages](#python-packages)
  * [Frameworks \& Tools](#frameworks--tools)
* [Testing and Validation](#testing-and-validation)
* [Deployment \& Development](#deployment--development)
  * [Deploy on heroku](#deploy-on-heroku)
  * [FORK THE REPOSITORY](#fork-the-repository)
  * [CLONE THE REPOSITORY](#clone-the-repository)
* [Credits](#credits)
  * [Media](#media)
  * [Code](#code)
* [Acknowledgements](#acknowledgements)

## Overview
Weber Restaurant is a fictional restaurant located in the heart of Munich's English Garden, Germany. The project is designed to create a comprehensive experience for Weber Restaurant's clients. The users can easily reserve tables,  add special notes for the booking, and specify the number of guests. On the other hand, staff members can manage these bookings efficiently through a staff-only interface. The system ensures that only available tables are offered to the customers, considering variables like time, date, and capacity. The website was created to handle real-world scenarios with ease. Weber Restaurant's booking website was developed using Python(Django), HTML, CSS, and JavaScript, with data being stored in a PostgreSQL database and images on a WhiteNoise.
<br><br>
The fully deployed project can be accessed at [this link](https://.herokuapp.com/).<br><br>

## User Experience - UX
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to see a menu so I can easily navigate through website content |             
|                                       |1B| As a user, I want to see relevant information about the restaurant|
|                                       |1C| As a user, I want the website to have a nice and intuitive design that will match the restaurant's theme|
|**USER REGISTRATION/AUTENTHICATION**                     |  ||
|                                       |2A| As a  user,  I want to create an account so that I can make reservations in my name|
|                                       |2B| As a  user, I want to use my email and password to log in so that my account is secure|
|                                       |2C| As a user, I want to log in from my account so that I can keep my account safe|
|                                       |2D| As a user, I want to reset my password by sending a link so that I can log in even if I forgot my password|
|**CONTACT**                            |  ||
|                                       |3A| As a user, I want to see the restaurant's opening and closing hours|
|                                       |3B| As a user, I want to see location information on the website|
|                                       |3C| As a user, I want to see contact information on the website|
|                                       |3D| As a user, I want to see relevant information on the website|
|**MENU**                               |  ||
|                                       |4A| As a user, I want to see the restaurant's menu with details about ingredients and prices so that I can be completely aware of everything I want to order|
|**BOOKINGS**                           |  ||
|                                       |5A| As a logged-in user, I can see a list of my reservations so that I can have a better overview|
|                                       |5B| As a logged-in staff member, I can see upcoming reservations so that we can prepare for the working day|
|                                       |5C| As a logged-in staff member, I can filter reservations so that I can see reservations for a specific date|
|                                       |5D| As a logged-in user, I can update a selected reservation so that I can choose a more convenient time|
|                                       |5E| As a logged-in staff member, I can update a selected reservation to help clients|X
|                                       |5F| As a logged-in user, I can delete reservations so that I have control over my bookings|
|                                       |5G| As a logged-in staff member, I can cancel bookings so that I can help a client with the cancellation|
|                                       |5H| As a logged-in user, I can select a time and date to finalize my reservation|
|                                       |5I| As a logged-in user, I can see available tables for a specific date and time so that I can easily decide where to sit|
|                                       |5J| As a site user, I get a confirmation email when making a reservation so that the risk of becoming a no-show-reservation is minimized |
|**STAND ALONE PAGES**                  |  ||
|                                       |6A| As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist|
|                                       |6B| As a developer, I need to implement a 500 error page to alert users when an internal server error occurs|
|                                       |6C| As a developer, I need to implement a 403 error page to redirect unauthorized users so that I can secure my views|
|                                       |6D| As a restaurant owner, I would like a home page so that customers can view information on my restaurant|

|**DEPLOYMENT**                         |  ||
|                                       |7A| As a developer, I need to remove comments and turn off DEBUG so that my project is ready for final deployment|
|                                       |7B| As a developer, I need to deploy the project to Heroku so that it is live for customers|
|**DOCUMENTATION**                      |  ||
|                                       |8A| As a developer, I need to write automated tests and testing documentation so that others and myself can better understand my project|
|                                       |8B| As a developer, I need to write a readme.md so that others and I can better understand my project|

