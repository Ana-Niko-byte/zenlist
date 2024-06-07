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
    };
}

function resetValues(retrievedArray){
    /**
     * This function is used to re-append sorted array items to the review-box.
     * 
     * Arguments:
     * retrievedArray : array, the array to be iterated over.
     * 
     * Method:
     * Retrieves the review-box by Id.
     * Empties the review-box.
     * Iterates through the array and appends each item to the review-box.
     */
    document.getElementById("review-box").innerHTML = '';
    for (const item of retrievedArray){
        document.getElementById("review-box").append(item);
    };
}

const selectField = document.getElementById("review-filter").addEventListener("change", function(){
    /**
     * On change event, sorts values based on selection.
     * 
     * Retrieves the selection value.
     * Retrieves the array of items to be sorted by class value 'zenlist-reviews'.
     * 
     * Change value of dataset highestRate from symbols to integer value indicating quantity of filled stars.
     * 
     */
    let selectedOption = this.value;
    let reviewItemsArray = Array.from(document.getElementsByClassName("zenlist-review"));

    // Sets highestRate value to numeric.
    determineRatingLength(reviewItemsArray);

    // Filtering
    if (selectedOption === 'by best'){
        reviewItemsArray.sort(function(a,b) {
            // Parsing as dataset highestRate is set to String.
            let reviewLengthA = parseInt(a.dataset.highestRate);
            let reviewLengthB = parseInt(b.dataset.highestRate);

            return reviewLengthB - reviewLengthA;
        });
        // Clear existing order + set to sorted array.
        resetValues(reviewItemsArray);

    } else if (selectedOption === 'by lowest'){
        reviewItemsArray.sort(function(a,b) {
            let reviewLengthA = parseInt(a.dataset.highestRate);
            let reviewLengthB = parseInt(b.dataset.highestRate);

            return reviewLengthA - reviewLengthB;
        });
        resetValues(reviewItemsArray);

    } else if (selectedOption === 'by recent'){
        // Sort by date added (in view?).

    };
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