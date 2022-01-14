/* 
  Zip Arrays into Map
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

  const keys1 = ["abc", 3, "yo"];
  const vals1 = [42, "wassup", true];
  const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
  };
  
  const keys2 = ["abc", 3, "yo", "bob"];
  const vals2 = [42, "wassup", true];
  const expected2 = false
  
  
  /**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */
function zipArraysIntoMap(keys, values) {
    if (keys.length != values.length)
        return false;
    var dict = {};
    for (var i = 0; i < keys.length; i++) {
        dict[keys[i]] = values[i];
    }
    return dict;
}

console.log(zipArraysIntoMap(keys1, vals1));
console.log(zipArraysIntoMap(keys2, vals2));

/* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", character: 'dicey' };
// Or create a system that askes the end user what key they want to keep.
const two_expected2 = { Zaphod: "name", high: "charm", dicey: ["morals", "character"] };

const two_obj3 = { name: "Zaphod", charm: "high", morals: "dicey", character: null };
const two_expected3 = false;
// const two_expected3 = { Zaphod: "name", high: "charm", dicey: "morals", 'unknown': character };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) {
    var new_obj = {};
    var value = "";
    for (var key in obj) {
        value = obj[key]
        if (value == null) 
            return false;
        else if (value in new_obj) {
            if (new_obj[value] instanceof Array)
                new_obj[value].append(key);
            else
                new_obj[value] = [new_obj[value], key];
        } else
            new_obj[obj[key]] = key;
    }
    return new_obj;
}

console.log(invertObj(two_obj1))
console.log(invertObj(two_obj2))
console.log(invertObj(two_obj3))