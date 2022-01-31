/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums, i=0) {
    // edge case 

    // base case -> what is going to end the recursion
    if (i === nums.length){
        return 0
    }

    // recursive call
    return nums[i] + sumArr(nums, i + 1)
}

console.log(sumArr(nums1));


// *******************************************************


/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function recursiveSigma(num) {
    if (num <= 0)
        return 0;
    else
        return Math.floor(num) + recursiveSigma(Math.floor(num) - 1);
}

console.log(recursiveSigma(num1));
console.log(recursiveSigma(num2));
console.log(recursiveSigma(num3));