/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    var words = str.split(' ');
    for (var i = 0; i < words.length; i++) {
        var reverse = [];
        for (var j = words[i].length - 1; j >= 0; j--) {
            reverse.push(words[i].charAt(j));
        }
        words[i] = reverse.join('');
    }
    return words.join(' ');
}

console.log(reverseWords(str1));
console.log(reverseWords(str2));
console.log(reverseWords(str3));

// *****************************************************

/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const two_str1 = "This is a test";
const two_expected1 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) {
    var words = wordsStr.split(' ');
    var temp = "";
    for (var i = 0; i < words.length / 2; i++) {
        temp = words[i];
        words[i] = words[words.length - 1 - i];
        words[words.length - 1 - i] = temp;
    }
    return words.join(' ');
}

console.log(reverseWordOrder(two_str1));

// ********************************************************

/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const three_str1 = "abcABC";
const three_expected1 = "abcABC";

const three_str2 = " helloo ";
const three_expected2 = " helo";

// Bonus
const three_str3 = " hellool ";
const three_expected3 = "heol ";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    var return_string = [];
    for (var i = str.length - 1; i >= 0; i--) {
        if (!return_string.includes(str.charAt(i)))
            return_string.unshift(str.charAt(i));
    }
    return return_string.join('');
}

console.log(stringDedupe(three_str1))
console.log(stringDedupe(three_str2))
console.log(stringDedupe(three_str3))