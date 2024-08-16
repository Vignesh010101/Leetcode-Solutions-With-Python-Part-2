/**
 * @param {Array} arr - The input array to be flattened.
 * @param {number} depth - The depth to which the array should be flattened.
 * @return {Array} - The flattened array.
 */
var flat = function (arr, depth, result = [], currentCycle = 0) {
    // Iterate through each element in the array
    for (let index = 0; index < arr.length; index++) {
        // If the current element is an array and the depth hasn't been reached
        if (Array.isArray(arr[index]) && currentCycle < depth) {
            // Recursively call flat function with the nested array
            flat(arr[index], depth, result, currentCycle + 1);
        } else {
            // If the element is not an array or the depth limit is reached, push it to tempArray
            result.push(arr[index]);
        }
    }
    // Return the flattened array
    return result;
};
