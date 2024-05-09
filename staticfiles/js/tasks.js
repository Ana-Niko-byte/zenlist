const edits = document.getElementsByClassName("btn-edit");
const taskForm = document.getElementById("taskForm");

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
        let taskContent = document.getElementById('body' + targetId).innerHTML;

        document.getElementById('modal' + targetId).innerHTML = taskContent;
    });
}