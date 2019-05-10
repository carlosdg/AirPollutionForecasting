const fs = require("fs");
const util = require("util");
const path = require("path");

const mkdir = util.promisify(fs.mkdir);
const readdir = util.promisify(fs.readdir);
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

/**
 * This function automates the task of filling the form of air data quality of the
 * Canary Islands government. It has to be called in the browser's console of the
 * form web page
 *
 * @param {Object} parameters An object with the following properties:
 * - {Number} year: Integer denoting the year
 * - {Number} monthIndex: Integer denoting the month ranging between [0, 11]
 * - {String} area: Area to download data from
 */
function fillForm({ year = 2015, monthIndex = 0, area = "" } = {}) {
  // First year in the select list (index 0)
  const FIRST_POSSIBLE_YEAR = parseInt(
    Array.from(document.getElementById("selAnioIni").options)
      .map(option => option.text)
      .shift(),
    10
  );

  // Index of the year asked in the select list
  const yearIndex = Math.floor(year - FIRST_POSSIBLE_YEAR);

  // Get current date to check that the given date parameters are before the current date
  const currentDate = new Date();

  // Check that the year is valid
  if (yearIndex < 0 || year > currentDate.getFullYear()) {
    throw new Error(
      `Invalid year "${year}". It has to be between ${FIRST_POSSIBLE_YEAR} and ${currentDate.getFullYear()}`
    );
  }

  // Check that the month index refers to a valid month
  if (monthIndex < 0 || monthIndex > 11) {
    throw new Error(
      `Invalid month "${monthIndex}". It has to be in the range [0, 11]`
    );
  }

  // Check that the given month index is before the current
  // month if the year if the current year
  if (
    year === currentDate.getFullYear() &&
    monthIndex >= currentDate.getMonth()
  ) {
    throw new Error(
      `Invalid month "${monthIndex}". It has to be in the range [0, ${currentDate.getMonth()})`
    );
  }

  // Select hourly historical data
  document.getElementById("pinteg").selectedIndex = 0;

  // Select the given month as initial month
  document.getElementById("selMesIni").selectedIndex = monthIndex;

  // Select the given year as initial year
  document.getElementById("selAnioIni").selectedIndex = yearIndex;

  // This is a function defined in the page, this updates the calendar based on the previous selections
  updateCalIni();

  // Select the given month as final month
  document.getElementById("selMesFin").selectedIndex = monthIndex;

  // Select final year
  document.getElementById("selAnioFin").selectedIndex = yearIndex;

  // This is a function defined in the page, this updates the calendar based on the previous selections
  updateCalFin();

  // Select first day of the initial calendar
  document.querySelector("#cal1 td a").click();

  // Select last day in the final calendar
  // (We conver the node list to an array and take the last element with pop)
  [...document.querySelectorAll("#cal2 td a")].pop().click();

  // Select the area
  const stationSelect = document.getElementById("tbEstaciones"); // HTML select element
  const options = [...stationSelect.options]; // array of HTML options

  // Look for the options that matches the area asked
  const validOptions = options.filter(option =>
    option.textContent.toUpperCase().includes(area.toUpperCase())
  );

  // Throw if there is no option named like the given area
  if (validOptions.length <= 0) {
    throw new Error(
      `Couldn't find area "${area}". Maybe there is a tilde missing`
    );
  }

  // Select the first valid option
  stationSelect.selectedIndex = validOptions[0].index;

  // Trigger the "change" event
  stationSelect.dispatchEvent(new Event("change"));
}

/**
 * Calls the downloader and waits until the file downloads.
 *
 * NOTE: right now we need to use a folder for each downloaded file to track it
 * progress
 *
 * @param {any} page Puppeteer page object
 * @param {string} downloadFolderPath Path to the folder to place the downloads
 * @param {any} downloader Function that triggers the download
 */
async function download(page, downloadFolderPath, downloader) {
  const randomString = Math.random()
    .toString(36)
    .substr(2, 8);
  const randomFolderName = `download-${randomString}`;

  // Folder to place the unique download. Needed so we can track its download
  // progress
  const downloadPath = path.resolve(downloadFolderPath, randomFolderName);

  await mkdir(downloadPath, { recursive: true });
  await page._client.send("Page.setDownloadBehavior", {
    behavior: "allow",
    downloadPath
  });
  await downloader();

  let fileName;
  const timeBeforeNextTry = 100;

  while (!fileName || fileName.endsWith(".crdownload")) {
    await sleep(timeBeforeNextTry);
    [fileName] = await readdir(downloadPath);
  }

  return { fileName, downloadPath };
}

/**
 * Downloads all the CSV files in the given page
 *
 * @param {any} page Puppeteer page object
 * @param {string} downloadFolderPath Path to the folder to place the downloads
 */
async function downloadAllCSVs(page, downloadFolderPath) {
  const spans = await page.$$("span.export.csv");
  const downloadInfos = [];

  for (const span of spans) {
    const downloaderFunction = () => {
      console.log("Downloading...");
      span.click();
    };
    const downloadInfo = await download(
      page,
      downloadFolderPath,
      downloaderFunction
    );
    downloadInfos.push(downloadInfo);
  }

  console.log(`
Download path: ${downloadFolderPath}
Downloads. Expected: ${spans.length}. Got: ${downloadInfos.length}
  `);

  return downloadInfos;
}

/**
 * Fills the form of the given page with the given parameters, submits the form,
 * waits for the result page to load and downloads all the CSV files there
 *
 * @param {any} page Puppeteer page object
 * @param {any} params Form parameters to fill for this page
 */
async function fillFormAndDownloadCSVs(page, area, date) {
  const timeToWaitBeforeClick = 1000;

  await page.evaluate(fillForm, { area, ...date });
  await page.waitFor(timeToWaitBeforeClick);
  await page.click('[name="btAgregar"]');

  await page.waitFor(timeToWaitBeforeClick);
  await page.click('[type="submit"]');
  await page.waitForNavigation({ waitUntil: "domcontentloaded" });

  const { year, monthIndex } = date;
  const cleanAreaString = area.toLowerCase().replace(" ", "_");
  const areaDownloadFolderPath = path.resolve("downloads", cleanAreaString);

  await mkdir(areaDownloadFolderPath, { recursive: true });

  const monthString = (monthIndex + 1).toString().padStart(2, "0");
  const monthDataFolderName = `${year}_${monthString}`;
  const downloadPath = path.resolve(
    areaDownloadFolderPath,
    monthDataFolderName
  );

  return downloadAllCSVs(page, downloadPath);
}

module.exports = fillFormAndDownloadCSVs;
