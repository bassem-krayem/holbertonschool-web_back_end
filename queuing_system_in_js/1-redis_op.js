import { createClient } from 'redis';

const client = await createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'))
  .connect();

const setNewSchool = async (schoolName, value) => {
  await client.set(schoolName, value);
}

const displaySchoolValue = async (schoolName) => {
  const value = await client.get(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
