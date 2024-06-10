## Note: This application and its README is Work-In-Progress.

# Zenlist
The application is available for viewing [here](https://zenlist-b604919b54d1.herokuapp.com/).

## A Little Bit About Zenlist
Zenlist is a task-tracking Django application, designed to provide users an easy and quick way of organising and managing day-to-day tasks for different environments. With accessible sorting systems and an intuitive interface, Zenlist is the perfect go-to for anyone who wishes to improve their time-management skills and stay on top of their day.

# Business/Social Goals
- Allow for organisation/categorisation of assets in a clear system (user-created environments with sorting functionality) to make the platform easily accessible and understandable.

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
![Zenlist wireframe](static/images/zenlist-wireframe.png)
# Structure 
## Models
Below is a simple ERD for Zenlist's models.
![Entity Relationship Diagram for Zenlist](static/images/erd.jpg)

## Views & Templates
All pages contain the same navigation and footer sections.
### Scrum Home Page
This is the main home page of the project. Though it does not have a conventional 'Home' page, its root page is the starting point of Zenlist, deep diving into scrum methodology and providing potential users with information on the app (attention-grabbing header, reviews, an introduction to the scrum methodology for time-management, and the option for users to leave a review if they are logged in). 

- #### Jumbotron
    - If not signed in, the jumbotron displays a signup button and an advertising heading.

    - If signed in, the jumbotron displays a button to access the user's workspaces and an encouraging title.
- #### Reviews
    - These reviews are filtered by stars and displayed in a row to site visitors. 

    The app can only be reviewed by logged in users, and all reviews require approval from an administrator prior to being displayed on the home/reviews page. Additionally, the user is presented with a button to read all reviews for the application, which redirects to a standalone page. This page is not presented in the navigation bar, but users can return to a page of their choosing by selecting existing links in the navigation bar. 

    The standalone page incorporates common sorting functionality for all reviews (by best, by lowest, by recent), so users have fast access to the exact reviews they are looking for, as well as the ability to view any of their own reviews pending administrator approval. 

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

    - On click, takes the user into a detailed view of their workspace, where they have access to a task form (for adding new tasks), and an overview of all tasks in their status columns - '_To Do_', '_In Progress_', '_Completed_'. Additionally, upon clicking on one of these tasks, the task's notes and due date become visible, along with buttons for editing (the task appears in the form) and deleting the task. A circle beside the name of the task indicates its priority, as follows: 
        - red circle - '_Critical_' 
        - orange circle - '_Major_' 
        - yellow circle - '_Minor_' 
        - green circle - '_Nice to have!_' 
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
The application encompasses the following scope: 

### User Interaction
Once registered and logged in, the user can access their Zenlist environments in the _Your Workspaces_ tab. All tasks ('_To Do_', '_In Progress_', '_Completed_') are visible within their Zenlists. After selecting a workspace, the user can add another task to the list via the form on the left-hand side. Here they give a title, assign a category, a due date, a priority, and a brief description to the task they wish to add. Once the task is submitted, the user may:
- Open the task accordion item (through the 'click' event) to view the task details (due-date, priority (colourful dot), and any associated notes).

- Edit the task (using the form on the left-hand side of the page).

- Change the task's status, in which case the user receives a confirmation message following a successful update, and visual confirmation of the task under the relevant status list.

- Delete the task. 

- Sort the '_To Do_', '_In Progress_', '_Completed_' columns either by priority (from '_Critical_' at the top to '_Nice to have!_'), or by due date (tasks due at a later date are at the bottom of the list).

### Categorisation
The purpose of Zenlist is to allow users to categorise their day into environments. Each Zenlist environment, i.e., home-chores, study-related tasks, etc., keeps associated tasks separate from each other. Each of these spaces presents any tasks due on a particular day under the 'Due Today' column on the '_Your Workspaces_' tab.

### Filtering
To enable users to comfortably control their tasks, a filtering system was adopted to allow for quick access to all relevant data. The tasks can be filtered by the following: 
- _by priority_
- _by due date_

### Scrum & Agile Knowledge Sharing
To help users better understand the Zenlist framework, the home page of the application has been adapted as a Scrum Introduction page, with a basic overview over the practical uses and applications of scrum to a team and personal context. Furthermore, a link has been provided to the official [Scrum.org](https://scrumguides.org/index.html) website, where interested users may download the official scrum manual 2020 (latest version), free of charge.

# Aesthetics


# Strategy
This application aims at optimising task and time management by leveraging the benefits of an intuative and minimalist UI, visual reminders of approaching task due dates, and sorting systems for efficiency.

The application is designed as a mobile-first app, with an easy to use UI with hints where necessary. 

# Target Audience
- Users over 12 years of age. 
- Hobbyists.
- Students.
- Anybody who wishes to improve their time-management skills. 

# Key Information Deliverables
- Categorisation of tasks by environment.
- Time-tracking capabilities with visual reminders for approaching tasks.
- Sorting system (by space, by priority, by due date) for tasks, and by best, by lowest, by recent for reviews.
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
All testing and debugging procedures in this section have been conducted manually. For automated testing, please see all files '_test*.py_'.

## Home/Scrum Page
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Jumbotron display | If user is not logged in, the banner should display a signup button and signup motivation, else a hello, {user} and a workspaces button | Signout + visual check, signin + visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Reviews | Only displays approved 5 star reviews | Add new 5 star review, do not approve - check it does not display. Approve review, check it displays. | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Scrum Section | Image + Text Display as per styling | Visual Check + Lighthouse Image Paint test | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Review Form | If user is not logged in, do not display review form but display button to sign in, else display review form | Signout + visual check, signin + visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |

## Reviews Page
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Read all Reviews Button | Displays? Takes to correct page? | Visual check + click | Behaves as intended | <img src="static/images/thumbs-up.jpg"> |
| Reviews | Do all reviews display? | Visual check + database check | All display as intended | <img src="static/images/thumbs-up.jpg"> |
| Sorting | Do reviews sort as intended based on selection? | Manual test + check datasets in Chrome Developer Tools | Behaves as intended | <img src="static/images/thumbs-up.jpg"> |
| User Reviews | If user is logged in and has pending reviews, do they display in grey? | Sign in, manually add review through form on home page + check | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |
| Delete User Reviews | If user is logged in and has pending reviews, can they delete them? Confirmation modal pops up? | Delete a single user review from the reviews page | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |


## Contact Page
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Form Display | Form displays? | Visual check, both signed in and signed out | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Field Validation | Empty/wrong format fields == invalid form? | Leave fields empty one by one, enter invalid email format + submit each time, finally input correct formats + submit | Submits when fields are valid only. | <img src="static/images/thumbs-up.jpg"> |
| Send to Email | Does the user's message get sent to ananikolayenia@gmail.com? Is the user email in the reply to field in the mail? | Test message + check in email. | Functions as expected, reply gets sent to user email. | <img src="static/images/thumbs-up.jpg"> |

## SignUp
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Nav Display | Link displays only to signed out users? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Form Display | Form displays? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Field Validation | Empty/wrong format fields == invalid form? | Leave fields empty one by one, enter invalid email format + submit each time, finally input correct formats + submit | Submits when fields are valid only. | <img src="static/images/thumbs-up.jpg"> |
| Email Confirmation | Receive Email Confirmation? Button to Accept? | Check Email | Received. | <img src="static/images/thumbs-up.jpg"> |
| Redirect to SignIn | After accepting, redirects to signin page? | Click + Visual check | Behaves as expected. | <img src="static/images/thumbs-up.jpg"> |

## SignIn
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Nav Display | Link displays only to signed out users? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Form Display | Form displays? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Field Validation | Empty/wrong format fields == invalid form? | Leave fields empty one by one, enter invalid email format + submit each time, finally input correct formats + submit | Submits when fields are valid only. | <img src="static/images/thumbs-up.jpg"> |
| Success Message on Login | Displays Success Message? Jumbo Wording Change? | Signin + Visual Check | Wording changes and success message displays as expected. | <img src="static/images/thumbs-up.jpg"> |

## Your Workspaces
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Due Today Column | Displays workspace names with tasks due today? Congratulatory message if no due tasks? | Visual check for today's tasks + if no tasks due today, check for message and add a task due today. | Displays as intended. | <img src="static/images/thumbs-up.jpg"> |
| Workspaces List | Displays list of user workspaces? If no spaces, displays llamas with button to add a workspace? | Visual check + delete existing workspaces + add workspace on llama page | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |
| Add Workspace Button | Displays modal with form? Adds workspace to list? Success Message? | Add workspace + check | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |
| Delete Workspace Button | Displays confirmation modal? Displays correct workspace name? Deleted workspace from list and database? | Delete a workspace + visual check | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |


## Inside Workspace
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Task Form | Task Form displays? Add Task Successfully? | Add Task Manually | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |
| Status Columns | Display task counts? Display all tasks? Task accordions work as intended? | Visual check + click on tasks | Behave as intended. | <img src="static/images/thumbs-up.jpg"> |
| Edit Task | Edit button displayed in accordion? On click, displays all task information correctly in form? After submitting, updates task in status column? | Manual test | Behaves as expected except that the date gets added back to the form a day later than the due date | <img src="static/images/image.png"> |
| Delete Task | Confirmation modal pops up? After confirmation, deleted task? On cancel, returns to full workspace detail view? | Manual check +  visual check | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |


## Logout
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Nav Display | Link displays only to signed in users? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Button Display | Buttons display? | Visual check | Display as expected. | <img src="static/images/thumbs-up.jpg"> |
| Cancel Button | Returns to Home page and leaves user signed in? | Click 'cancel' + check if user still has access to workspaces + correct navigation links | Functions as intended. | <img src="static/images/thumbs-up.jpg"> |
| SignOut Button | Sigs User out returns to Home page? Changes Banner Wording? | Click 'SignOut' + check navigation link display, banner, and success message | Functions as intended. | <img src="static/images/thumbs-up.jpg"> |

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

[Reddit's philgyford](https://www.reddit.com/r/django/comments/1aqh4rw/error_with_testing_a_dynamic_url_in_django/) for URL resolve + [Medium Rafał Buczyński](https://medium.com/@buczynski.rafal/nawigacja-przez-django-testowanie-adres%C3%B3w-url-77b05cb30d87) for URL reverse and mentioning resolve.

# Acknowledgements