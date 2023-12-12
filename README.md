# Weber Restaurant - Booking Website

(Developer: Theresa Wolff)

![Mockup image](file:///C:/Users/wolff/OneDrive/Desktop/mockup_files/image.png)

**Live Site:**

[Live webpage](https://weber-restaurant-496816a4ee09.herokuapp.com/)

**Link to Repository:**

[Repository](https://github.com/th-1982/weber-restaurant)

**Developed by: Theresa Wolff**

## Table of Content

* [The Weber Restaurant-Booking Website](#the-weber-restaurant-booking-website)
* [Table of Content](#table-of-content)
* [Overview](#overview)
* [User Experience - UX](#user-experience---ux)
  + [Strategy](#strategy)
  + [Scope](#scope)
  + [Structure](#structure)
  + [Skeleton](#skeleton)
  + [Surface](#surface)
    - [Color Scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Visual Effects](#visual-effects)
* [Agile Methodology](#agile-methodology)
* [Features](#features)
  + [Existing Features](#existing-features)
    - [Create bookings](#create-bookings)
    - [Menu](#menu)
    - [Client booking management](#client-bookings-management)
    - [Staff bookings management](#staff-bookings-management)
    - [Contact](#contact)
  + [Future Feature Considerations](#future-feature-considerations)
* [Responsive Layout and Design](#responsive-layout-and-design)
* [Technologies Used](#technologies-used)
  + [Languages](#languages)
  + [Python packages](#python-packages)
  + [Frameworks \& Tools](#frameworks--tools)
* [Testing and Validation](#testing-and-validation)
* [Deployment \& Development](#deployment--development)
  + [Deploy on heroku](#deploy-on-heroku)
  + [FORK THE REPOSITORY](#fork-the-repository)
  + [CLONE THE REPOSITORY](#clone-the-repository)
* [Credits](#credits)
  + [Media](#media)
  + [Code](#code)
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
|                                       |2C| As a user, I want to log out from my account so that I can keep my account safe|
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

**Project Goal:**<br>
This project aims to create a website for the Weber Restaurant that is useful and ensures efficient management for staff members and an engaging experience for clients.

**Project Objectives:**<br>
* To create a  website  with a simple and intuitive User Experience;
* To make a responsive website that works on every device;
* To add content that is relevant and helps create a better image of the restaurant;
* To make clear categories of login accounts for staff members and clients;
* To implement fully functional features that will ease the staff members' tasks and upgrade clients' experience with the restaurant services;
* To present the restaurant's menu visually appealing and informatively, providing details about ingredients, prices, and any particular dishes;
* To ensure the security and privacy of user data, especially regarding personal information and reservation details;
* To maintain consistency with the brand identity of Weber Restaurant in terms of colors, fonts, and overall visual style.<br><br>

### Scope<hr>
**Simple and Intuitive User Experience**<br>
* Create a design that aligns with the restaurant's theme and branding;
* Create a clear and well-organized header and footer design;
* Ensure the navigation menu is prominently displayed and remains functional at every step of the user journey;
* Ensure each page has a suggestive name that reflects its content;
* Create visual feedback mechanisms to inform users as they navigate through different pages;
* Organize content logically, making relevant information easily accessible to users;
* Create prominent and clear call-to-action buttons, guiding users to essential functions like making reservations and viewing the menu.

**Relevant Content**<br>
* Add relevant information about the restaurant, such as the restaurant's name, precise location, contact phone number, and email address;
* Create a clear and attractive presentation of the restaurant menu;
* Create the culinary delights of Weber Restaurant through high-quality and appetizing photos.

**Features for Upgraded Experience**<br>
* Create an intuitive reservation system enabling users to view and select available tables for specific dates and times:
* Create a Menu feature that provides information about each dish, including ingredients and pricing;
* Create a Profile page where customers can track their upcoming reservations and manage their favorite meals;
* Create a staff-member account system with specialized privileges for managing all bookings for all the users.

**Clients and Staff Members Different Accounts**<br>
* Allow access to a personalized profile page for client types of users where they can view and manage their reservations, favorite meals, and dining preferences;
* Allow access to the Manage Bookings page, which enables staff members to handle reservations efficiently, update table availability, and provide excellent customer service;
* Create a filter function within the staff-member dashboard to quickly locate and manage specific reservations;
* Allow the client to add and edit meal reviews and overall dining experiences.

**Responsiveness**<br>
* Create a responsive website that adapts to various devices, including desktops, laptops, tablets, and smartphones. 

### Structure<hr>
The website is created and designed to focus on user experience and is divided into seven distinct pages, each crafted to fulfill a specific function. The content on these pages dynamically adapts depending on the user's authentication status and roles as either a client or staff member. Here are the details:
* **Register/Login:** pages allow users to create accounts and authenticate for accessing personalized features. 
* **Logout:** This page implements a modal for users to securely log out of their account and ensure a user-friendly experience when exiting the current session.
* **Home page:** The page is accessible to both client and staff users and includes restaurant details, special dishes, and reviews. A call to action to encourage users to make a reservation like  Book a Table.  It also provides a welcoming overview of the restaurant for all visitors.
* **Menu:** The page is open to all users and displays the restaurant's menu items. An "Add to Favourite" feature is available only to logged-in clients.
* **Reservations:** Exclusive to authenticated users (clients and staff). This page enables authenticated users to make or manage bookings and provides a personalized space for users to handle their reservations and account details.
* **Contact:** contains information visible to all users and provides details on the restaurant's location, opening & closing times, and contact information for easy access.
* **Staff Manage Bookings:** Limited to staff members only and exclusively accessible to staff members. This page displays a comprehensive view of all registered bookings, offering tools for efficient management through grouping and filtering by date.

#### Flowchart
The Flowchart for my program was designed using <b>LucidChart</b>. It visualizes the system's work, providing an overview of the logic and steps involved in the program's workflow.<br>
![Flowchart](docs/readme_images/weber-restaurant-flowchart1.jpg)<br><br>

### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created with  [Balsamiq](https://balsamiq.com/wireframes/desktop/#) tool 
- Home page

![Home Page](docs/readme_images/home-w.jpg)


- Menu page


![Menu Page](docs/readme_images/menu-w.jpg)

- Reservation page

![Reservation Page](docs/readme_images/reservation-w.jpg)

-Contact page

![Contact Page](docs/readme_images/contact-w.jpg)

- Register Page

![Register page](docs/readme_images/register-w.jpg)

- Login 

![Login](docs/readme_images/login-w.jpg)

- Logout page

![Logout](docs/readme_images/logout-w.jpg)

- Create Reservation page

![create reservation](docs/readme_images/create_reservation-w1.jpg)


- Update Reservation page

![Update reservation](docs/readme_images/edit_reservation-w1.jpg)



**Database**<br>
The project uses ElephantSQL as PostgreSQL relational database for storing the data.<br>
Two diagrams were created to represent the relationships between the tables. The first diagram was created before the website was developed, and it was used to identify the most relevant and useful attributes and tables. The final diagram was created after the website was developed, and it reflects the changes that were made to the attributes and tables.

<details>
  <summary>Initial Model</summary>
<img src="docs/readme_images/datamodel_plan.jpeg" ><br>
</details>


### Surface<hr>
#### Color Scheme
* The color scheme balances vibrant and energetic elements with neutral tones to maintain readability and a harmonious visual appeal. Using consistent colors throughout different sections creates a cohesive and branded user experience for the Weber Restaurant project. The remaining features on the website and font are a balance of dark grey or black and white to maintain contrast and readability. <br>

<img src="docs/readme_images/colorscheme-weber1.jpg">
<img src="docs/readme_images/coloscheme-weber2.jpg">

#### Fonts
* The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>
* h1 - h6 elements: *Montserrat*
* Body: *Lato*

#### Logo
* The website logo was made using [Canvas](https://www.canva.com/templates/?query=logo) to match website's color scheme


## Agile methodolgy
This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [GitHub](https://github.com/). As the user stories were accomplished, they were moved in the GitHub Kanban board from **ToDo**, to **In Progress**, **Done** and **Not Implemented** lists.
<details> 
<summary>Sprint Details</summary>

* **KANBAN BOARD**<br><br>
    <img src="docs/readme_images/kanban-weber-restaurant.jpg" width="70%"><br><br>
* **EPIC 1 - BASE SETUP**<br>
    - Create base.html<br>
    - Create static resources<br>
    - Create navigation menu<br>
    - Design according to good UX practices<br>
    - Setup Django project<br>
    - Create a footer<br><br>
    <img src="docs/readme_images/epic-1.jpg" width="60%"><br><br>
* **EPIC 2 - CONTENT AND NAVIGATION**<br>
    -2A create content and navigatio<br>
    -2B view the Restaurant's relevant information<br>
    -2C see the nice and intuition design about the restaurants<br><br>
    <img src="docs/readme_images/epic-2.jpg" width="60%"><br><br>
* **EPIC 3 - USER REGISTRATION/AUTENTHICATION**<br>
    -3A Implement the *Register* page using the django-allauth module<br>
    -3B Implement the *Login* page using django-allauth module<br>
    -3C Implement *Logout* modal using django-allauth module<br>
    -3D Implement a *Reset password* function<br><br>
    <img src="docs/readme_images/epic-3.jpg" width="60%"><br><br>
* **EPIC 4 - CONTACT**<br>
    -4A Implement opening & closing times on the webpage<br>
    -4B Implement information about location of the restaurant<br>
    -4C Implement contact information<br>
    -4D Implement other relevant information<br><br>
    <img src="docs/readme_images/epic-4.jpg" width="60%"><br><br>
* **EPIC 5 - MENU**<br>
    -5A Create a menu page with menu items<br>
    -5B Implement a function so that staff can enter new items on the menu<br><br>
    <img src="docs/readme_images/epic-5.jpg" width="60%"><br><br>
* **EPIC 6 - BOOKINGS**<br>
    -6A Implement reservation view for site user<br>
    -6B Implement reservation view for staff<br>
    -6C Implement reservation filter function for staff<br>
    -6D Implement function so site user can update a reservation<br>
    -6E Implement function so staff can update reservation<br>
    -6F Implement so user can delete a reservation<br>
    -6G Implement so staff can delete reservations<br>
    -6H Implement function so that user can create a reservation<br>
    -6I Implement so that site user can see available tables<br>
    -6J Implement so that user receives a confirmation email after creating a reservation<br><br>
    <img src="docs/readme_images/epic-6.jpg" width="60%"><br><br>
* **EPIC 7 - STAND ALONE PAGES**<br>
    -2A Implement 404 page<br>
    -2B Implement 505 page<br>
    -2C Implement 403 page<br>
    -2D Create a restaurant page<br><br>
    <img src="docs/readme_images/epic-7.jpg" width="60%"><br><br>
* **EPIC 8 - DEPLOYMENT**<br>
    -7A Prepare the project for deployment<br>
    -7B Deploy the project to Heroku<br><br>
    <img src="docs/readme_images/epic-8.jpg" width="60%"><br><br>
* **EPIC 9 - DOCUMENTATION**<br>
    -8A Create automated tests<br>
    -8B Write documentation for project in README.md<br><br>
    <img src="docs/readme_images/epic-9.jpg" width="60%"><br><br>
</details><br><br>

## Features

### Existing Features<hr>

#### Navigation Menu

* Navigation Menu on Weber Restaurant Website:
The navigation menu on the Weber Restaurant website is a critical component that facilitates seamless navigation and enhances the overall user experience. Here are key features and characteristics:
* Logo and Restaurant Name:
  * The menu prominently features the restaurant's logo and name, providing users with instant brand recognition and reinforcing the identity of Weber Restaurant.<br>
* Navbar:
  * The navigation menu includes a navbar with links to various sections and pages of the website.<br>
  * The navbar is designed for user-friendly navigation, allowing visitors to access different parts of the website easily.<br>
* Consistency Across Pages:
  * The navigation menu maintains consistency across all pages of the website.<br>
  * This consistency ensures that users can quickly locate and access navigation options, irrespective of the specific page they view.<br>
* Visibility for All Users:
  * The navbar, logo, and restaurant name are visible to unauthenticated and authenticated users.<br>
  * This design choice ensures a uniform and familiar interface for all visitors, contributing to a positive and cohesive user experience.<br>
* Responsive Design:
  * The navigation menu is designed to be responsive, adapting to different screen sizes.<br>
  * On smaller devices, the menu may collapse into a hamburger menu, optimizing space and ensuring usability on mobile devices.<br>
<br><br>

<img src="docs/readme_images/navbar.jpg" width="60%"><br><br>

#### Footer

* Social Media Links:
  * The footer includes links to the restaurant's social media profiles on Twitter, Instagram, YouTube, and Facebook.<br>
  * These links allow users to stay updated on special offers and promotions not featured on the website.<br>
* Accessibility Considerations:
  * Aria labels have been added to the social media icons to enhance accessibility for users relying on-screen reading technology.<br>
  * This ensures that users with disabilities can understand the purpose of each link.<br>
* New Tab Opening:
  * The social media links are configured to open in new tabs. This helps users maintain their current browsing session on the restaurant's website.<br>
* Consistent Footer Design:
  * The footer maintains a consistent design across various screen sizes, ensuring a cohesive and visually pleasing experience for users.<br>
* Copyright Feature:
  * Includes a copyright statement, providing legal information about the ownership of content on the website.<br>
* Scroll-to-Top Functionality:
  * The footer incorporates a scroll-to-top link, represented by an arrow icon.<br>
  * When clicked, this link smoothly scrolls users back to the top of the page, enhancing overall user experience and navigation.<br>
<br><br>

<img src="docs/readme_images/footer.jpg" width="60%"><br><br>

#### Home page
* Accessibility:
  * The home page is accessible to client and staff users, ensuring a consistent experience for all visitors.<br>
  * About Page: Provides an overview of the restaurant's history, mission, or other relevant details.
* Special Dishes: 
  * Showcases unique or signature dishes offered by Weber Restaurant.<br>
  * Reviews: Displays customer reviews, adding a social proof element to the page.<br>
* Call to Action (CTA):
  * Features a prominent call to action, encouraging users to make a reservation with a "Book a Table" button.<br>
  * The CTA serves as an invitation for visitors to engage with the restaurant and plan their visit. .<br>
<br><br>
<img src="docs/readme_images/hero.jpg" width="60%"><br><br>
<img src="docs/readme_images/welcome.jpg" width="60%"><br><br>
<img src="docs/readme_images/special.jpg" width="60%"><br><br>
<img src="docs/readme_images/review.jpg" width="60%"><br><br>

#### Menu 
* List of Menu Elements:
  * Displays a comprehensive list of all available menu items offered by Weber Restaurant.<br>
  * Each item represents a distinct meal.<br>
* Details for Each Menu Item:
  * **Name**: Mention the name of the dish.<br>
  * **Image**: Includes a visual representation of the dish (optional).<br>
  * **Price**: Specifies the cost of each menu item.<br>
  * **Ingredients**: Provides a list of ingredients used to prepare the dish.<br>
* Simple and Attractive Design:
  * The page's design is kept simple and attractive, enhancing the user experience.<br>
  * Emphasizes visual appeal with images (if included) and clear presentation of information.<br>
<img src="docs/ireadme_images/menu.jpg" width="60%"><br><br>


#### Reservation
* The key features and aspects of this specialized page:
* Authentication Requirement:
  * The page is accessible only to users who have undergone the authentication process, ensuring it remains exclusive to authenticated clients and staff members.<br>
* Personalized Space:
  * Authenticated users are provided a personalized space to perform various actions related to their reservations and account details.<br>
* Booking Creation:
  * Authenticated clients can initiate the booking creation process directly from this page. A user-friendly form or interface allows them to input reservation details such as date, time, and the number of guests.<br>
* Booking Management:
Users, both clients and staff, can manage their existing bookings through intuitive controls. This includes options to view, edit, and delete reservations as needed.<br>
<br><br>
<img src="docs/readme_images/reservation.jpg" width="60%"><br><br>

#### Contact

* Opening Hours:
  * Displays the operating hours of Weber Restaurant.<br>
  * Provides visitors with information about when the restaurant is open for business.<br>
* Contact Information:
  * Includes essential contact details such as phone number and email address.<br>
  * Allows users to contact the restaurant for inquiries, reservations, or other purposes.<br>
* Physical Location:
  * Specifies the address of Weber Restaurant.<br>
  * Offers users a clear understanding of where the restaurant is located.<br><br> 

<img src="docs/readme_images/contact.jpg" width="60%"><br><br>

#### Register/Login
* User Registration:
  * Users can create accounts on the platform.<br>
  * This process typically involves providing username, email, and password information.<br>
* Authentication:
  * Authenticated users can access personalized features and content.<br>
  * Authentication ensures that users are who they claim to be, typically by entering valid credentials.<br>
* User Registration Page:
  * Allows new users to sign up for an account.<br>
  * Collects necessary information for account creation.<br>
* Authentication Page:
  * It will enable users to log in to their accounts.<br>
Typically, it involves entering a username/email and password.<br>
* Password Reset Functionality:
  * Provides a mechanism for users to reset their passwords if forgotten.<br>
  * Enhances user experience and security. .<br><br> 

<img src="docs/readme_images/register2.jpg" width="60%"><br><br>
<img src="docs/readme_images/login.jpg" width="60%"><br><br>

#### Logout
* Purpose:
  * The modal is designed to facilitate a secure and user-friendly logout experience.<br>
* User Triggered:
  * Users trigger the logout modal, presumably by interacting with a "Logout" button or a similar UI element.<br>
* Modal Functionality:
The modal provides a secure environment for users to confirm their logout decision.<br>
* User-Friendly Experience:
  * The modal aims to enhance the user experience by providing a clear and intuitive way to end their session.<br>
  <br><br>

<img src="docs/readme_images/logout.jpg" width="60%"><br><br>

#### Client bookings management

* The Reservation page on the Weber Restaurant website is specifically designed for authenticated clients, providing them with a convenient overview and management options for their reservations. Here are the key functionalities:
* Authentication Requirement:
The Reservation page is accessible only to authenticated clients, ensuring the content and functionalities are personalized and secure.<br>
* Overview of Reservations:
  * Authenticated clients are presented with a clear overview of their existing reservations.<br>
  * The overview may include reservation date, time, table information, and special notes.<br>
* Create New Reservation:
  * Clients can create a new reservation directly from the Reservation page.<br>
  * This functionality streamlines the reservation process, allowing clients to schedule a new dining experience easily.<br>
* Edit Existing Reservation:
Authenticated clients can edit their existing reservations.<br>
  * The edit functionality may include modifying details such as the reservation date, time, or the number of guests.<br>
* Delete Reservation:
  * Clients can delete reservations they no longer need or wish to modify.<br>
  * The delete functionality allows clients to manage their reservations according to their preferences.<br>
<br><br>

<img src="docs/readme_images/clientlist.jpg" width="60%"><br><br>

#### Staff bookings management

* The reservation page for authenticated staff users in Weber Restaurant is a powerful tool designed to streamline the management of reservations. Here's an overview of the key features and functionalities available to staff users:
* Authentication and Authorization:
Access to the Reservation page is restricted to authenticated staff users, ensuring only authorized personnel can perform reservation-related actions.<br> 
  * Comprehensive Overview:
Staff users are presented with a comprehensive overview of all reservations made at the restaurant.<br>
  * Reservation details include reservation date, time, assigned table, guest count, and special notes.<br>
* Search Functionality:
  * Staff users can search for specific reservations based on criteria such as reservation date or customer email address.<br>
  * The search feature enhances efficiency, allowing staff to locate and manage reservations quickly.<br>
* Create New Reservation:
  * Staff users can initiate the creation of a new reservation directly from the Reservation page.<br>
  * This functionality is valuable for handling walk-in customers or phone reservations with ease.<br>
* Edit Existing Reservation:
  * The system allows staff users to edit details of existing reservations as needed.<br>
  * Editing functionalities may include modifying reservation date, time, table assignment, or updating guest count.<br>
* Delete Reservation:
  * Staff users can delete reservations when necessary.
  * This feature helps handle cancellations or adjust the seating plan based on changing circumstances.<br>
* Efficient Reservation Management:
  * The Reservation page provides a user-friendly interface, ensuring staff users can efficiently manage reservations without unnecessary complexity.<br>
* Confirmation Messages:
Staff users receive confirmation messages upon successfully creating, editing, or deleting a reservation.<br>
* Confirmation messages provide feedback and acknowledgment, ensuring that staff are informed of the outcomes of their actions.<br>
<br><br>

<img src="docs/readme_images/stafflist.png" width="60%"><br><br>

#### Create bookings

* The Reservation page for authenticated users in Weber Restaurant allows users to create reservations using a user-friendly form. Here's an overview of the key features and the reservation creation process:
* Authentication and Access:
  * Access to the Reservation page is available to authenticated users, ensuring that only logged-in customers can create reservations.<br>
* Reservation Form:
  * The page features a reservation form where users can input details for their booking.<br>
* Key form elements include fields for Name, Date, Time, Number of People, and any Special Notes.<br>
* Date and Time Selection:
  * Users can select the desired date for their reservation.<br>
  * Time intervals are presented as a list, and users can choose from the available time slots:
*  12:00 - 14:00
*  14:00 - 16:00
*  16:00 - 18:00
*  18:00 - 20:00
*  20:00 - 22:00<br>

* Success Message:
  * Upon successful submission of a reservation, users receive a success message.<br>
<br><br>
   
<img src="docs/readme_images/create_reservation.jpg" width="60%"><br><br>



#### Edit bookings page

* For Users:
  * The "Edit" button is available on the manage bookings page.<br>
  * Regular users can click on this button to be directed to a form.<br>
  * The form allows them to update or edit their booking details when necessary.<br>
  * This feature enhances user experience, enabling them to manage their reservations easily.<br>

* For Staff Users:
  * Staff members can access the "Edit" button on the manage bookings page.<br>
  * Staff can edit bookings, even if they did not create the reservation.<br>
  * It allows staff members to amend booking details as needed, providing more control and flexibility in managing reservations.<br>
  <br><br>
<img src="docs/readme_images/edit_reservation.jpg" width="60%"><br><br>

#### Delete Booking Page

* Adding a "Delete Booking" feature enhances the user and staff experience on the reservation management page. Here are the critical aspects of the "Delete Booking" functionality:
* User-Friendly Interface:
  * A "Delete" button for customers and staff members is incorporated into the reservation management page.<br>
* Reservation_Deletion.html Template:
  * The delete functionality is implemented within the reservation_delete.html template, providing a dedicated space for users to manage their bookings.<br>
* Customer Deletion:
  * Upon accessing the reservation management page, customers can utilize the "Delete" button to remove a booking they no longer require.<br>
  * This feature empowers customers to manage their reservations independently without contacting the restaurant directly.<br>
* Staff Deletion:
  * Staff members also can delete bookings through the user interface.<br>
  * This capability allows staff to efficiently handle situations where a customer calls to cancel a booking, freeing up table capacity.<br>
* Confirmation Process:
  * This confirmation step ensures that users, both customers and staff, are intentional about their deletion actions.<br>
  <br><br>
  <img src="docs/readme_images/delete_reservation.jpg" width="60%"><br><br>


### Potential Future Features
**Multilingual Support**: Provide Support for multiple languages to cater to a diverse customer base.

**Personalized User Accounts**: Allow users to create accounts for a more customized experience, saving favorite menu items or past reservations.

**User Reviews and Ratings**: Implement a review and rating system for menu items and overall dining experience.

**Google Login**: Users can register or log in with their existing Google credentials, eliminating the need to create a new account and remember additional login details.

**Email confirmation for Reservations**:  Implement an automated email confirmation system that sends a confirmation email to users when they make a reservation.


## Responsive Layout and Design
The project design has been adapted to all devices using Bootstrap predefined breakpoints. A custom breakpoint was used for intermediate devices where the layout didn't fit accordingly.

## Tools used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Visual Studio](https://code.visualstudio.com/) - for writing and testing the code<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[ElephantSQL](https://www.elephantsql.com/) - For PostgreSQL database<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[LucidChart](https://www.lucidchart.com/) - used for creating the Flowchart and Database relational schema<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[TinyPNG](https://tinypng.com/) - for compressing the images<br>
[Grammarly](https://app.grammarly.com/) - for correcting text content<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[Code Institute Pylint](https://pep8ci.herokuapp.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[Cloudinary](https://cloudinary.com/) - for storing static data<br>
Chrome LightHouse extension - for testing performance<br>
[coolors.co](https://coolors.co/8aea92-80ada0-5f5566-33202a-000000) - for super color palettes generator<br>
[Canva](https://www.canva.com/templates/?query=logo) - used to create the logo in header


### Python Modules/Packages used:

Several core packages were used; a few of the most important ones are listed here, together with their functions:

* Django - A high-level Python web framework developed for this application/site.
* psycopg2 - PostgreSQL database adapter for the Python programming language.
* WhiteNoise - used for serving static files (CSS; Javascript, images, etc)
- django-allauth - Integrated Django applications addressing authentication, registration, account management, and 3rd party (social) account authentication.
- Django-crispy-forms - provides a `crispy` filter and `{% crispy %}` tag that allows control of the rendering behavior of Django forms in an exquisite and DRY way.
- crispy-boostrap4 - Bootstrap4 template pack for django-crispy-forms.
- coverage - allows the creation of a coverage report of automated testing.

## Testing
The testing documentation can be found at [TESTING.md](TESTING.md)


## Deployment


### Deploy on Heroku

**Requirement and Procfile**

Before deployment on Heroku, two files need to be created and be up to date, a `requirements.txt` file and a `Procfile`.

- The `requirements.txt` file is created by executing the following command in the terminal window: ` pip3 freeze --local > requirements.txt`. A file with all requirements will be created.
- Then create a file named `Procfile` and insert the following code: `web: gunicorn worldtravels.wsgi`, with no empty lines after it.
- Then make sure to push these files to your repository.

**Creating Heroku App**

- Log into Heroku and go to the Dashboard.
- Click "New" and then select "Create new app".
- Give your app a name and select the region closest to you.
- Click "Create app" to confirm.

**Creating a database**

- Log into ElephantSQL.com and access your dashboard.
- Click "Create New Instance"
- Set up a plan, give your plan a **Name**, select the **Tiny Turtel (Free)** plan, leave the **Tags** field blank.
- Select "Select Region" and select a data center new you.
- Click "Review".
- Confirm your details and then click "Create instance".
- Return to the ElephantSQL dashboard and click on the database instance name for this project.
- In the URL section, click the copy icon to copy the database URL.
- In your workspace make sure django and gunicorn are installed by running `pip3 install 'django<4' gunicorn`.
- Equally make sure that infrastructure for the database is installed by running `pip3 install dj_database_url===0.5.0 psycopg2`.
- Update the `requirements.txt` file if needed.

**The env.py file**

- If you do not have a `env.py` file in your workspace create one and make sure it is included in the `.gitignore` file.
- At the top of the `env.py` file add the line: `import os`.
- Below that add the following two lines:

  `os.environ["DATABASE_URL"] = "<copied URL from SQL database>"` <br>
  `os.environ["SECRET_KEY"] = "<create a secret key of your own>"` <br>

- If you are using Cloudinary storage also add the following line: <br>

  `os.environ["CLOUDINARY_URL"] = "<copied URL from Cloudinary account>"`<br>

- Make sure the environment variables are imported correctly into the `settings.py` file.
- Run `python manage.py migrate` in the terminal window to migrate the data structure to the database instance.

**Setting Environment Variables**

- On the Heroku Dashboard select the app you just created and then select the "Settings" tab.
- Click "Reveal Config Vars"
- Add the following config vars: <br>

  `DATABASE_URL` - copy the database URL from ElephantSQL in here, it should also be in the `env.py` file. <br>
  `SECRET_KEY` - copy your secret key in here. <br>

- If you are using Cloudinary storage you also need to copy your personal `CLOUDINARY_URL` into these fields. <br>
- In addition, you may need the key `PORT` with value `8000`.

**Connecting to GitHub and Deploy**

- On the Heroku Dashboard select the app you just created and then select the "Deploy" tab.
- Select GitHub for the deployment method.
- Search for the name of the project repository and click "Connect".
- Further down the page, select "Enable Automatic Deploys" if desired.
- Then finally further down, select "Deploy Branch" and watch the app being built.

### Forking the Repository

- Log in to GitHub and locate the GitHub repository you want to fork.
- At the top of the Repository above the "Settings" Tab on the menu, locate the "Fork" Button and click it.
- You will have a copy of the original repository in your GitHub account.
- You will now be able to make changes to the new version and keep the original safe.

### Making a Local Clone

- Log into GitHub and locate the repository you want to clone.
- Click the 'Code' dropdown above the file list.
- Copy the URL for the repository.
- Open Git Bash in your IDE.
- Change the current working directory to the location where you want the cloned directory.
- Type `git clone` in the CLI and then paste the URL you copied earlier. This is what it should look like:
  `$ git clone https://github.com/`
- Press Enter to create your local clone.

You will need to install all of the packages listed in the requirements file you can use the following command in the terminal `pip install -r requirements.txt` which will do it for you.

## Credits


### Code

Resources, Readme and inspiration came from a few sources:

*  [Christia Goran](https://github.com/christiangoran/dome-restaurant-repo)
* [Useriasminna](https://github.com/useriasminna/italianissimo-booking-website) 
* Further studies with [Net Ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
* Help with Bootstrap from their own excellent [documentation](https://getbootstrap.com)
* Database setup and much more with [Codemy.com](https://www.youtube.com/watch?v=A1nqCgAM6CE)
* Automated testing with [CodingEntrepeneurs](https://www.youtube.com/watch?v=5E_xLmQXOZg)
* Code from Gareth McGirr's [project](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak) used and customized for table verification
* I use also a book called Django for bigginers and Django Documentation. Code Institutes  Agile Methodologies, Django and Python walkthrough projects and videos.
* Code from Gareth McGirr's [project](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak),
[Ulrike](https://github.com/URiem/worldtravellog)
* I also re-watching Code Institutes splendid videos on Agile Methodologies, Django and Python to find solutions to problems.


## Media 

Images:
* The hero image, background image and all the images in the manu page, about page were taken from [pexels](https://www.pexels.com),
[pixaby],(https:pixaby.com)
[Freepik](https://www.freepik.com)


## Acknowledgements

- Code Institute for providing a great course and support.<br>
- My mentor Gareth McGirr for great guidance and for wanting to help me more than expected of him  with the problems encountered during the development of the project<br>
- Slack community for great involvement in helping each other<br>
- MY family, for their encouragement and support along the way<br>







