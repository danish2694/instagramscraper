const cron = require('node-cron');
const shell = require('shelljs');

// Fetch instagram page posts at At 12:00 am every day.
cron.schedule('0 0 * * *', function() {
    console.log('Running Cron Job');
    if (shell.exec('python instascraper.py ' + 'instagram').code !== 0) {
      shell.exit(1);
    }
    else {
      shell.echo('Scrapping complete');
    }
  });