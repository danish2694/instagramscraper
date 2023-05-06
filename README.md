# instagramscraper
## This is a prototype to scrape instagram pages
### This project assumes that the page/account is public which is being scraped

To run the project, install node dependencies and python dependencies using

```
pip install -r requirements.txt
npm i
```
You also need chromedriver to run the python script, current chromedriver with version `112.0.5615.138` is included in the repo

To download the compatible chromedriver, check your chrome version from ``Settings >> About Chrome``

You can download the chromedriver from [here](https://chromedriver.chromium.org/downloads).

Then run the cron script using

`
node scheduler.js
`

This will set-up the cron to run every 24 hour
If you just want to run the python script, you can do so by executing the following command
`
python instascraper.py instagram
`

Here `instagram` is the page name to be scrapped.

This project needs some more enhancements, like using `AWS Lambda` for IP rotations to prevent blocking and scrapping links results using Multi-Threading.

This is just a prototype, hence limited posts are being fetched, which can be increased anytime. Also, page name is also static in the script which can be passed on using Express API.

We can also use services like PM2 to host the script on the server.
