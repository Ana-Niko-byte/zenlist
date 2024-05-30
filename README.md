## Note: This application and its README is Work-In-Progress.

# Zenlist
The application is available for viewing [here](https://zenlist-b604919b54d1.herokuapp.com/).

## A Little Bit About Zenlist
Zenlist is a task-tracking Django application, designed to provide users an easy and quick way of organising and managing day-to-day tasks for different environments. With custom filtering systems and an intuitive interface, zenlist is the perfect go-to for anyone who wishes to improve their time-management skills and stay on top of their day.

# Business/Social Goals
- Allow for organisation/categorisation of assets in a clear system (user-created environments) to make the platform easily accessible and understandable.

- Design the platform to be accessible for all ages (or at minimum for those over 12 years of age).

- Set up a visual alert for tasks approaching due date. 

- Set up an email alert for registration and account authentication.

- Spread knowledge of the Scrum framework and explain how this framework benefits workplaces and personal time-management. Add links to relevant medias and opensource documents. 

# UX Goals
- Create a simple and intuitive UI for young and first time users to foster a sense of comfort and reassurance. 

- Design a simple and easy navigation system (primary navigation and breadcrumbs so the user knows where they are at all times and can back track when needed).

- Establish a colour scheme and font family that ties the theme of _zen_ together to create a cohesive and comprehensive branding with accents in both where needed.

- Keep the application visually minimalistic with white spacing and simple accents to maintain the _zen_ theme and branding. 

# Wireframes
![zenlist wireframe](static/images/zenlist-wireframe.png)
# Structure 
All pages contain the same navigation and footer sections.
The structure of _Zenlist_ is as follows: 
### Scrum Home Page
This is the main home page of the project. Though it does not have a conventional 'Home' page, its root page is the starting point of Zenlist, deep diving into scrum methodology and providing potential users with information on the app (attention-grabbing header, reviews, an introduction to the scrum methodology for time-management).

- #### Jumbotron
    - If not signed in, the jumbotron displays a signup button and an advertising heading.

    - If signed in, the jumbotron displays a button to access the user's workspaces and an encouraging title.
- #### Reviews
    - These reviews are filtered by stars and displayed in a row to site visitors. 

    The app can only be reviewed by logged in users, and all reviews require approval from an administrator prior to being displayed on the home page. Additionally, the user is presented with a button to read all reviews for the application, which redirects to a standalone page. This page is not presented in the navigation bar, but users can return to a page of their choosing by selecting existing links in the navigation bar. 
- #### Scrum Paragraph
    - A concise paragraph explaining the scrum methodology and its benefits in every day use. This paragraph serves as an introduction to the framework for anyone not already familiar with it and contains a helpful link to the official Scrum.org website, where users may download the free Scrum Guide 2020 (the latest revision). 

- #### Review Form
    - If users are logged in, they are presented a form to leave an application review. 

    - If users are logged out, they are presented a button and a prompt to log in to leave a review.

### Contact 
This is a contact page for users to send queries to the Zenlist team (connected to my email: ananikolayenia@gmail.com).

### Your Workspaces
Note: This page is only visible in the navigation bar to logged in users. 
This is a list of workspaces belonging to the user. This page also contains a 'due today' column with lists of tasks that are due in each workspace. If there are no due tasks, a congratulatory message is displayed to the user. 

- #### Workspace List 
    - Workspace Name

    - Total number of tasks in workspace.

    - Delete Workspace Button
- #### Due Today List
    - Number of tasks in each space due on a particular day.

- #### Add Workspace Button
    - Modal with title field input.

    - Messages to tell user the workspace was successfully created.

### Sign in/Sign Up
This is only displayed when the user is not signed in. 
- A page where the user may signup/signin, using allauth Django.

- An email authentication prompt for users who have just signed up.

- Visual indication that the user is signed in (jumbotron + '_Your Workspaces_- tab in navigation bar).

### Logout
This is only displayed when the user is signed in. 
- A page where the user may logout, using allauth Django.

- Visual indication that the user has signed out (jumbotron + no '_Your Workspaces_' tab in navigation bar).

---
# Scope of Application
The application is scope is currently to the following: 

### User Interaction
Once registered and logged in, the user can access their zenlists in the _Your Workspaces_ tab. All tasks (due, in progress and completed) are visible within their relevant zenlists. The user can add another task to the list via the form on the left-hand side. Here they give a title, assign a category, a due date, a priority, and a brief description to the task they wish to add. Once finished and logged, the user may:
- Open the task accordion item (through the 'click' event) to view the task details (due-date, priority (colourful dot), and any associated notes).

- Edit the task (using the form on the left-hand side of the page).

- Change the task's status, in which case the user receives a confirmation message following a successful update, and visual confirmation of the task under the relevant status list.

- Delete the task. 

### Categorisation
The purpose of zenlist is to allow users to categorise their day into environments. Each environment, i.e., home-chores, study-related tasks, etc., separate from each other. Each of these spaces presents any tasks due on a particular day on the home page of the '_Your Workspaces_' tab, on the left hand side of the page.

### Filtering
To enable users to comfortably control their tasks, a filtering system was adopted to allow for quick access to all relevant data. The tasks can be filtered by the following: 
- _by priority_
- _by due date_
    - _by approaching_
    - _by way-off_
    - _by late tasks_

### Scrum & Agile Knowledge Sharing

# Aesthetics
# Strategy
This application aims at optimising task and time management by leveraging the benefits of an intuative and minimalist UI, visual reminders of approaching task due dates, and an easy and accessible filtering system.

The application is designed as a mobile-first app, with an easy to use UI with hints where necessary. 

# Target Audience
- Users over 12 years of age. 
- Hobbyists.
- Students.
- Anybody who wishes to improve their time-management skills. 

# Key Information Deliverables
- Categorisation of tasks by environment.
- Time-tracking capabilities with visual reminders for approaching tasks.
- Filtering system (by space, by priority, by due date).
- Ability to add/view/edit/delete assets. 

# Features


# Technologies
1. HTML5/ Django Templates - Used for structuring and content.
2. CSS3 - Used for adding styles to the content for legibility and aesthetic appeal.
3. Vanilla Javascript - For adding basic interactivity and dynamically setting URLs.
4. FontAwesome/Boostrap icons - used for icons.
5. Emojipedia - used for emojis.
6. Firefox Developer Tools - used for debugging the website during production.
7. Lighthouse - An extension I used for testing the performance, accessibility, best practices and SEO of my site (result shown under debugging below).
8. GitHub - For code storage,version control and deployment.
9. Git - For commiting through terminal and pushing to Github for storage.
10. VSC - The IDE I developed the project in.
11. Balsamiq - For a clear understanding of the structure I wanted my application to follow. The project has since deviated slightly from the design for improved user experience.
12. Color Contrast Accessibility Validator - check legibility of my text on different backgrounds for better accessibility.
13. W3C Markup Validation Service - to validate my HTML for potential errors.
14. W3C CSS Validation Service - to validate my CSS code for potential errors.
15. JSHint - for checking and validating my JS code. 
16. Pep8 - for Python code validation and best practices formatting.
17. Freeformatter CSS Beautify - to ensure I formatted my CSS correctly.
18. Beautifier.io - to beautify my JS. 
19. AmIResponsive - to create the responsive image.

# Testing & Debugging
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
||||| <img src="docs/images/thumbs-up.jpg"> |
### Issues
### Debugging
# Accessibility & Performance
### Lighthouse

### Colour Accessibility Validator 

### HTML Validation

### CSS Validation

### JSHint Validation

# Deployment
The application is deployed on Heroku through github, and is available for viewing in the link at the top of this README.md document. To deploy a Heroku project, follow the following steps: 

# Future Development
Email Notifications for approaching tasks. This was going to be implemented with Celery, Redis, and django-celery-beat, but the emails weren't sending for some reason. 

# Credits
For help with Django [queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/).

For some help in setting up [email verification](https://www.codesnail.com/django-allauth-email-authentication-tutorial/) on signup.

For help understanding Django [get_queryset() and get_context_data()](https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django) for conditionally rendering workspaces.

For help understanding how to create a [slug from a title](https://stackoverflow.com/questions/72944678/django-how-to-create-slugs-in-django)

Changing [all-auth styling for emails](https://www.reddit.com/r/django/comments/t5o51d/customising_the_djangoallauth_verification_email/)

For removing the background from image: [remove bg](https://www.remove.bg/upload)

This awesome GeeksforGeeks page for helping to understand [CBV DeleteView](https://www.geeksforgeeks.org/deleteview-class-based-views-django/)

For help understanding how to generate unique ids for the accordion elements using Django's [forloop.counter](https://stackoverflow.com/questions/1107737/numeric-for-loop-in-django-templates) in Stack Overflow and [Dev](https://dev.to/swesadiqul/activate-the-first-bootstrap-collapse-in-django-for-dynamic-data-3b22).

For [date picker](https://mrasimzahid.medium.com/how-to-implement-django-datepicker-calender-in-forms-date-field-9e23479b5db)

[Date.toISOString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString) for date input in HTML. 

# Acknowledgements