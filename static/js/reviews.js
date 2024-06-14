// Imports from common.js
import { resetValues, returnRecent } from "./common.js";

// Sorting Functionality 
function determineRatingLength(retrievedArray){
    /**
     * Iterates over retrieved array to determine the length of the rating dataset attribute 'highestRate'.
     * Reassigns integer value to dataset highestRate.
     * 
     * Arguments:
     * retrievedArray : array, array for determining length of highestRate dataset value.
     */
    for (const item of retrievedArray){
        // Removes all empty stars ('★★★★', ''), joins at '' ('★★★★'), find the length (4). 
        let reviewLength = item.getAttribute("data-highestRate").split('☆').join('').length;
        // Sets the value of dataset highestRate to the reviewLength.
        item.dataset.highestRate = reviewLength;
    }
}

document.getElementById("review-filter").addEventListener("change", function(){
    /**
     * On change event, sorts values based on selection.
     * 
     * Method:
     * Retrieves the selection value.
     * Retrieves the array of items to be sorted by class value 'zenlist-reviews'.
     * Based on a conditional check of selection value, sorts the retrieved array.
     * 
     * Functions:
     * determineRatingLength(arr : array);
     * Change value of dataset highestRate from symbols to integer value indicating quantity of filled stars.
     * 
     * resetValues(arr : array);
     * Empties the review box container and reappends sorted values.
     * 
     * amendReviewedFormat(arr : array);
     * Changes the human readable format of the review.reviewed_on date to ISO 'YYYY-MM-DD'
     */
    let selectedOption = this.value;
    let reviewItemsArray = Array.from(document.getElementsByClassName("zenlist-review"));

    // Sets highestRate value to numeric.
    determineRatingLength(reviewItemsArray);

    // Filtering
    if (selectedOption === 'by best'){
        // Shallow copy to avoid changing original array.
        const newArray = [...reviewItemsArray].sort(function(a,b) {
            // Parsing as dataset highestRate is set to String.
            let reviewLengthA = parseInt(a.dataset.highestRate);
            let reviewLengthB = parseInt(b.dataset.highestRate);

            return reviewLengthB - reviewLengthA;
        });
        // Clear existing order + set to sorted array.
        resetValues(newArray, "review-box");

    } else if (selectedOption === 'by lowest'){
        const newArray = [...reviewItemsArray].sort(function(a,b) {
            let reviewLengthA = parseInt(a.dataset.highestRate);
            let reviewLengthB = parseInt(b.dataset.highestRate);

            return reviewLengthA - reviewLengthB;
        });
        resetValues(newArray, "review-box");

    } else if (selectedOption === 'by recent'){
        // If something breaks tomorrow morning - it is because of the 5th parameter.
        returnRecent(reviewItemsArray, "reviewedOn", "review-box", "data-reviewedOn", "reviewedOn");
    }
});


// Delete Functionality
const deletes = document.getElementsByClassName("btn-delete");

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deletes` array:
 * Onclick, retrieves the associated review's ID.
 * Updates the `deleteReviewConfirm` link's href to point to the deletion endpoint for the specific review.
 * Displays a confirmation modal (`deleteReviewModal`) to prompt the user for confirmation before deletion.
 */
for (let button of deletes) {
    button.addEventListener("click", (e) => {
        const deleteReviewModal = new bootstrap.Modal(document.getElementById("deleteReviewModal"));
        const deleteReviewConfirm = document.getElementById("deleteReviewConfirm");

        let reviewId = e.target.getAttribute("data-review-id");
        deleteReviewConfirm.href = `delete-review/${reviewId}`;
        deleteReviewModal.show();
    });
}