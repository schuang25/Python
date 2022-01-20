/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    var parens_count = 0;
    for (var i = 0; i < str.length; i++) {
        if (str[i] == '(')
            parens_count++;
        else if (str[i] == ')') {
            parens_count--;
            if (parens_count < 0)
                return false;
        }
    }
    return parens_count == 0;
}

console.log(parensValid(str1))
console.log(parensValid(str2))
console.log(parensValid(str3))
console.log(parensValid(str4))

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str5 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected5 = true;

const str6 = "D(i{a}l[ t]o)n{e";
const expected6 = false;

const str7 = "A(1)s[O (n]0{t) 0}k";
const expected7 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var open_pairs = [];
    for (const char of str) {
        if (char == '(' || char == '[' || char == '{')
            open_pairs.push(char)
        else if (char == ')') {
            if (open_pairs[open_pairs.length - 1] == '(')
                open_pairs.pop();
            else
                return false;
        }
        else if (char == ']') {
            if (open_pairs[open_pairs.length - 1] == '[')
                open_pairs.pop();
            else
                return false;
        }
        else if (char == '}') {
            if (open_pairs[open_pairs.length - 1] == '{')
                open_pairs.pop();
            else
                return false;
        }
    }
    return open_pairs.length == 0;
}

console.log(bracesValid(str5))
console.log(bracesValid(str6))
console.log(bracesValid(str7))


/*****************************************************************************/