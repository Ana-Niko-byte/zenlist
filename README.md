## Note: This application and its README is Work-In-Progress.

# Zenlist
The application is available for viewing [here](https://zenlist-b604919b54d1.herokuapp.com/).

## A Little Bit About Zenlist
Zenlist is designed to provide an easy and quick way of organising and managing day-to-day tasks in different environments. Complete with organise-by-environment functionality, time-tracking, and alerts for upcoming tasks, zenlist is the perfect go-to for anyone who wishes to improve their time-management skills and stay up to date on their day. 

# Business/Social Goals
- Allow for organisation/categorisation of assets in a clear system (user-created environments) to make the platform easily accessible and understandable.

- Design the platform to be accessible for all ages (or at minimum for those over 12 years of age).

- Set up a visual alert for tasks approaching due date. 

- Set up email alerts for personalised experiences and functional reminders. 

- Set up an email alert for registration.

- As a certified Scrum Master II, spread knowledge of the scrum framework and explain how this framework benefits workplaces and personal time-management. Add links to relevant medias and opensource documents. 

# UX Goals
- Create a simple and intuitive UI for young and first time users to foster a sense of comfort and reassurance. 

- Design a simple and easy navigation system (primary navigation and breadcrumbs so the user knows where they are at all times and can back track when needed).

- Set up email alerts for personalised experiences and functional reminders. 

- Establish a colour scheme and font family that ties the theme of _zen_ together to create a cohesive and comprehensive branding with accents in both where needed.

- Keep the application visually minimalistic with white spacing and simple accents to maintain the _zen_ theme and branding. 

# Wireframes
![zenlist wireframe](static/images/zenlist-wireframe.png)
# Structure 
All pages contain the same navigation and footer sections.
The structure of _Zenlist_ is as follows: 
### Scrum Home Page
This is the main home page of the project. Though it does not have a conventional 'Home' page, its root page is the starting point of Zenlist, deep diving into scrum methodology and providing potential users with information on the app (reviews, features, and a contact option for more information).

- Jumbotron
    - If not signed in, the jumbotron displays a signup button and a different summary heading.
    - If signed in, the jumbotron displays a button to access the user's workspaces and an encouraging title.
- Reviews
    - These reviews are filtered by stars (at the moment 4 stars, but this query will be modified to look for 4+ stars), and displayed in a row to the potential users. These reviews can only be made by a logged in user, and do not require approval from any administrators, as they are filtered. Consideration is being given towards having a button to show all reviews. 
- Features
    - Feature 1
    - Feature 2
    - Feature 3
### Your Workspaces
This is a list of workspaces belonging to the user. This page also contains some basic analytics (quantity of tasks/workspace), and a visual indication of what tasks are approaching their due dates. 

- Workspace List 
    - Delete Workspace Button
- Workspace Analytics
    - Total Tasks
    - To Do Task Quantity
    - In Progress Task Quantity
    - Completed Task Quantity
- Due Today Alerts
    - Visual Display in left-side panel.
    - Email alerts.
- Add New Workspace Button
    - Modal with title field input.
    - Messages to tell user the workspace was successfully created.
### Sign in/Sign Up
This is only displayed when the user is not signed in. 
- A page where the user may signup/signin, using allauth Django.
- An email confirmation for users who have just signed up.
- Visual indication that the user is signed in (jumbotron).
### Logout
This is only displayed when the user is signed in. 
- A page where the user may logout, using allauth Django.
- Visual indication that the user has signed out (jumbotron).

---
# Scope of Application
The application is scope is currently to the following: 

### User Interaction
Once registered and logged in, the user can access their zenlists in the _Your Workspaces_ tab. All tasks (due, in progress and completed) are visible within their relevant zenlists. The user can add another task into the _to do_ section by clicking the '+' sign. Here they give a title, assign a category, a due date, a priority, and a brief description to the task they wish to add. Once finished and logged to the _to do_ body, the user may:
- view (through the 'click' event).
- edit the task (change anything except the task name).
- move the task to a different list.
- delete the task as needed. 

### Categorisation
When creating a zenlist, the user is presented with a selection of _categories_ for their environment - this helps keep work tasks separate from home chores, from study-related tasks, separate from hobbies.

### Filtering
To enable users to comfortably control their tasks, a filtering system was adopted to allow for quick access to all relevant data. The tasks can be filtered by the following: 
- _by category_
- _by priority_
- _by due date_
    - _by approaching_
    - _by way-off_
    - _by late tasks_

### Email Reminders
As a task is approaching its due date, an email reminder is sent to the user's registered address (the one used to sign up to _zenlist_).

### Scrum & Agile Knowledge Sharing

# Aesthetics
# Strategy
This application aims at optimising task and time management leveraging the benefits of an accessible and intuative UI, timely reminders connected to registered email addresses, a customisable categorisation and filtering system, and the ability to manage assets with ease. 

The application is designed as a mobile-first app, with an easy to use UI with hints where necessary. 

# Target Audience
- Users over 12 years of age. 
- Hobbyists.
- Students.
- Anybody who wishes to improve their time-management skills. 

# Key Information Deliverables
- Categorisation of assets.
- Time-tracking capabilities with email alerts for approaching tasks.
- Filtering system (by category, priority, due date).
- Ability to add/view/edit/move/delete assets. 

# Features
# Technologies
1. HTML5 - Used for structuring and content.
2. CSS3 - Used for adding styles to the content for legibility and aesthetic appeal.
3. Vanilla Javascript - To add the interactivity, validation and page display toggling for the application to work.
4. FontAwesome - used for icons.
5. Firefox Developer Tools - used for debugging the website during production.
6. Lighthouse - An extension I used for testing the performance, accessibility, best practices and SEO of my site (result shown under debugging below).
7. GitHub - For code storage,version control and deployment.
8. Git - For commiting through terminal and pushing to Github for storage.
9. VSC - The IDE I developed the project in.
10. Balsamiq - For a clear understanding of the structure I wanted my application to follow. The project has since deviated slightly from the design for improved user experience.
11. Color Contrast Accessibility Validator - check legibility of my text on different backgrounds for better accessibility.
12. W3C Markup Validation Service - to validate my HTML for potential errors.
13. W3C CSS Validation Service - to validate my CSS code for potential errors.
14. JSHint - for checking and validating my JS code. 
15. Freeformatter CSS Beautify - to ensure I formatted my CSS correctly.
16. Beautifier.io - to beautify my JS. 
16. AmIResponsive - to create the responsive image.
17. Looka.com - for logo ideas (Ai tool). -->

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
The application is deployed on Gitpages through github, and is available for viewing in the link at the top of this README.md document. To deploy a github repository, follow the following steps: 

1. Login to your github account
2. Click on your repository section under your profile icon, and select the repository you want to deploy.
3. Once you are in your repository, click ' Settings' in the top bar. 
4. Select 'Pages' from the menu on the left. 
5. Ensure the 'Source' section is set to 'Deploy from a branch'.
6. Ensure you deploy from the main branch in your root directory. The screen should look something like this: 
<!-- ![github pages](docs/images/github-one.png) -->
7. The site you want to deploy is given a URL, available above the source section, as in the image above. It might take a while for this link to become visible and active. 

### Forking a Github Repository
If you want to make changes to your repository (or part of it) without affecting it, you can 'fork' it (make a copy of it). This ensures the original repository remains unchanged. To fork a github repository, follow the following steps: 

1. Click into the github repository you want to fork. 
2. Click 'Fork' in the top right hand side of the top bar, and this should take you to a page titled 'Create a new fork'
3. You can now work in this copy of your repository without it affecting the original. 

### Cloning a Github Repository
Cloning a repository essentially means downloading a copy of your repository that can be worked on locally. This method allows for version control and back up of code. To clone a github repository, follow the following steps: 

1. Click into the github repository you want to clone. 
2. Press the 'Code' button. This should open a section similar to the one below. 
<!-- ![Clone Code Button Dropdown](docs/images/github-two.png) -->
3. Copy the link in this dropdown
4. Open a terminal within your VSC (or whatever IDE you choose to use). 
5. In the terminal type 'git clone' and paste the URL. 
6. Press Enter - you now have a cloned version of your github repository.

# Future Development
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