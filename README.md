# Fry Me to the Moon

![Fry Me to the Moon Header](./media/logo.JPG)

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

</details>

---

## UX Design

### Design
The main design rules were to follow the Name of the website, keeping it light and Jazz themed, adding in an essence of a Jazz Resteraunt. Initially the project was aimed to be a user driven interactive web book, which may be implemented post deadline.

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

### Wireframes & Mockups
[Include links or descriptions of wireframes and design mockups]

### Color Scheme & Typography
[Describe the color palette and typography choices]

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

### Sprint Planning
[Document your sprint cycle and planning process]

### User Stories & Acceptance Criteria
[List key user stories with acceptance criteria]

### Sprint History
| Sprint | Duration | Goals | Status |
|--------|----------|-------|--------|
| Sprint 1 | [Dates] | [Goals] | Completed |
| Sprint 2 | [Dates] | [Goals] | Completed |
| Sprint 3 | [Dates] | [Goals] | In Progress |

### Burndown Charts & Metrics
[Include links to or descriptions of project metrics and burndown data]

---

## Entity Relationship Diagram (ERD)

### Database Schema
[Describe your database structure and key entities]

### ER Diagram
```
[Include ASCII diagram or link to visual diagram]

Example:
+---------+          +-----------+
| Recipe  |----------|  Comment  |
+---------+          +-----------+
    |
    |
    v
+---------+
|  User   |
+---------+
```

### Key Models
- **User:** [Description of user model and fields]
- **Recipe:** [Description of recipe model and fields]
- **Comment:** [Description of comment model and fields]
- [Add other models as needed]

---

## Features

### Core Features
1. **User Authentication**
   - User registration and login
   - Password reset functionality
   - User profile management

2. **Recipe Management**
   - Create, read, update, and delete recipes
   - Recipe categorization
   - Image uploads for recipes

3. **User Interactions**
   - Comment on recipes
   - Rate recipes
   - Share recipes

4. **Search & Filter**
   - Search recipes by name or ingredients
   - Filter by category or difficulty level

### Future Features
- [List planned features]
- [List potential enhancements]

---

## AI Implementation

### AI Features
[Describe any AI/ML features integrated into the application]

### Algorithms & Models Used
[Explain the AI models, algorithms, or services used]

### Implementation Details
[Provide technical details about how AI is implemented]

### Performance & Limitations
[Discuss performance metrics and any limitations of the AI implementation]

### API Integration
[If using external AI services, document the API integration]

---

## Deployment

### Deployment Platform
- **Platform:** [e.g., Heroku, AWS, PythonAnywhere, etc.]
- **Environment:** [Production/Staging details]

### Deployment Steps
1. [Step 1 - Preparation]
2. [Step 2 - Building]
3. [Step 3 - Testing]
4. [Step 4 - Deployment]

### Environment Variables
[Document required environment variables]
```
DATABASE_URL=
SECRET_KEY=
DEBUG=False
ALLOWED_HOSTS=
```

### Database Migrations
```bash
python manage.py migrate
```

### Static Files
```bash
python manage.py collectstatic
```

### Maintenance & Monitoring
[Describe monitoring, logging, and maintenance procedures]

---

## Testing

### Testing Strategy
[Describe your overall testing approach]

### Unit Tests
[Document unit tests for key components]

### Integration Tests
[Document integration tests]

### Running Tests
```bash
python manage.py test
```

### Test Coverage
[Include test coverage metrics or link to coverage reports]

### Key Test Cases
| Feature | Test Case | Status |
|---------|-----------|--------|
| [Feature] | [Test description] | Pass/Fail |
| [Feature] | [Test description] | Pass/Fail |

---
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


### User Testing
[Describe user testing sessions conducted]
- **Number of Testers:** [#]
- **Test Date:** [Date]
- **Feedback Summary:** [Key findings]

### Accessibility Testing
- **WCAG Compliance Level:** [A, AA, or AAA]
- **Testing Tools Used:** [e.g., Lighthouse, axe DevTools]
- **Results:** [Summary of accessibility audit]

### Performance Testing
- **Load Testing Results:** [Include key metrics]
- **Response Times:** [Document average response times]
- **Browser Compatibility:** [List tested browsers]

### Security Testing
[Document security testing and validation]
- **Penetration Testing:** [Results and findings]
- **Security Vulnerabilities:** [Document any issues found and resolved]

### Feedback & Improvements
[Summarize feedback received and improvements made based on external testing]

---

## Credits and Acknowledgements

### Project Team
- **Developer(s):** [Your name/team]
- **Designer(s):** [Designer name(s)]
- **Project Manager:** [PM name]

### Technologies & Frameworks
- Django
- Python
- PostgreSQL / SQLite
- Bootstrap / CSS Framework
- [Other libraries and tools]

### Third-Party Services
- [Service 1] - [Purpose]
- [Service 2] - [Purpose]
- [Cloudinary] - Image hosting and management

### Resources & References
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Any other resources, tutorials, or references used]

### Special Thanks
[Thank any mentors, instructors, peers, or community members who contributed to the project]

---

## Getting Started

### Prerequisites
- Python 3.9+
- Django 4.0+
- [Other requirements]

### Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Configure environment variables
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`

### Usage
[Provide instructions on how to use the application]

---

## License
[Include license information if applicable]

---

**Last Updated:** December 8, 2025