# Testing

## 1. Code Validation
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

### 1.1 CSS Validation
The test was succesfull and did not report any issues.<br>
<img src="https://github.com/Lasserini/stine-poulsen-psykoterapeut/blob/master/validation/css_validation.png">

### 1.2 HTML Validation
The first attempt at HTML Validation gave a long list of various items that wasn't allowed in span containers, those containers were changed to divs. Some fixes to the contact formular were also required. Below is the result of the 2nd pass through the tests.
#### Index Page
<img src="https://github.com/Lasserini/stine-poulsen-psykoterapeut/blob/master/validation/index_validation.png">

#### Individual Therapy Page
<img src="https://github.com/Lasserini/stine-poulsen-psykoterapeut/blob/master/validation/individual_validation.png">

#### Couples Therapy Page
<img src="https://github.com/Lasserini/stine-poulsen-psykoterapeut/blob/master/validation/couples_validation.png">

#### About Me Page
<img src="https://github.com/Lasserini/stine-poulsen-psykoterapeut/blob/master/validation/aboutme_validation.png">

#### Price Page
<img src="https://github.com/Lasserini/stine-poulsen-psykoterapeut/blob/master/validation/price_validation.png">

#### Contact Page
<img src="https://github.com/Lasserini/stine-poulsen-psykoterapeut/blob/master/validation/contact_validation.png">


## 2. Responsiveness
To test responsiveness across various devices & screensizes, I used [Responsive Design Checkcer](https://www.responsivedesignchecker.com/), a 15`` laptop & a OnePlus 6T mobile phone.

Viewport | iPhone 5/5s<br>320x568 | Galaxy S5/S6/S/<br>360*640 | OnePlus 6T<br>412x892 | Ipad Mini<br>768x1012 | Ipad Pro<br>1366x1024 | Desktop 1024px | Desktop 1440px
--- | --- | --- | --- | --- | --- | --- | --- |
Site responsive<br>below 801px  | Good | Good| Good | Good | n/a | n/a | n/a
Site responsive<br>above 800px | n/a | n/a | n/a | n/a | Good | Good | Good
Links functionality  | Good | Good | Good | Good | Good | Good | Good
Navigation Menu  | Good | Good | Good | Good | Good | Good | Good
Images | Good | Good | Good | Good | Good | Good | Good
Renders as expected | Good | Good | Good | Good | Good | Good | Good


## 3. Browser Compatability
Browser -> | Chrome | Firefox | Edge | Safari | Opera | IE
--- | --- | --- | --- | --- | --- | --- |
Appearance  | Good | Good | Good | Decent | Good | Good
Responsiveness | Good | Good | Good | Good | Good | Good
Functionality | Good | Good | Good | Good | Good | Good

## 4. Contrast Testing
A test of colour contrast to ensure accessibility.
-   [WebAim Contrast Checkter](https://webaim.org/resources/contrastchecker/)

Black text (#3A3A3A) on white background (#FFFFFF).
- Passes all tests.

Black text (#252525) on white background (#FFFFFF).
- Passes all tests.

White text (#FFFFFF) on green background (#0f352d).
- Passes all tests.

White text (#FFFFFF) in footer on brown background (#35251a).
- Passes all tests.

Black text (#252525) on grey background (#CCCCCC).
- Passes all tests.

Green icon and hovor effect (#159D15) on dark green background (#0F352D)
- Passes tests for Graphical Objects & User Interface Components.
- It fails the test for normal text & some large text. But the website only utilize the colors together for icons and UI effects.

## 5. Testing User Stories from User Experience (UX) Section
- As an owner, I want to show my services and experience to attract more clients.<br>
    - The site provides a detailed overview of all the services the Psychotherapist offers, both in brief form on the welcome page, but also in-depth in pages dedicated to essential topics. 
    - The site also has an About Me page, that provides further background information. 
    - Furthermore, the site has contact information posted in a long list of locatins. Intended to provide the end-goal of a potential client picking up the phone and booking a therapy session.
- As an owner, I want to have an online presence for collegues to refer overflow clients to.<br>
    - Having a website allows referred clients easy access to my services and credentials.
    - Having a website gives my business a more professional image.
- As an owner, I want returning customers to have an easy way of finding me & my contact information<br>
    - The site has the Psychotherapists name & image at the top left of every page. Creating easy recognition. 
    - Contact information is clearly visible in many elements across the website, from the welcome page top content box, to the footer on every page, on the pages for individual and couples therapy, and also on a page dedicated to contact information.
    <br>
- As a user, I want to easily find the Psychotherapists contact information.<br>
    - The user will come across the Psychotherapists phonenumber on most pages, and several links leading to the Contact page.
    - The welcome page has contact information in the topmost box with key information, it also has a content box dedicated to contact information.
    - The Footer on every page has phone contact information.
    - The pages for Individual and Couples Therapy has a box with contact information. Providing a call-to-action immediatly if the information about the specific kind of therapy has pursuaded the visiting into booking a session.
    - The price page has the phone number listed, and also links to the contact page.
    - The contact page is dedicated to providing contact information, and adds a contact formular that serves as an alternative to the user making a phonecall.
- As a user, I want to book a therapy session.<br>
    - The user can find contact information on the welcome page.
    - If required, the user can easily navigate from the welcome page and onto pages detailing the therapy type thats relevant to them, information about the Psychotherapist or price information.
- As a user, I want an alternative to having to make a phone call right now.<br>
    - The welcome page highlights that there is a secondary option in the form of filling out a contact formular.
    - The contact page has a contact formular that allows the user an alternative to placing a phone call themselves.
- As a user, I want to know more about the Psychotherapist.<br>
    - The welcome page has a link to the About Me page.
    - The user can read about the Psychotherapist on the About Me page.
    - The user can find information about the Psychotherapists educational background, courses, workshops, supervision and of her past work experiences on the About Me page.
    - The user can see what therapy issues the Psychotherapist has experience with on both the Individual and the Couples Therapy pages.
- As a user, I want to know more about Gestalttherapy.<br>
    - The user can read about the therapy form that is being used on the About Me page.
- As a user, I want to read about the Individual Therapy sessions.<br>
    - The user finds a quick introduction to Individual Therapy on the welcome page. This information is supplemented by a link to the Individual Therapy page.
    - The user can find more in-depth information about the Individual Therapy on the dedicated page.
- As a user, I want to read about the Couples Therapy sessions.<br>
    - The user finds a quick introduction to Couples Therapy on the welcome page. This information is supplemented by a link to the Couples Therapy page.
    - The user can find more in-depth information about the Couples Therapy on the dedicated page.
- As a user, I want to know if the Psyhotherapist has experience with a specific issue/problem.<br>
    - The user can see what therapy issues the Psychotherapist has experience with on both the Individual and the Couples Therapy pages.
- As a user, I want to know about the prices for the services on offer.<br>
    - The user can find pricing information on the pages dedicated to Individual and Couples Therapy.
    - The user can find prices on the Price page.
    - The user can find payment options on the Price page.
- As a user, I want to find a supervisor.<br>
    - On the welcome page, the user can see that the Psychotherapist offers Supervision for both individuals and groups.
    - The user can click the provided link on the welcome page, to go to the Price page where more information is given about Supervision pricing.
    - As the primary focus of the website is to attact clients for Individual & Couples therapy, further information about Supervision will require a phonecall or filling out the contact formular.
- As a group, we want to find a group supervisor.<br>
    - On the welcome page, the user can see that the Psychotherapist offers Supervision for both individuals and groups.
    - The user can click the provided link on the welcome page, to go to the Price page where users looking for Group Supervision are instructed to place a phone call for more information.
- As a user, I want to find more information about Mental First Aid courses.<br>
    - On the welcome page, the user can see that the Psychotherapist offers a Course in Mental First Aid.
    - The user can click the provided link on the welcome page, to go to the Price page where users looking for information about the Mental First Aid Course are provided with a link to the company that handles bookings and questions about these courses.
- As a user, I want to know how the Psychotherapist is applying Covid-19 precautions.<br>
    - On the Price page the user can find information about Covid-19 precautions.
    - On the Contact page the user can find information about the Covid-19 precautions.
- As a user, I want to cancel/change an appointment.<br>
    - The user can find contact information on all pages throughout the site.
    - The user can find out how to cancel or change an appointment on the price and contact pages.
    - The user can find the conditions that apply to canceling or changing a booking on the price and contact pages.


## 5. Known Bugs
- On devices with a viewport height below 600px there was an issue with the dropdown navigation menu. The menu was locked in place & didn't scale, which caused an issue on the very smallest of phones. Bugfix: Applied a change that makes the menu list items scale with viewport height.
- There was a validation issue on the about me page. The problem was identified as headings being used inside a paragraph. Bugfix: A restructuring of the content box fixed the issue.
- The Contact Formular isn't working yet. The backend required will be added in a future update.
- The navigation menu was too large for midsize screens (i.e. 800px to 970px), using the small nav bar at such a large screensize felt off. So instead a solution with reduced font-size at that range of screens is applied.