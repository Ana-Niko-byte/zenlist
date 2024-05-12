const edits = document.getElementsByClassName("btn-edit");
const taskForm = document.getElementById("taskForm");

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
        let targetId = e.target.getAttribute("task_id");
        let targetName = document.getElementById(`name${targetId}`);
        let targetDueDate = document.getElementById(`due-date${targetId}`);
        let targetStatus = document.getElementById(`status${targetId}`);
        let targetPriority = document.getElementById(`priority${targetId}`);
        let targetNotes = document.getElementById(`notes${targetId}`);
        
        // entire form element content
        // let taskContent = document.getElementById('body' + targetId).innerHTML;
        taskNameField.value = targetName;
        taskNotesField.value = targetNotes;
        taskPriorityField.value = targetPriority;
        taskStatusField.value = targetStatus;
        taskDueDateField.value = targetDueDate;
        taskForm.setAttribute("action", `edit_task/${targetId}`);

        document.getElementById(`modal${targetId}`).innerHTML = targetStatus;
    });
}