export default function appendToEachArrayValue(array, appendString) {
    const clone = [];
    let counter = 0;
    for (const e of array) {
      clone[counter] = appendString + e;
      counter += 1;
    }
    return clone;
  }
