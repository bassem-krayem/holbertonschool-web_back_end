import { createClient } from 'redis';

const client = await createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'))
  .connect();

await client.hSet(
  'HolbertonSchools',
  {
    Portland: 50,
  }
);
await client.hSet(
  'HolbertonSchools',
  {
    Seattle: 80,
  }
);
await client.hSet(
  'HolbertonSchools',
  {
    NewYork: 20,
  }
);
await client.hSet(
  'HolbertonSchools',
  {
    Bogota: 20,
  }
);
await client.hSet(
  'HolbertonSchools',
  {
    Cali: 40,
  }
);
await client.hSet(
  'HolbertonSchools',
  {
    Paris: 2,
  }
);

const values = await client.hGetAll('HolbertonSchools');
console.log(values);
