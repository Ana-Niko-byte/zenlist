const edits = document.getElementsByClassName("btn-edit");
const taskForm = document.getElementById("taskForm");

const taskNameField = document.getElementById("id_name");
const taskDueDateField = document.getElementById("id_due_date");
const taskStatusField = document.getElementById("id_status");
const taskPriorityField = document.getElementById("id_priority");
const taskNotesField = document.getElementById("id_notes");

// Delete Functionality
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Iterates through all edit buttons and appends a 'click' event listener.
 * targetId : retrieves the id of the task that has been clicked on.
 * taskContent : retrieves the innerHTML of the task. 
 * 
 * At the moment, the innerHTML gets put into the modal body and cannot be edited directly.
 */
for (let button of edits){
    button.addEventListener('click', (e) => {
        let targetId = e.target.getAttribute("task_id");

        let targetName = document.getElementById(`name${targetId}`);
        let targetDueDate = document.getElementById(`due-date${targetId}`);
        let targetStatus = document.getElementById(`status${targetId}`);
        let targetPriority = document.getElementById(`priority${targetId}`);
        let targetNotes = document.getElementById(`notes${targetId}`);
        
        // entire form element content
        // let taskContent = document.getElementById('body' + targetId).innerHTML;
        taskNameField.value = targetName.innerHTML;
        taskNotesField.value = targetNotes.innerHTML;
        taskPriorityField.value = targetPriority.innerHTML;
        taskStatusField.value = targetStatus.innerHTML;
        taskDueDateField.value = targetDueDate.innerHTML;
        taskForm.setAttribute("action", `edit_task/${targetId}`);
    });
}

// Delete Functionality
/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let taskId = e.target.getAttribute("data-task-id");
      deleteConfirm.href = `delete-task/${taskId}`;
      deleteModal.show();
    });
  }