const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const pushNotificationJob = queue.create('push_notification_code_3', job).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${pushNotificationJob.id}`);
      }
    });

    pushNotificationJob.on('complete', () => {
      console.log(`Notification job ${pushNotificationJob.id} completed`);
    });

    pushNotificationJob.on('failed', (errorMessage) => {
      console.log(`Notification job ${pushNotificationJob.id} failed: ${errorMessage}`);
    });

    pushNotificationJob.on('progress', (progress) => {
      console.log(`Notification job ${pushNotificationJob.id} ${progress}% complete`);
    });
  });
}
export default createPushNotificationsJobs;