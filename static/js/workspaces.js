// Delete Functionality
const deleteWorkspaceModal = new bootstrap.Modal(document.getElementById("deleteWorkspaceModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteWorkspaceConfirm");

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
        let workspaceId = e.target.getAttribute("data-workspace-id");
        deleteConfirm.href = `delete/${workspaceId}`;
        deleteWorkspaceModal.show();
    });
}