import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const results = [signUpUser(), uploadPhoto()];
  return Promise.allSettled(results).then((results) => {
    return results;
  });
}
