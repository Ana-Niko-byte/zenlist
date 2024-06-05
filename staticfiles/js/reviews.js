// Sorting Functionality 

const selectField = document.getElementById("review-filter").addEventListener("change", function(){
    /**
     * 
     * 
     */
    let selectedOption = this.value;
    let reviewItemsArray = Array.from(document.getElementsByClassName("zenlist-review"));
    let ratings = []

    for (const item of reviewItemsArray){
        let arrayedStars = item.getAttribute("data-highest-rate").split('☆').join('').split('');
        const itemId = item.getAttribute("data-review-id");
        ratings.push([itemId, arrayedStars.length]);
    };

    if (selectedOption === 'by best'){
        // Sort by second item in sub array in ascending order.
        ratings.sort((a, b) => b[1] - a[1]);

    } else if (selectedOption === 'by lowest'){
        // Sort by second item in sub array in descending order.
        ratings.sort((a, b) => a[1] - b[1]);

    } else if (selectedOption === 'by recent'){
        // Sort by date added (in view?).

    };
});

// Delete Functionality
const deleteReviewModal = new bootstrap.Modal(document.getElementById("deleteReviewModal"));
const deletes = document.getElementsByClassName("btn-delete");
const deleteReviewConfirm = document.getElementById("deleteReviewConfirm");

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
        let reviewId = e.target.getAttribute("data-review-id");
        deleteReviewConfirm.href = `delete-review/${reviewId}`;
        deleteReviewModal.show();
    });
}