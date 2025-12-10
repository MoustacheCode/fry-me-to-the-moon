

![Fry Me to the Moon Header](./media/logo_2.png)


## Introduction

[Provide a brief overview of your project. Explain what the application does, its main purpose, and who the target users are. Include a high-level description of the problem it solves and key features.]

### Project Overview
- **Project Name:** Fry Me to the Moon
- **Purpose:** To upload, discover and share your own unique recipes
- **Target Audience:** Anybody who has an interest in Cooking/Baking
<details>
<summary><strong>Technologies Used</strong></summary>

- **Front End:** HTML5, CSS, Bootstrap 5, JavaScript
- **Back End:** Python, Django
- **Database:** SQLite, PostgreSQL
- **Frameworks:** Bootstrap, Cloudinary, Django, gunicorn, pyscopg2
- **Tools:** Flake8, Black (For linting and formating to pep8 standards)

</details>

---

## UX Design

### Design
The main design rules were to follow the Name of the website, keeping it light and Jazz themed, adding in an essence of a Jazz Resteraunt. Initially the project was aimed to be a user driven interactive web book, which may be implemented post deadline.

Some of the current features are:

- Animated Nav Bar - Moon effect logo, twinkling stars and animated clouds
- Recipe Cards clearly depicting the recipe and type of recipe
- Restaurant style Recipe Card
- Interactive Polaroid for each Recipe with Hover over
- "Meal Receipt" Comments board, each comment randomly "placed" down, with Hover over
- "Flares" softly animated in the background to add effect to the theme

<details>
<summary><strong>User Stories</strong></summary>

[Amongst the user stories located on the Project Board, the below are those that I was able to fulfill within the deadline:]
- As a registered user, I want to upload my own recipe with images so that I can share my creations with the community.
- As a registered user, I want to edit or delete my recipes so that I can keep my content up to date.
- As a visitor, I want to view a recipe with ingredients, steps, and cooking time clearly laid out so that I can follow it easily.
- As a visitor, I want to see images alongside recipes so that I know what the finished dish should look like.
- As a visitor, I want to browse recipes by category (e.g., desserts, mains, vegan) so that I can quickly find what I’m interested in.
- As a registered user, I want to comment on recipes so that I can share tips or ask questions.
- As a visitor, I want to navigate recipes easily on mobile and desktop so that I can cook from any device.

</details>

<details>
<summary><strong>Wireframes & Mockups</strong></summary>

After realising that I wouldn't be able to achieve an interactive book within the time frame, I pivoted and decided to try and give a "Jazz Restaurant" feeling to the site. The wireframes below show initial conception for the 2 main pages in the project.

![Wireframe 1](./media/wireframe-home.JPG)

![Wireframe 2](./media/wireframe-view.JPG)

</details>

<details>
<summary><strong>Color Scheme & Typography</strong></summary>

**Color Palette:**
A lot of colours over all went in to bringing the design to life, but the Core 5 can be viewed below:

![Colors](./media/colors.png)

**Typography:**
Trying to achieve a classy feel, I used the following fonts:

- Alex Brush
- Caveat
- Patrick Hand
- Quintessential

</details>

### Responsive Design
<details>
<summary><strong>Click to view Responsive Design details</strong></summary>

The application is designed to be fully responsive, ensuring a seamless user experience across various devices and screen sizes. Key features of the responsive design include:

- **Fluid Grid Layout:** The layout adjusts dynamically based on the screen size, using percentage-based widths for elements.
- **Media Queries:** CSS media queries are employed to apply different styles for different screen sizes, ensuring optimal readability and usability.
- **Flexible Images:** Images are set to a maximum width of 100%, allowing them to scale appropriately within their containers.
- **Mobile Navigation:** A collapsible navigation menu is implemented for mobile devices, providing easy access to all sections without overwhelming the user.

This approach guarantees that users can interact with the application effectively, whether on a desktop, tablet, or smartphone.
![Responsive Design Example](./media/responsive.png)
</details>

---

## Agile

### Agile Methodology
[Describe your agile approach - Scrum, Kanban, etc.]

---

## Entity Relationship Diagram (ERD)

<details>
<summary><strong>Click to view Entity Relationship Diagram</strong></summary>

![Entity Relationship Diagram](./media/ERD.png)

</details>

---


---

## Features

### Core Features
1. **User Authentication**
   - User registration and login

2. **Recipe Management**
   - Create, read, update, and delete recipes
   - Recipe categorization
   - Image uploads for recipes

3. **User Interactions**
   - Comment on recipes
   - Share recipes

4. **Search & Filter**
   - Search recipes by name or ingredients
   - Filter by category

### Future Features
- [Generate the interactive "Cook book" effect so users can feel like they're recipes are found in the traditional method]
- [Performance enhancements to ensure a smoother experience for the user.]

---

<details>
<summary><strong>AI Implementation</strong></summary>

AI was very helpful when it came to building Fry me to the Moon. Treating it as a Senior Developer, asking it the correct questions to guide me to the right outcome.

- Co-Pilot was used to help generate Bootstrap code quickly and efficiently
- Provided swift suggestions for color matching and styling
- Generated a Readme Template for me to populate
- Used in Conjunction with Course Materials for debugging

</details>

---

## Deployment

### Deployment Platform
- **Platform:** [e.g., Heroku, AWS, PythonAnywhere, etc.]
- **Environment:** [Production/Staging details]

## Testing


### Unit Tests
<details>
<summary><strong>Forms Tests</strong></summary>

![Forms](./media/forms_test.JPG)
![Forms](./media/testformcode.JPG)

</details>

<details>
<summary><strong>Views Tests</strong></summary>

![Views](./media/views_test.JPG)
![Views](./media/testviewscode.JPG)

</details>

<details>
<summary><strong>URLs Tests</strong></summary>

![URLs](./media/urls_test.JPG)
![URLs](./media/urlstestcode.JPG)

</details>

<details>
<summary><strong>Models Tests</strong></summary>

![Models](./media/recipe_model_test.JPG)
![Models](./media/modelstest.JPG)

</details>



### Integration Tests
<details>
<summary><strong>Integration Tests</strong></summary>

![Integration](./media/testcase_integrations.JPG)
![Integration](./media/integration-flow.JPG)

</details>


## External Testing and Validation


#### Recipe List Page
<details>
<summary>Click to view Recipe List screenshot</summary>

![Recipe List Page](./media/desktop_home_lighthouse.JPG)
![Recipe List Page](./media/mobile_home_lighthouse.JPG)

</details>

#### Recipe Details Page
<details>
<summary>Click to view Recipe Details screenshot</summary>

![Recipe Details Page](./media/recipe_view_lighthouse_desktop.JPG)
![Recipe Details Page](./media/recipe_view_lighthouse_mobile.JPG)

</details>

#### Login Page
<details>
<summary>Click to view Login screenshot</summary>

![Login Page](./media/login_lighthouse_desktop.JPG)
![Login Page](./media/login_lighthouse_desktop.JPG)

</details>

#### Logout Page
<details>
<summary>Click to view Logout screenshot</summary>

![Logout Page](./media/logout_lighthouse_desktop.JPG)
![Logout Page](./media/logout_lighthouse_mobile.JPG)

</details>

#### Edit Recipe Page
<details>
<summary>Click to view Edit Recipe screenshot</summary>

![Edit Recipe Page](./media/edit_lighthouse_desktop.JPG)
![Edit Recipe Page](./media/edit_lighthouse_mobile.JPG)

</details>

#### Delete Recipe Page
<details>
<summary>Click to view Delete Recipe screenshot</summary>

![Delete Recipe Page](./media/delete_lighthouse_desktop.JPG)
![Delete Recipe Page](./media/delete_lighthouse_mobile.JPG)

</details>

#### HTML & CSS Testing
<details>
<summary>Click to view HTML & CSS Testing details</summary>

**HTML Validation:**
- All pages validated using W3C HTML Validator
- No critical errors or warnings
- Semantic HTML5 structure implemented throughout

![HTML](./media/base-validation.JPG)

**CSS Testing:**
- CSS validated using W3C CSS Validator
- Cross-browser compatibility tested (Chrome, Firefox, Safari, Edge)
- Media queries verified for responsive breakpoints
- Bootstrap 5 framework validation passed

![CSS](./media/css-validation.JPG)

**Accessibility:**
- WCAG 2.1 compliance verified
- Color contrast ratios meet AA standards
- Alt text present on all images
- Keyboard navigation tested and functional

</details>



### User Testing
During deployment, once the functionality of the website was achieved, I asked a number of individuals to go on, register, add recipes or comments and report back any findings.

As of today, any issues with uploading images has been resolved, and all the active recipes are user uploaded, and the process as detailed above in the Python test, works from Registering, Viewing, Adding a Recipe, leaving a comment, logging out. 


#### Recipe Added Success Page
<details>
<summary>Click to view Recipe Added Success screenshot</summary>

![Recipe Added Success](./media/recipe_submit.JPG)


</details>

#### Logged Out
<details>
<summary>Click to view Logged Out screenshot</summary>

![Logged Out](./media/logged-out.JPG)

</details>

### Feedback & Improvements
[Summarize feedback received and improvements made based on external testing]

---

## Getting Started


### Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Configure environment variables
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`


---

## Credits and Acknowledgements

### Project Team
- **Developer(s):** Richard Duerden



### Third-Party Services
- [Cloudinary] - Image hosting and management

### Resources & References
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [FreeFrontEnd](https://freefrontend.com/css-animated-backgrounds/page/2/)
- [Eraser.io](https://app.eraser.io/workspace/I2ctBmT5eFPguCVwpBPI)

### Special Thanks
[Thank you to Code Institute for their guidance and preperation to be able to build this project]

---