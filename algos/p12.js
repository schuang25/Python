/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
const expected3 = [1, 2, 3, 4, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
const expected4 = [42, 0, 6];

/**
 * Interleaves two arrays into a new array. Interleaving means alternating
 * the items starting from the first array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr1
 * @param {Array<any>} arr2
 * @returns {Array<any>} A new array of interleaved items.
 */
function interleaveArrays(arr1, arr2) {
    if (arr1.length == 0)
        return arr2;
    if (arr2.length == 0)
        return arr1;
    var i = 0, long_len;
    var return_arr = [];
    if (arr1.length > arr2.length) 
        long_len = arr1.length;
    else
        long_len = arr2.length;
    for (i; i < long_len; i++) {
        if (i < arr1.length)
            return_arr.push(arr1[i]);
        if (i < arr2.length)
            return_arr.push(arr2[i]);
    }
    return return_arr;
}

console.log(interleaveArrays(arrA1, arrB1))
console.log(interleaveArrays(arrA2, arrB2))
console.log(interleaveArrays(arrA3, arrB3))
console.log(interleaveArrays(arrA4, arrB4))

/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
function binarySearch(sortedNums, searchNum) {
    var binary_start = 0, binary_end = sortedNums.length - 1, search_index = 0;
    var num_count = 0;
    while (binary_end > binary_start) {
        search_index = Math.floor((binary_start + binary_end) / 2);
        console.log("searching index " + search_index);
        if (sortedNums[search_index] == searchNum)
            break;
        else if (sortedNums[search_index] > searchNum)
            binary_end = search_index - 1;
        else
            binary_start = search_index + 1;
    }
    search_index = Math.floor((binary_start + binary_end) / 2);
    console.log("searching index " + search_index)
    if (sortedNums[search_index] != searchNum)
        return false;
    num_count++;
    var index = search_index + 1;
    while (index < sortedNums.length && sortedNums[index] == searchNum) {
        num_count++;
        index++;
    }
    index = search_index - 1;
    while (index >= 0 && sortedNums[index] == searchNum) {
        num_count++;
        index--;
    }
    return num_count;
}

console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))
console.log(binarySearch(nums4, searchNum4))