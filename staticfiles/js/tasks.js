// Imports from common.js
import { resetValues, TaskSort } from "./common.js";

// Delete Functionality
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletes = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deletes` array:
 * Onclick, retrieves the associated task's ID.
 * Updates the `deleteConfirm` link's href to point to the deletion endpoint for the specific task.
 * Displays a confirmation modal (`deleteModal`) to prompt the user for confirmation before deletion.
 */
for (let button of deletes) {
    button.addEventListener("click", (e) => {
        let taskId = e.target.getAttribute("data-task-id");
        deleteConfirm.href = `delete-task/${taskId}`;
        deleteModal.show();
    });
}


// Edit Functionality
const edits = document.getElementsByClassName("btn-edit");

const taskNameField = document.getElementById("id_name");
const taskNotesField = document.getElementById("id_notes");
const taskStatusField = document.getElementById("id_status");
const taskPriorityField = document.getElementById("id_priority");
const taskDateField = document.getElementById("id_due_date");

const form = document.getElementById("taskForm");
const submit = document.getElementById("submitButton");

/**
 * Iterates through all edit buttons and appends a 'click' event listener.
 * 
 * taskId : retrieves the id of the task that has been clicked.
 * task- : retrieves the value of dataset attributes attached to the edit button.
 * 
 * Formats the date value returned from attribute: data-edit-date to the ISO recognised format in HTML YYYY-mm-dd.
 * Assigns retrieved attributes to the values of the relevant form fields.
 * 
 * Changes the innerHTML of the Submit button to reflect the change in form action. 
 * Dynamically sets the form's action to the URL section defined in URLs.py.
 */
for (let editButton of edits) {
    editButton.addEventListener("click", (e) => {
        // Retrieve taskId for updating
        let taskId = e.target.getAttribute("task_id");

        // Retrieve Task information + assign each to the relevant task form field.
        let taskName = e.target.getAttribute("data-edit-name");
        let taskNotes = e.target.getAttribute("data-edit-notes");
        let taskPriority = e.target.getAttribute("data-edit-priority");
        let taskStatus = e.target.getAttribute("data-edit-status");
        let taskDate = e.target.getAttribute("data-edit-date");

        let date = new Date(taskDate);
        let actualDate = date.toISOString().split("T")[0];

        taskNameField.value = taskName;
        taskNotesField.value = taskNotes;
        taskStatusField.value = taskStatus;
        taskPriorityField.value = taskPriority;
        taskDateField.value = actualDate;

        // Visual indication of where to edit the task.
        document.getElementById("taskCard").style.backgroundColor = '#FFC107';

        submit.innerText = "Update My Task";
        form.setAttribute("action", `update-task/${taskId}`);
    });
}

// Sorting Functionality Common.js
TaskSort("task1-filter", "accordion-ToDo", "tasks-todo");
TaskSort("task2-filter", "accordion-InProgress", "tasks-inprogress");
TaskSort("task3-filter", "accordion-Completed", "tasks-completed");