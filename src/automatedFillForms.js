const os = require("os");
const path = require("path");
const puppeteer = require("puppeteer");

/**
 * Launches a browser that, for each form parameter given, goes to the given form URL
 * in a new tab. Then the given form filler function is called in the page's context
 * with the respective form parameters.
 *
 * The browser's user data is store in a OS tmp directory. So if the users want
 * to customize some settings they can and they will be persisted until the tmp
 * directory is emptied (normally they are automatically emptied by the OS on reboot).
 *
 * @param {String} formUrl URL of the form to fill
 * @param {Function} formFiller Function used in the page's console context to fill the form
 * given some form parameters to enter
 * @param {Array<Object>} formParameters List of parameters that have to be given to the
 * form filler function to fill a form
 *
 * @returns {Promise<Array<Promise>>} An array of promises, each resolves when the formFiller is
 * evaluated in its respective page's context. Or rejects if there is an error.
 */
module.exports = async function automatedFillForms(
  formUrl,
  formFiller,
  formParameters
) {
  const USER_DATA_DIR = path.join(os.tmpdir(), "puppeteer_user_data_dir");
  const MILLISECONDS_TO_WAIT_BETWEEN_TABS = 1000;

  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: USER_DATA_DIR
  });

  return formParameters.map(async (params, index) => {
    // Go to the form page in a new tab after
    // waiting some time to not abuse the service
    const page = await browser.newPage();
    await page.waitFor(index * MILLISECONDS_TO_WAIT_BETWEEN_TABS);
    await page.goto(formUrl, { waitUntil: "domcontentloaded" });

    // Fill the form
    return page.evaluate(formFiller, params);
  });
};
