export default function uploadPhoto(filename) {
  return new Promise(
    (resolve, reject) =>
      // eslint-disable-next-line
      reject(new Error(`${filename} cannot be processed`))
    // eslint-disable-next-line
  );
}
