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
Below is a simple ERD for Zenlist's models. Its two applications, _Scrum_ and _Workspace_ consist of several One-To-Many database tables. Below is a brief overview, with an explanation under the image.

![Entity Relationship Diagram for Zenlist](static/images/erd.jpg)

### Scrum App
Models: Scrum + Review

---

#### The Scrum Model
The scrum model contains all relevant information regarding the Scrum paragraph on the main homepage. While it was valid to add this content directly into the HTML, a model format allows admins to have user-friendly access for the purposes of maintaining and updating content based on website needs. 

The _id_ field in the model is automatically provided by Django (and could potentially come into use if the model were to be recycled throughout the application). 

The _title_ field refers to the title of the Scrum paragraph. 

The _updated_on_ field is read-only and is used mostly for reference whenever the scrum model is modified. 

The _content_ field is a textField that utilises Summernote for efficient and manageable content-editing. 

---

#### The Review Model
The _id_ field in the model is automatically provided by Django and comes into play in views that need to access specific reviews for editing/deletion.

The _author_ field refers to the _Django User_ model in a One-To-Many relationship, referencing the user to whom the review belongs.

The _job_industry_ field is a selection field for selecting the industry in which the reviewer works. This is used purely for contextual purposes and as a means of demonstrating that the application can be used by all, regardless of their professional background. 

The _rating_ field is a selection field for selecting the star rating the reviewer wishes to give to the appliation during the review process.

The _review_ field is a TextField (max 120 characters), where the user can comment on the application. 

The _reviewed-on_ field is a read-only date field refering to the date the review was left on (regardless of when it was approved).

The _approved_ field is a boolean field indicating whether the review has been approved by a Zenlist admin. 

---

### Workspace App
Models: Workpace + Task

---

#### The Workspace Model
The _id_ field in the model is automatically provided by Django and comes into play in views that need to access a specific workspace for deletion.

The _title_ field is a modifiable character field referring to the title of the workspace. 

The _slug_ field contains a slugified _title_ value, which is used in the creation of unique URLs for each workspace.

The _creator_ field is a One-To-Many relationship database table referring to the Django User model, and references the currently logged in user and their ownership of a specific workspace. This field is used for filtering and displaying only the relevant workspaces to each user.

The _created_on_ field is a read-only date field refering to the date the workspace was created on.

The_updated_on_ field is a read-only date field refering to the date the workspace was modified on.

---

#### The Task Model
The _id_ field in the model is automatically provided by Django and comes into play in views that need to access specific tasks in each workspace for editing/deletion.

The _name_ field is a modifiable character field, referring to the name of the task assigned by the user during task creation using the _TaskForm_. 

The _notes_ field is a modifiable text field with a max length of 100 characters, used for adding any notes/comments under each task.

The _creator_ field is a One-To-Many relationship database table referring to the Django User model, and references the currently logged in user and their ownership of a specific task.

The _workspace_ field is a One-To-Many relationship database table referring to the _Workspace_ model, and references the workspace to which the task belongs.

The _status_ field is a modifiable selection field for selecting one of three avaiable statuses for the purpose of filtering tasks by _To Do_, _In Progress_, and _Completed_.

The _priority_ field is a modifiable selection field for selecting one of four avaiable priorities for the purpose of filtering tasks by their priority, i.e., by _Critical_, _Major_, _Minor_, and _Nice to have!_.

The _due_date_ field is a modifiable datetime field used for specifying the task's due date.

The _date_created_ field is a read-only date field refering to the date the task was created on.

The_last_modified_ field is a read-only date field refering to the date the task was modified on.

---

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
This is a contact page for users to send queries to the Zenlist team (connected to my email).

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
This section outlines procedures for manual testing. For automated testing, please see all files '_test*.py_'.

## Manual Testing
### Home/Scrum Page
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Jumbotron display | If user is not logged in, the banner should display a signup button and signup motivation, else a hello, {user} and a workspaces button | Signout + visual check, signin + visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Reviews | Only displays approved 5 star reviews | Add new 5 star review, do not approve - check it does not display. Approve review, check it displays. | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Scrum Section | Image + Text Display as per styling | Visual Check + Lighthouse Image Paint test | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Review Form | If user is not logged in, do not display review form but display button to sign in, else display review form | Signout + visual check, signin + visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |

---

### Reviews Page
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Read all Reviews Button | Displays? Takes to correct page? | Visual check + click | Behaves as intended | <img src="static/images/thumbs-up.jpg"> |
| Reviews | Do all reviews display? | Visual check + database check | All display as intended | <img src="static/images/thumbs-up.jpg"> |
| Sorting | Do reviews sort as intended based on selection? | Manual test + check datasets in Chrome Developer Tools | Behaves as intended | <img src="static/images/thumbs-up.jpg"> |
| User Reviews | If user is logged in and has pending reviews, do they display in grey? | Sign in, manually add review through form on home page + check | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |
| Delete User Reviews | If user is logged in and has pending reviews, can they delete them? Confirmation modal pops up? | Delete a single user review from the reviews page | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |

---

### Contact Page
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Form Display | Form displays? | Visual check, both signed in and signed out | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Field Validation | Empty/wrong format fields == invalid form? | Leave fields empty one by one, enter invalid email format + submit each time, finally input correct formats + submit | Submits when fields are valid only. | <img src="static/images/thumbs-up.jpg"> |
| Send to Email | Does the user's message get sent to ananikolayenia@gmail.com? Is the user email in the reply to field in the mail? | Test message + check in email. | Functions as expected, reply gets sent to user email. | <img src="static/images/thumbs-up.jpg"> |

---

### SignUp
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Nav Display | Link displays only to signed out users? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Form Display | Form displays? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Field Validation | Empty/wrong format fields == invalid form? | Leave fields empty one by one, enter invalid email format + submit each time, finally input correct formats + submit | Submits when fields are valid only. | <img src="static/images/thumbs-up.jpg"> |
| Email Confirmation | Receive Email Confirmation? Button to Accept? | Check Email | Received. | <img src="static/images/thumbs-up.jpg"> |
| Redirect to SignIn | After accepting, redirects to signin page? | Click + Visual check | Behaves as expected. | <img src="static/images/thumbs-up.jpg"> |

---

### SignIn
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Nav Display | Link displays only to signed out users? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Form Display | Form displays? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Field Validation | Empty/wrong format fields == invalid form? | Leave fields empty one by one, enter invalid email format + submit each time, finally input correct formats + submit | Submits when fields are valid only. | <img src="static/images/thumbs-up.jpg"> |
| Success Message on Login | Displays Success Message? Jumbo Wording Change? | Signin + Visual Check | Wording changes and success message displays as expected. | <img src="static/images/thumbs-up.jpg"> |

---

### Your Workspaces
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Due Today Column | Displays workspace names with tasks due today? Congratulatory message if no due tasks? | Visual check for today's tasks + if no tasks due today, check for message and add a task due today. | Displays as intended. | <img src="static/images/thumbs-up.jpg"> |
| Workspaces List | Displays list of user workspaces? If no spaces, displays llamas with button to add a workspace? | Visual check + delete existing workspaces + add workspace on llama page | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |
| Add Workspace Button | Displays modal with form? Adds workspace to list? Success Message? | Add workspace + check | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |
| Delete Workspace Button | Displays confirmation modal? Displays correct workspace name? Deleted workspace from list and database? | Delete a workspace + visual check | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |

---

### Inside Workspace
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Task Form | Task Form displays? Add Task Successfully? | Add Task Manually | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |
| Status Columns | Display task counts? Display all tasks? Task accordions work as intended? | Visual check + click on tasks | Behave as intended. | <img src="static/images/thumbs-up.jpg"> |
| Edit Task | Edit button displayed in accordion? On click, displays all task information correctly in form? After submitting, updates task in status column? | Manual test | Behaves as expected except that the date gets added back to the form a day later than the due date | <img src="static/images/thumbs-up.jpg"> |
| Delete Task | Confirmation modal pops up? After confirmation, deleted task? On cancel, returns to full workspace detail view? | Manual check +  visual check | Behaves as intended. | <img src="static/images/thumbs-up.jpg"> |

---

### Logout
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|
| Nav Display | Link displays only to signed in users? | Visual check | Displays as expected. | <img src="static/images/thumbs-up.jpg"> |
| Button Display | Buttons display? | Visual check | Display as expected. | <img src="static/images/thumbs-up.jpg"> |
| Cancel Button | Returns to Home page and leaves user signed in? | Click 'cancel' + check if user still has access to workspaces + correct navigation links | Functions as intended. | <img src="static/images/thumbs-up.jpg"> |
| SignOut Button | Sigs User out returns to Home page? Changes Banner Wording? | Click 'SignOut' + check navigation link display, banner, and success message | Functions as intended. | <img src="static/images/thumbs-up.jpg"> |

---

## Automated Testing
Tests are compiled in files with the following naming convention: '_test_*.py_'. This section is broken down by app, with a brief overview of testing procedures.

### Scrum App
- test_forms.py

    Contains a class for testing the contact form associated with the Scrum model form and if specific user inputs are correctly placed in the form fields.

    Methods: 

    '_test_name_required()_':
    This test verifies that a populated contact form which is missing a
    name input is not submitted, and that the error stems from the missing
    name field input.

    '_test_email_required()_':
    This test verifies that a populated contact form which is missing an
    email input is not submitted, and that the error stems from the missing
    email field input.

    '_test_email_correct_format()_':
    This test verifies that a completed populated contact form is not submitted
    unless the email adheres to the expected email format, and that the error
    stems from the incorrectly filled email field.

    '_test_message_required()_':
    This test verifies that a populated contact form which is missing a
    message input is not submitted, and that the error stems from the missing
    message field input.

    '_test_message_max_length_200_char()_':
    This test verifies that a completed populated contact form is not submitted
    unless the message input is less than 200 characters, and that the error
    stems from the overfilled message field.

    Note: The application form on the user side does not allow the insertion
    of more than 200 characters.

    '_test_form_is_valid()_':
    This test verifies that a correctly filled out contact form is
    successfully submitted.

- test_models.py

    Contains a class to test all models associated with the Scrum app.

    Methods: 

    '_def setUp()_':
        Simulates the logging in of a user for review model assertion,
        and creates instances for the Scrum and Review models.

    '_def test_scrum_model_creation()_':
        Runs a series of asserions for each Scrum Model field to validate
        the expected values of the instance.

    '_def test_review_model_creation()_':
        Runs a series of assertions for each Review Model field to validate
        the expected values of the instance.

    '_def test_user_deletion_cascade()_':
        Deletes the current logged in user and checks whether the
        user's reviews were deleted as well, as per cascade.

- test_urls.py

    Contains a class for testing URLs associated with Scrum Views.

    Methods: 

    '_def test_hello_resolves()_':
        Reverses the URL name and checks if it returns the correct
        FBV of HelloScrum.
        Asserts HelloScrum is resolved from 'hello'.

    '_def test_contact_resolves()_':
        Reverses the URL name and checks if it returns the correct
        FBV of Contact_Me.
        Asserts Contact_Me is resolved from 'contact'.

    '_def test_reviews_resolves():_'
        Reverses the URL name and checks if it returns the correct
        FBV of Zenlist_Reviews.
        Asserts Zenlist_Reviews is resolved from 'reviews'.

---

### Workspace App
- test_forms.py

    Contains two classes. The first is a class for testing the workspace form associated with the Workspace Model. This form creates a new workspace instance if specific user inputs are correctly placed in the form fields.

    Methods: 

    '_def test_title_is_required()_':
        This test verifies that a populated workspace form which is missing a
        title input is not submitted, and that the error stems from the missing
        title field input.

    '_def test_form_is_valid()_':
        This test verifies that a correctly filled out workspace form is
        successfully submitted.

- test_models.py

    Contains a class to test all models associated with the Workspace app.

    Methods: 

    '_def setUp()_':
        Simulates user log in to allow the creation for workspaces and tasks.
        Simulates the creation of a workspace where workspace.creator field is
        automatically assigned the current User instance.
        Simulates the creation of a task where task.creator is automatically
        assigned the current User instance, and task.workspace is automatically
        assigned the current workspace.

    '_def test_workspace_model_creation()_':
        Runs a series of asserions for each Workspace Model field to validate
        the expected values of the instance.

    '_def test_task_model_creation()_':
        Runs a series of asserions for each Task Model field to validate
        the expected values of the instance.

    '_def test_workspace_delete_when_user_delete()_':
        Deletes the user and checks whether workspaces and tasks associated
        with the user were deleted as well, as per cascade.

    '_def test_task_delete_when_workspace_delete()_':
        Deletes the current workspace and checks whether tasks associated
        with the workspace were deleted as well, as per cascade.

- test_urls.py

    Contains a class for testing URLs associated with Workspace Views.

    Methods:

    '_def test_workspace_list_resolves()_':
        Reverses the URL name and checks if it returns the correct
        CBV of WorkspaceListView.
        Asserts WorkspaceListView is resolved from 'spaces'.

    '_def test_workspace_detail_resolves()_':
        Reverses the URL name with arguments [slug] and checks if it
        returns the correct FBV of workspace_detail.
        Asserts workspace_detail is resolved from 'full_workspace'.

    '_def test_workspace_delete_resolves()_':
        Reverses the URL name with arguments [int:id] and checks if it
        returns the correct FBV of delete_ws.
        Asserts delete_ws is resolved from 'delete_workspace'.

    '_def test_task_edit_resolves()_':
        Reverses the URL name with arguments [slug, int:id] and checks if it
        returns the correct FBV of update_ws_task.
        Asserts update_ws_task is resolved from 'task_edit'.

    '_def test_task_delete_resolves()_':
        Reverses the URL name with arguments [slug, int:id] and checks if it
        returns the correct FBV of delete_ws_task.
        Asserts delete_ws_task is resolved from 'task_delete'.

# Accessibility & Performance
### Lighthouse

### Colour Accessibility Validator 
Upon running the application through the [a11y Colour Checker](https://color.a11y.com/) via the URL input, the service displayed no issues. 

![Colour Accessibility Checker](static/images/contrast-checker.png)

### HTML Validation
Upon running the application through the [W3C Markup Validation Service](https://validator.w3.org/) via the URL input, the service highlighted two errors, as shown below. 

![HTML Validation Results](static/images/html-validation-errors.png)

Note: The second error shown above resulted from Summernote's rendering of the Scrum Content text. This was rectified by changing my own HTML 'p' element to a 'div', so that the paragraph would be rendered inside the div and not crop up as an error.

Homepage - 
![Clean HTML Validation Results](static/images/clean-html.png)
Contact - 
![Clean Contact HTML Validation Results](static/images/contact-html-validation.png)
Reviews -
![Clean Reviews HTML Validation Results](static/images/reviews-html-validation.png)
Sign Up - 
![Clean SignUp HTML Validation Results](static/images/signup-html-validation.png)
Sign In -
![Clean SignIn HTML Validation Results](static/images/signin-html-validation.png)
Sign Out - 
![Clean SignOut HTML Validation Results](static/images/logout-html-validation.png)
Your Workspaces - 
![Clean Workspaces HTML Validation Results](static/images/workspaces-html-validation.png)
Inside a Workspace - 
![Clean Workspaces Detail HTML Validation Results](static/images/workspace-detail-html-validation.png)

### CSS Validation
Upon running the application through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) via the URL input, the service highlighted no errors, as shown below. 

![CSS Validation Results](static/images/css-validation.png)

### JSHint Validation
Each of the application's JS files were run through the [JSHint](https://jshint.com/) separately, to ensure the code was up to standard and functioned as expected. 

Below are the results of the js files' validation. 

common.js - 
![common.js validation results](static/images/common-js.png)

reviews.js -
![reviews.js validation results](static/images/reviews-js.png)

#### Warning Explanation: 
This error is directed at the bootstrap modal being initiated within the button listener. Explanation...

tasks.js - 
![tasks.js validation results](static/images/tasks-js.png)

workspaces.js -
![workspaces.js validation results](static/images/ws-js.png)

# Deployment
The application is deployed on Heroku through github, and is available for viewing in the link at the top of this README.md document. To deploy a Heroku project, please refer to the guide below.

## Foreword
There are some general requirements when it comes to setting up your application and its files: 
- Your dependencies must be placed in the requirements.txt file.
- You must strictly adhere to the correct folder structure expected by Django's settings.
- In Django's settings.py file, setting Debug = True in development will display a detailed errors page if the applocation comes across an error hindering template rendering. It will also allow the collect of static files (stylesheets, images, and javascript files automatically). Setting Debug = False will display standard error pages under the same conditions and will not update with any changes to static files.

In Heroku, this is additionally configured under '_Config Vars_', as COLLECT_STATIC, with the value of 0 for blocking automatic collection, and 1 for allowing it.
- Do not commit to github with Debug = True. Always set Debug = False before committing to avoid exposing personal details.

You will need two-factor verification set up. I chose Google Authenticator because I already had it pre-installed on my phone.

### Step 1: Create an App on Heroku
Log onto your Heroku dashboard using your username and password, and confirm the access code in the two-factor verification app of your choosing.

Create a new Heroku app:
![New Heroku App](static/images/new-heroku.png)

You will be asked to pick a name and region for your app before clicking '_Create app_' on the next page.
![New App Options](static/images/new-app-options.png)

### Step 2: Connect to GitHub
Once you've created your app, go to the Deploy tab at the top.
Note: For demonstration purposes, I created a new app called '_testapp-123_'.

Select the middle box with GitHub's logo to connect your Heroku app to a Github Repository.

If prompted, authorize Heroku to access your GitHub account.
At the bottom, enter the name of the repository you wish to deploy to, and click Connect.
![Connecting GitHub to Heroku](static/images/heroku-github.png)

### Step 3: Automatic Deploy (Optional)
Under the "Automatic deploys" section, choose a branch from your GitHub repository that Heroku will watch for changes.

Enable automatic deploys by clicking Enable Automatic Deploys. With this, every push to the selected branch will automatically deploy a new version of your app.

### Step 4: Settings
When you create the app, you will need to add the '_heroku/python_' buildpack in the Settings tab. 

### Step 5: Deploy Your Masterpiece
If you've enabled automatic deploys, any push to the selected branch will automatically deploy your application.

If you prefer to deploy manually or want to deploy a branch without enabling automatic deploys, go to the "Manual deploy" section, select the branch, and click "Deploy Branch."

### Step 6: Where is my Application?
Your application has a similar look to the following Heroku URL: (https://*.herokuapp.com), and can be found after clicking the Open App button on your dashboard in the top right.

![Open App Button](static/images/open-app.png)

## Forking a Github Repository
To changes to your repository (or part of it) without affecting it's original state, you can 'fork' it (make a copy of it). This ensures the original repository remains unchanged. To fork a github repository, follow the following steps:

1. Click into the github repository you want to fork.
2. Click 'Fork' in the top right hand side of the top bar, and this should take you to a page titled 'Create a new fork'.
3. You can now work in this copy of your repository without it affecting the original.

## Cloning a Github Repository
Cloning a repository essentially means downloading a copy of your repository that can be worked on locally. This method allows for version control and back up of code. To clone a github repository, follow the following steps:

1. Click into the github repository you want to clone.
2. Press the 'Code' button. This should open a section similar to the one below.

<!-- clone github repository -->

3. Copy the link in this dropdown
4. Open a terminal within your VSC (or whatever IDE you choose to use).
5. In the terminal type 'git clone' and paste the URL.
6. Press Enter - you now have a cloned version of your github repository.

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