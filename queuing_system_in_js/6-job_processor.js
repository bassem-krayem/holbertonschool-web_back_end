import kue from 'kue';

// Create a Kue job queue
const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber},  with the message: ${message}`);
}

// Process jobs of type 'notification'
queue.process('push_notification_code', (job, done) => {
  const { phone, message } = job.data;
  sendNotification(phone, message);
  done();
});
