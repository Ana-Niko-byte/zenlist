// Delete Functionality
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletes = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deletes` array:
* - Onclick, retrieves the associated task's ID.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
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
const taskForm = document.getElementById("taskFormModal");
const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editConfirm = document.getElementById("editConfirm");

const taskNameField = document.getElementById("id_name");
const taskDueDateField = document.getElementById("id_due_date");
const taskStatusField = document.getElementById("id_status");
const taskPriorityField = document.getElementById("id_priority");
const taskNotesField = document.getElementById("id_notes");

/**
 * Iterates through all edit buttons and appends a 'click' event listener.
 * targetId : retrieves the id of the task that has been clicked on.
 * taskContent : retrieves the innerHTML of the task. 
 * 
 * At the moment, the innerHTML gets put into the modal body and cannot be edited directly.
 */
for (let button of edits){
  button.addEventListener('click', (e) => {
    let editId = e.target.getAttribute("data-task-id");
    let targetName = e.target.getAttribute("data-edit-name");
    let targetDueDate = e.target.getAttribute("data-edit-due-date");
    let targetStatus = e.target.getAttribute("data-edit-status");
    let targetPriority = e.target.getAttribute("data-edit-priority");
    let targetNotes = e.target.getAttribute("data-edit-notes");

    // taskForm.setAttribute("action", `update-task/${editId}`);
    editConfirm.href = `update-task/${editId}`;
    
    taskNameField.value = targetName;
    taskNotesField.value = targetNotes;
    taskPriorityField.value = targetPriority;
    taskStatusField.value = targetStatus;
    taskDueDateField.value = targetDueDate;
    editModal.show()
  });
}