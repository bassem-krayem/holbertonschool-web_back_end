export default function appendToEachArrayValue(array, appendString) {
  // eslint-disable-next-line
  const new_array = [];
  for (const value of array) {
    new_array.push(appendString + value);
  }
  // eslint-disable-next-line
  return new_array;
}
