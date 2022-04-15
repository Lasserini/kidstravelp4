<h1 align="center">KidsTravel</h1>

<h2 align="center"><img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/readme_image.png"></h2>


[Visit the deployed website](https://kids-travel.herokuapp.com/)

## 1. User Experience (UX)

### 1.1 Project introduction
This website is a concept model for a website aimed at helping parents traveling with their children. The site features a variety of activities to do with kids whilst traveling. <br><br>
This demo concept contains prepopulated experiences added for Florence & Copenhagen, whilst a fully fletched version of the site would incorporate functionality to allow users to add additional experiences to the database.<br>
It provides search functionality to find experiences based on city and category filtering, enabling users to quickly navigate to relevant content.

Users can search for experiences and write their own review of the experiences, with build-in functionality to edit and delete previously posted reviews.

### 1.2 Design approach
The site was build using an agile methodology. The method applied was a Kanban Board. Here's an image of the Kanban board earlier in the process.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/kanban_board.png">

### 1.3 Design guidelines
Simple, intuitive, stick to a few colours & designpatterns throughout the site. Simple does it.

### 1.4 Project goals
- Provide a proof of concept.
- Add meaningful search mechanisms.
- Allow users to post reviews of the added experiences.

### 1.5 Target audience
- Parents traveling with children.
- Parents seeking local activities with children could also utilize the database.

### 1.6 User stories
- As an owner, I want to post new activities, so the site offers stronger value.
- As an owner, I want to provide users with quality content.
- As an owner, I want allow users to create a profile.
- As a user, I want to find travel activities for my children.
- As a user, I want to share how an activity was for me.
- As a user, I want to edit a posted review.
- As a user, I want to delete a posted review.
- As a user, I want an search by category.
- As a user, I want an search by city.
- As a user, I want an create a user account.

### 1.7 Design

-   #### Typography
    -   The Roboto font is the main font used with Sans Serif as the fallback font in case Roboto isn't being imported into the site correctly. Oswald is used for headings, also with Sand Serif as fallback.

*   ### Wireframes
    Desktop | Phone
    --- | --- |
    <a href="https://github.com/Lasserini/kidstravelp4/blob/main/media/wireframes/index_desktop.png">Index</a> | <a href="https://github.com/Lasserini/kidstravelp4/blob/main/media/wireframes/index_mobile.png">Index</a> 
    <a href="https://github.com/Lasserini/kidstravelp4/blob/main/media/wireframes/search_desktop.png">Search</a> | <a href="https://github.com/Lasserini/kidstravelp4/blob/main/media/wireframes/search_mobile.png">Search</a>
    <a href="https://github.com/Lasserini/kidstravelp4/blob/main/media/wireframes/experience_desktop.png">Experience</a> | <a href="https://github.com/Lasserini/kidstravelp4/blob/main/media/wireframes/experience_mobile.png">Experience</a>


## 2. Features
### 2.1 Current Features
*   General   
    - User authentication, account creation etc
    - Search functionality
    - Users are able to post reviews of the listed activities
    
    <br>
*   The Header includes:
    - **Logo** allows the user to clearly see what site they are visiting at any given moment.
    - **Navigation Bar:** provides an easy and intuitive way for the user to navigate the site.
    - **Profile Buttom:** allows user easy access to their personal account page.

    <br>
*   The Footer includes:
    - **Social Media links**
    - **Site Name**

    <br>
*   The Index page includes:
    - **Hero Image**
    - **Welcoming Text**
    - **Links to Search and Log In**

    <br>
*   The Search page includes:
    - **A filtering/search function**
    - **Excerpt listings of the experiences**

    <br>
*   The experiences page includes:
    - **More indepth description of the chosen experience**
    - **User created reviews**
    - **Option for user to submit a review**
    - **Ability to edit & delete previously posted reviews**

### 2.2 Futures left to implement 
- Add stronger delete review & experience protection. Touchscreens needs a better solution.
- Allow users to add new experiences to the database.
- A user dashboard with overview of their posted items.
- Signup/login with Facebook/Google/Etc.
- Like or up/downvote functionality to experiences and reviews
- More advanced search options, fx a search function that utilize Map Clustering

## 3. Technologies Used

### 3.1 Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)


### 3.2 Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the Roboto and Oswald fonts used throughout the site.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add icons for visual and user experience (UX) purposes.
1. [Django:](https://www.djangoproject.com/)
    - The site is build within the Django Framework.
1. [Gitpod](https://gitpod.io/)
    - Gitpod was used to develop the website.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git. And to host the project.
1. [Heroku:](https://heroku.com/)
    - Heroku is used to deploy the final website.
1. [Balsamic:](https://balsamiq.com/)
    - Balsamiq was used during the design process to create Wireframes.
1. [Responsive Design Checker:](https://www.responsivedesignchecker.com/)
    - Used in the testing process to check responsiveness on various devices.
1. [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
    - Used to validate the HTML code.
1. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate the CSS code.
1. [PEP8 Validator](http://pep8online.com/)
    - Used to validate the Python code.
1. [JSHint](https://jshint.com/)
    - Used to validate the JavaScript code.
1. [Summernote](https://summernote.org/)
    - A text editor for the admin panel.

## 4. Testing
The testing process can be found [here.](https://github.com/Lasserini/kidstravelp4/blob/main/testing.md)

## 5. Deployment

### 5.1 GitHub Pages

The site was deployed to Heroku pages using following steps:

1. Sign up or Login to Heroku
2. Click on the "new appllication", select App name and choose your region.
3. Click on "Deploy" and choose your deployment method
4. If you are connecting with Github choose your main branch and find your repository
5. Under "ressources" attach "Heroku Postgres" as Database.
6. Under "settings" -> "reveal config vars": add "CLOUDINARY_URL", "DATABASE_URL" & "SECRET_KEY" with mathing values.
7. Click on deploy manually or automatically
8. The project is now beeing deployed
9. When deployed click on "Open App"
10. If you click on settings on the main menu bar you will find your Heroku git URL

### 5.2 Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Lasserini/kidstravelp4
```

7. Press Enter. Your local clone will be created.
8. Remember to create an env.py file, install dependencies and create/update a requirements.txt file.
9. To install the required packages for this application, type the following: pip3 install -r requirements.txt

asgiref==3.5.0
cloudinary==1.29.0
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==3.2
django-allauth==0.50.0
django-filter==21.1
django-summernote==0.8.20.0
gunicorn==20.1.0
oauthlib==3.2.0
psycopg2==2.9.3
PyJWT==2.3.0
python3-openid==3.2.0
pytz==2022.1
requests-oauthlib==1.3.1
sqlparse==0.4.2

```
$ git clone https://github.com/Lasserini/kidstravelp4
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## 6. Credits

### Code

- Responsive Nav Bar code is inspired by https://www.w3schools.com/howto/howto_js_mobile_navbar.asp

### Content

-   All content was written by the developer.


### Acknowledgements

- My Mentor for continuous helpful feedback.

- Code Institute for providing me with the know-how of basic HTML & CSS necessary to complete this course.