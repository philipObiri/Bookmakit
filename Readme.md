# Bookmakit 
Bookmakit is a social website that allows users to share images that they find on the internet.
- An authentication system for users to register, log in, edit their profile, and change or reset their password. 

- A Follow System to allow users to follow each other on the website 

- Functionality to display shared images and a system for users to share images from any website .

- An activity stream that allows users to see the content uploaded by the people that they follow.


## Details Of Implementation : 
### Implementing Social Authentication : 
- Utilizing the built-in Django Authentication Framework 
- Extending the Default User Model with a Custom Profile Model. 
- Utilizing the built in Messages Framework 
- Implementing a custom authentication backend
- Implemented social authentication with Google , Facebook and Twitter using OAuth 2 with Python Social Auth. 
- Used Django Extensions to run the development server through HTTPS and Customized the social authentication pipeline to automate the User Profile Creation.


## Sharing Content 
Features to allow users to bookmark / pin media they are interested in : 

- Implemented an image bookmarking feature on the web app(Created a JavaScript Bookmarklet that integrates into the web app).
- Added Dynamic Image Thumbnail Generation 
- Implemented Asynchronous HTTP requests using JavaScript and Django
- Infinite Scroll Pagination 

## Real Time Tracking Of User Actions :
- Implemented a Follower System for users 
- Realtime User Activity Streaming 
- Realtime Counting of Image Views , Image Ranking and Recommendation with Redis. 



## Instructions to run this project : 