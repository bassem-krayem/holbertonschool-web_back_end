export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      resolve({ status: 200, body: 'success' });
    })
    .catch(() => {
      console.log('Got a response from the API');
      reject(new Error());
    });
}
