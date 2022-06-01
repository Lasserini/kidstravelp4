# Testing

## 1. Code Validation
The following validators were used.
1. [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
    - Used to validate the HTML code.
1. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate the CSS code.
1. [PEP8 Validator](http://pep8online.com/)
    - Used to validate the Python code.
1. [JSHint](https://jshint.com/)
    - Used to validate the JavaScript code.

### 1.1 CSS Validation
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/css_validation.png">

### 1.2 HTML Validation
### Index Page
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/index_html_validation.png">

### Results Page
- Django adds various table tags to the elements the site pulls from a data model. The validator doesn't like that, I'm unsure of how to fix it though.
- I've made a concious decision to break the "no button in A tag" rule. The site has significant issues with "overflowing" A-tags, inparticular the delete item tags being out of place was too large of an issue to ignore. Attempted several other fixes before resorting to this method.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/results_html_validation.png">

### Experience_Detail Page
- Django adds various table tags to the elements the site pulls from a data model. The validator doesn't like that, I'm unsure of how to fix it though.
- I've made a concious decision to break the "no button in A tag" rule. The site has significant issues with "overflowing" A-tags, inparticular the delete item tags being out of place was too large of an issue to ignore. Attempted several other fixes before resorting to this method.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/experiencedetail_html_validation.png">

### Add_Experience Page
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/addexperience_html_validation.png">

### Edit Experience Page
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/editexperience_html_validation.png">

### Edit Review Page
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/editreview_html_validation.png">


### 1.3 JavaScript Validation
### script.js validation
Nothing of concern. The "unused" variable is being called from the html with "onclick"<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/scriptJS_validation.png">

### scroll.js validation
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/scrollJS_validation.png">

### 1.4 Python Validation
### models.py:
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/models_validation.png">

### views.py:
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/views_validation.png">

### forms.py
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/forms_validation.png">

### urls.py
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/urls_validation.png">

### filters.py
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/filters_validation.png">

### admin.py
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/validation/admin_validation.png">


## 2. Responsiveness
To test responsiveness across various devices & screensizes, I used [Responsive Design Checkcer](https://www.responsivedesignchecker.com/), a 17`` laptop & a OnePlus 6T mobile phone.

Viewport | iPhone 5/5s<br>320x568 | Galaxy S5/S6/S/<br>360*640 | OnePlus 6T<br>412x892 | Ipad Mini<br>768x1012 | Ipad Pro<br>1366x1024 | Desktop 1024px | Desktop 1440px
--- | --- | --- | --- | --- | --- | --- | --- |
Site responsive<br>below 900px  | Good | Good| Good | Good | n/a | n/a | n/a
Site responsive<br>above 900px | n/a | n/a | n/a | n/a | Good | Good | Good
Links functionality  | Good | Good | Good | Good | Good | Good | Good
Navigation Menu  | Good | Good | Good | Good | Good | Good | Good
Images | Good | Good | Good | Good | Good | Good | Good
Renders as expected | Good | Good | Good | Good | Good | Good | Good


## 3. Browser Compatability
Browser -> | Chrome | Firefox | Edge | Safari | Opera
--- | --- | --- | --- | --- | --- |
Appearance  | Good | Good | Good | Decent | Good
Responsiveness | Good | Good | Good | Good | Good
Functionality | Good | Good | Good | Good | Good


## 4. Testing User Stories from User Experience (UX) Section
- As an owner, I want to post new activities, so the site offers stronger value.<br>
    - The sites admin panel allows for easy creation of new activities/experiences.
    - The newly added experiences integrate flawlessly into the data model and site rendering.
    - A large amount of dropdown panels with preset values makes the task of adding more content fairly simple.
    - Site admins also have access to adding new experiences directly from the Front End.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/addbutton.png">
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/addexperience.png">

- As an owner, I want to provide users with quality content.<br>
    - The added experiences are easy to find, and the backend datamodel supports adding ample relevant information.
    - Users can post reviews, allowing up-to-date information about the experiences listed.
- As an owner, I want allow users to create a profile.<br>
    - Users can create a profile.
    - Having a profile allows the users to utilize more site features, such as post a review.
    - The site has several "call-to-actions" for unregistered users.
    <br>
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/signin.png">
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/loginrequired.png">
- As a user, I want to find travel activities for my children.<br>
    - The user can go straight to the find activities section from the nav bar.
    - The index page has a "Get Started" call-to-action to allow users to navigate there quickly.
    - The search function allow users to filter for relevant activities.
    - In this demo version the user can find travel activities for travels to Copenhagen & Florence.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/findexperiences.png">
- As a user, I want to share how an activity was for me.<br>
    - The user can add a review below all experiences.
    - The user can give the experience a rating of 1 to 5 stars.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/reviews.png">
- As a user, I want an search by category.<br>
    - The user can search by category, quickly filtering irrelevant items away.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/categorysearch.png">
- As a user, I want an search by city.<br>
    - The user can search by city.
    - The user can combine searching by city with other parameters, i.e. category. This provides a quick method for finding fx "a cafe in Florence" thats kids friendly.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/citysearch.png">
- As a user, I want an create a user account.<br>
    - The user can create a user account.
    - The user account allows the user to access more of the sites functionality.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/signup.png">
- As a user, I want to edit one of my reviews.<br>
    - Under their own reviews, users are presented with an option to edit their review.
    - The edit formular prepopulates the forms with the excisting review, and the user can then edit and update headling, text and as desired.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/editreview.png">
- As a user, I want to delete one of my reviews.<br>
    - Under their own reviews, users are presented with an option to delete their review.
    - (on desktop) user is asked to confirm deletion. This functionality is still lacking on mobile.
<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/deletereview.png">


## 5. Django Admin Panel testing
- I have tested Django Administration. Summernote works, the filters work, adding and editing experiences and reviews work.
Deleting experiences and reviews are also working as intended.

- The FrontEnd also features some additional add, edit & delete functionality for admins. These also work as intended.

<img src="https://github.com/Lasserini/kidstravelp4/blob/main/media/testing/admin_panel.png">

## 6. Known Bugs
- **Fixed** Posting a review was bugged, throwing back a "username-id" value = null. Fixed by adding some backend data to the POST method view.

- **Fixed** The NavBar pushing content down has been adressed, for desktop a normal nav list was added & for mobile the pushing down content has been changed to look much better.

- **Fixed** Image rendering on large devices has been improved for version 2 of the site. Site looks and performs much better on desktop now.

- Rendering from the data models is causing HTML validation issues. Considering trying to load more data forms as paragraphs, would require a rethink for the pages that only select a few values from the models.

- The delete functionality for both experience and reviews could be improved with better designed confirmation checks. Solved so far with some very aggresive mouseover confirm boxes.

- The forms for adding and editing experiences and reviews are functional, however their visual appeal definately needs improvement.

