/* 
  recursively find the lowest common multiple between two numbers
  "A common multiple is a number that is a multiple of two or more integers. 
  The common multiples of 3 and 4 are 0, 12, 24, .... 
  The least common multiple (LCM) of two numbers is the smallest number (not zero) 
  that is a multiple of both."
  
  Try writing two columns of multiples as a starting point:
  starting with 15 and 25 and keep writing their multiples until you find the lowest common one
  then turn this in to a step by step instruction
  15 25
  30 50
  45 75
  60
  75
  75 is the first common
*/

const num1A = 1;
const num1B = 1;
const expected1 = 1;

const num2A = 5;
const num2B = 10;
const expected2 = 10;

const num3A = 10;
const num3B = 5;
const expected3 = 10;

const num4A = 6;
const num4B = 8;
const expected4 = 24;

const num5A = 15;
const num5B = 25;
const expected5 = 75;

/**
 * Add params if needed for recursion
 * Finds the lowest common multiple of the two given ints.
 * @param {number} a
 * @param {number} b
 * @returns {number} The lowest common multiple of the given ints.
 */
function lowestCommonMult(a, b, a_base=a, b_base=b) {
    if (a == b)
        return a;
    if (a % b == 0)
        return a;
    if (b % a == 0)
        return b;
    if (a < b)
        return lowestCommonMult(a + a_base, b, a_base, b_base);
    else
        return lowestCommonMult(a, b + b_base, a_base, b_base);
}

console.log(lowestCommonMult(num1A, num1B))
console.log(lowestCommonMult(num2A, num2B))
console.log(lowestCommonMult(num3A, num3B))
console.log(lowestCommonMult(num4A, num4B))
console.log(lowestCommonMult(num5A, num5B))

// ************************************************************************

/* 
  Binary String Expansion
  You are given a STRING containing chars "0", "1", and "?"
  For every "?" character, either "0" or "1" can be substituted.
  Write a recursive function to return array of all valid strings with "?" chars expanded to "0" or "1". 
*/

const two_str1 = "1?0?";
const two_expected1 = ["1000", "1001", "1100", "1101"];
// output list order does not matter

/**
 * Add params if needed for recursion
 * Expands a string such that each "?" in the given string will be replaced
 * with a "0" and a "1".
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string containing to expand.
 * @returns {Array<string>} The expanded versions of the given string.
 */
function binaryStringExpansion(str, output=[]) {
    /*var output_str = "";
    var has_question_mark = false;
    for (var i = 0; i < str.length; i++) {
        if (str[i] == "1" || str[i] == "0")
            output_str += str[i];
        else {
            has_question_mark = true;
            output = binaryStringExpansion(output_str + "0" + str.slice(i+1), output)
            output = binaryStringExpansion(output_str + "1" + str.slice(i+1), output)
            break;
        }
    }
    if (!has_question_mark)
        output.push(output_str)
    return output; */

    /* if (str.includes("?")) {
        output = binaryStringExpansion(str.replace("?", "0"), output)
        output = binaryStringExpansion(str.replace("?", "1"), output)
    }
    else
        output.push(str)
    return output; */

    var question_mark = str.indexOf("?");
    if (question_mark == -1)
        output.push(str);
    else {
        output = binaryStringExpansion(str.slice(0, question_mark) + "0" + str.slice(question_mark + 1), output)
        output = binaryStringExpansion(str.slice(0, question_mark) + "1" + str.slice(question_mark + 1), output)
    }
    return output;
}

console.log(binaryStringExpansion(two_str1))