//   **************************************************************************************

/* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {
    var returnstring = "";
    var char = "";
    var count = 1;
    for (var i = 0; i < str.length; i++) {
        char = str.charAt(i);
        if (isNaN(parseInt(char))) {
            if (i < str.length - 1)
                count = parseInt(str.substring(i+1));
            else
                count = 1;
            returnstring += char.repeat(count);
        }
    }
    return returnstring;
}

console.log(decodeStr(str1));
console.log(decodeStr(str2));