import kue from 'kue';

const blackListed = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0);
  if (blackListed.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  // track the job progress when it's 50%
  job.progress(50);
  console.log(`Sending notification to ${phoneNumber}, message: ${message}`);
  done();
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});