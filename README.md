# Oishi Restaurant

![](assets/images/responsive.jpg)

[Live application can be found here](https://oishi-restaurant.herokuapp.com/)

This is a full-stack framework project built using Django, Python, HTML, & CSS. The website is built for a fictional Japanese restaurant called Oishi as an educational project for Code Institue's portfolio four. It is designed to showcase the restaurant and allow the customer to make, edit and delete reservations through their account. 


---
## UX

## Strategy
Using the core UX principles I first started with Strategy, thinking about the target audience for this restaurant & the features they would benefit from.

The target audience for 'Grow' are:
- 25-60 year olds
- People interested in food, fine-dining and eating-out
- People that are interested in culture, travel and local hotspots

These users will be looking for:
- A user-friendly website that balances information with an aesthetic that communicates the restaurant's values and reflects target customers
- Information about the restaurant, tyoes of dishes it serves and who runs it
- A way to book a table 
- A way to view and manage reservations
- Contact information
- A way to easily access social media accounts form the website


 It is increasingly common for people to make restaurant reservations on the go from their mobioe devices. Therefore, creating a mobile friendly website is essential. Bootstrap grids and elements along side custom CSS has benn used in the front-end creation. 

## User Stories
Please find all my defined user stories & their acceptance criteria [here](https://github.com/daisygunn/grow-restaurant/issues)

1. As a user I can intuitively navigate through the site so that I can view desired content.
2. As a user I can get key information about the restaurant from the landing page so that I can spend less time having to search for information.
3. As an admin user I can log in so that I can access the site's backend.
4. As an admin user I can approve or reject any reservation requests so that I can manage the restaurant's bookings efficiently.


5. As a user I can register or log in so that I can manage my booking requests.
6. As a user I can easily see if I'm logged in or not so that I can choose to log in or log out depending on what I'm doing.
7. As a user I am prompted to register for an account so that I can create an account and receive the benefits from having a profile.
8. As a user I can log in so that I can auto-populate forms with my information on the site.

9. As a user I can submit a reservation request so that I can visit the restaurant.
10. As an admin user I can prevent guests from submitting reservation requests for full slots so that I can efficiently manage customer expectations and prevent a backlog of bookings.

11. As a logged-in customer I can edit/delete an existing enquiry so that I can make changes if required online.
12. As a user I can edit my customer information so that I can make sure my details are up to date for any future communication with the restaurant.

## Scope
As a MVP the website has to achieve the desired user & business goals, the following features will be included in this version:

- A responsive navbar that will have links to all the sections and pages in the website

- A visually strong landing page that entices the user on to further exploration of the business 
- About section, with a brief suitable description and three images. 
- Specials section showcasing some of the menu items on offer. 
- Chef section describing the head chef with an image. 
- Reservations section, where logged-in users can make reservations.
- A footer section with contact information, social media links and opening times. 

 
- Register and login pages using Django allauth.
- A logout page for logged in users.  


## Structure and Styling
This website has been designed with simplicity and visual consisty in mind. It is built around the home page which contains the landing-image. As one scrolls down the  about,specials, head Chef and Reservation  sections appear. 


## Features
### Navigation Bar & Landing Page
![Screenshot of navigation, logo and main image](assets/images/screenshot-homepage.jpg)
* The nav-bar, situated on the top-right of the pages, provides the user with a clear and easily identifiable way to go between the sections and pages. 
* The logo sits in the centerof the nav-bar. This works well with the image used as draws the eye from the centeral action in the photo natuarrly to the logo. It uses an off-white colour in have a strong contrast. 
 

### About Section
![Screenshot of ethos section](assets/images/screenshot-ethos.jpg)
* This provides a brief description of the restaurant.
* The images conveys a sense of location and energy.  

### Specials Section
![Screenshot of offers section](assets/images/screenshot-offers.jpg)
* In this section further details are given on some of the signature dishes on offer alon with an image. 
  

### Chef Section
* Here a description of the head chef is given with a suitable image. 

### Footer Section
* In the footer section links are provided to the restaurant's social media accounts.
* Contact details and address are given.
* Details of opening hours.  

### Register/Login/Logout pages
![Screenshot of gallery page](assets/images/screenshot-gallery.jpg)
* Register and login pages using Django allauth.
* A logout link is provided in the nav-bar fir logged in users. 

### Databases

The reservation app requires a database to store information. This incluses ywo custom models.  

