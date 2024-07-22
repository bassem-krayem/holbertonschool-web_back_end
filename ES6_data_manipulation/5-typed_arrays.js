export default function createInt8TypedArray(length, position, value) {
  // Step 1: Create an ArrayBuffer with the given length
  const buffer = new ArrayBuffer(length);

  // Step 2: Create a DataView for the ArrayBuffer
  const dataView = new DataView(buffer);

  // Step 3: Check if the position is valid
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Step 4: Set the value at the specified position using DataView
  dataView.setInt8(position, value);

  // Return the DataView
  return dataView;
}
