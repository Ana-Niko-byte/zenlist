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