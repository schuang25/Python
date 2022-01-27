/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
    var change = {};
    var remaining_change = cents;
    if (remaining_change / 25 >= 1) {
        change['quarter'] = Math.floor(remaining_change / 25);
        remaining_change -= 25 * change['quarter'];
    }
    if (remaining_change / 10 >= 1) {
        change['dime'] = Math.floor(remaining_change / 10);
        remaining_change -= 10 * change['dime'];
    }
    if (remaining_change / 5 >= 1) {
        change['nickel'] = Math.floor(remaining_change / 5);
        remaining_change -= 5 * change['nickel'];
    }
    if (remaining_change > 0) {
        change['penny'] = remaining_change;
    }
    return change;
}

console.log(fewestCoinChange(cents1))
console.log(fewestCoinChange(cents2))
console.log(fewestCoinChange(cents3))
console.log(fewestCoinChange(cents4))

/* 
  Missing Value
  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  Quickly determine and return the missing value.
*/

const nums1 = [3, 0, 1];
const expected1 = 2;

const nums2 = [3, 0, 1, 2];
const expected2 = null;
// Explanation: nothing is missing

/* 
  Bonus: now the lowest value can now be any integer (including negatives),
  instead of always being 0. 
*/

const nums3 = [2, -4, 0, -3, -2, 1];
const expected3 = -1;

const nums4 = [5, 2, 7, 8, 4, 9, 3];
const expected4 = 6;

/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
function missingValue(unorderedNums) {
    var min = unorderedNums[0], max = unorderedNums[0];
    for (var i = 1; i < unorderedNums.length; i++) {
        if (unorderedNums[i] < min)
            min = unorderedNums[i];
        else if (unorderedNums[i] > max)
            max = unorderedNums[i];
    }
    for (var j = min; j <= max; j++) {
        if (!unorderedNums.includes(j))
            return j;
    }
    return null;
}

console.log(missingValue(nums1))
console.log(missingValue(nums2))
console.log(missingValue(nums3))
console.log(missingValue(nums4))