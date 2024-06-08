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

function amendReviewedFormat(retrievedArray){
    /**
     * Iterates over each item in the array and retrieves the dataset reviewedOn value
     * representing the date on which the review was made.
     * 
     *Arguments:
     * retrievedArray : array, array for formatting reviewedOn dataset value.
     * 
     * Method:
     * Retrieves reviewedOn dataset value.
     * Converts to a new Date object.
     * Retrieves day, month, year of new Date object.
     * Formats with zeroes to match date format from getCurrentDateFormat();
     * Resets value of reviewedOn dataset to formatted date.
     * 
     */
    for (const item of retrievedArray){
        // reviewedOn current value format: "June 5, 2024"
        let reviewedDate = item.getAttribute("data-reviewedOn");

        const formattedDate = new Date(reviewedDate);
        const day = formattedDate.getDate();
        const month = formattedDate.getMonth() +1;
        const year = formattedDate.getFullYear();

        // To comply with date format from getCurrentDateFormat();
        const zeroedM = month < 10 ? "0" + month : month;
        const zeroedD = day < 10 ? "0" + day : day;

        item.dataset.reviewedOn = `${year}-${zeroedM}-${zeroedD}`;
    }
};

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
};

const selectField = document.getElementById("review-filter").addEventListener("change", function(){
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
        amendReviewedFormat(reviewItemsArray);
        reviewItemsArray.sort(function(a, b) {
            const dateA = a.dataset.reviewedOn;
            const dateB = b.dataset.reviewedOn;
            // As format is Str 'YYYY-MM-DD'
            return dateB.localeCompare(dateA);
        });
        resetValues(reviewItemsArray);
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