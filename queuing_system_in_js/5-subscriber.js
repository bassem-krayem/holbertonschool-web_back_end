import { createClient } from 'redis';

const client = await createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'))
  .connect();

await client.subscribe(
  'holberton school channel',
  async (message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      await client.unsubscribe('holberton school channel');
      await client.quit();
    }
  }
);
