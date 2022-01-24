/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "        ";
const expected2 = "";

const str3 = "   hello world earth     ";
const expected3 = "hello world earth";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
    var start = 0, end = str.length - 1;
    while (str[start] == ' ')
        start++;
    while (str[end] == ' ')
        end--;
    if (end == 0)
        return "";
    var trimmed_str = "";
    for (var i = start; i <= end; i++) {
        trimmed_str += str[i];
    }
    return trimmed_str;
}

console.log(trim(str1))
console.log(trim(str2))
console.log(trim(str3))

// ************************************************************************

/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
*/

const two_strA1 = "yes3";
const two_strB1 = "3eys";
const two_expected1 = true;

const two_strA2 = "yes";
const two_strB2 = "eYs";
const two_expected2 = true;

const two_strA3 = "no";
const two_strB3 = "noo";
const two_expected3 = false;

const two_strA4 = "silent";
const two_strB4 = "listen";
const two_expected4 = true;

const two_strA5 = "not";
const two_strB5 = "noo";
const two_expected5 = false;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {
    if (s1.length != s2.length)
        return false;
    var dict1 = {}, dict2 = {};
    var char1 = "", char2 = ""
    for (var i = 0; i < s1.length; i++) {
        char1 = s1[i].toLowerCase();
        char2 = s2[i].toLowerCase();
        if (char1 in dict1)
            dict1[char1]++;
        else
            dict1[char1] = 1;
        if (char2 in dict2)
            dict2[char2]++;
        else
            dict2[char2] = 1;
    }
    if (Object.keys(dict1).length != Object.keys(dict2).length)
        return false;
    for (var key in dict1) {
        if (!(key in dict2))
            return false;
        else  {
            if (dict1[key] != dict2[key])
                return false;
        }
    }
    return true;
}

console.log(isAnagram(two_strA1, two_strB1))
console.log(isAnagram(two_strA2, two_strB2))
console.log(isAnagram(two_strA3, two_strB3))
console.log(isAnagram(two_strA4, two_strB4))
console.log(isAnagram(two_strA5, two_strB5))