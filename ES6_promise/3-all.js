import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const results = [uploadPhoto(), createUser()];
  return Promise.all(results)
    .then(([photoResult, userResult]) => {
      const output = `${photoResult.body} ${userResult.firstName} ${userResult.lastName}`;
      console.log(output);
      return output;
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
