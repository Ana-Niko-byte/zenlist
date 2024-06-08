export function resetValues(retrievedArray, containerId){
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
    document.getElementById(containerId).innerHTML = '';
    for (const item of retrievedArray){
        document.getElementById(containerId).append(item);
    };
};

export function amendFormat(retrievedArray, dataAttribute, dataValue){
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
        let date = item.getAttribute(dataAttribute);

        const formattedDate = new Date(date);
        const day = formattedDate.getDate();
        const month = formattedDate.getMonth() +1;
        const year = formattedDate.getFullYear();

        const zeroedM = month < 10 ? "0" + month : month;
        const zeroedD = day < 10 ? "0" + day : day;

        item.dataset[dataValue] = `${year}-${zeroedM}-${zeroedD}`;
    };
};

// If something breaks tomorrow morning - it is because of the 5th parameter. - value: taskDueDate.
export function returnRecent(arrayToDuplicate, datasetValue, taskBoxId, amendDataValue, dataValue){
    /**
     * 
     */
    const newArray = [...arrayToDuplicate];
    amendFormat(newArray, amendDataValue, dataValue);

    newArray.sort(function(a, b) {
        const dateA = a.dataset[datasetValue];
        const dateB = b.dataset[datasetValue];

        return dateB.localeCompare(dateA);
    });
    resetValues(newArray, taskBoxId);
}

// Event Listener for Task Sorting
export function TaskSort(mainSelect, accordionIdentifier, taskBoxId){
    document.getElementById(mainSelect).addEventListener("change", function(){
        let selectedValue = this.value;
        const taskArray = Array.from(document.getElementsByClassName(accordionIdentifier));
    
        if (selectedValue === 'by priority'){
            // Create shallow copy for manipulation.
            const priorityArray = [...taskArray];
            // For easy numeric sorting.
            for (const item of priorityArray){
                let taskPriority = item.getAttribute("data-taskPriority");
                if (taskPriority === 'Critical'){
                    item.dataset.taskPriority = 0;
                } else if (taskPriority === 'Major'){
                    item.dataset.taskPriority = 1;
                } else if (taskPriority === 'Minor'){
                    item.dataset.taskPriority = 2;
                } else {
                    item.dataset.taskPriority = 3;
                }
            };

            priorityArray.sort(function(a,b) {
                const priorityA = a.dataset.taskPriority;
                const priorityB = b.dataset.taskPriority;
                return priorityA - priorityB;
            });

            resetValues(priorityArray, taskBoxId);
    
        } else if (selectedValue === 'by due-date'){
            returnRecent(taskArray, 'taskDueDate', taskBoxId, "data-taskDueDate", 'taskDueDate');
        }
    });
};