const path = require("path");
const puppeteer = require("puppeteer");
const fillFormAndDownloadCSVs = require("./automatedFillForms");

const FORM_URL =
  "http://www.gobiernodecanarias.org/medioambiente/calidaddelaire/datosHistoricos.do";
const USER_DATA_DIR = path.join("puppeteer_user_data_dir");
const TIME_TO_WAIT_FOR_LOAD = 1000;
const DEFAULT_NAVIGATION_TIMEOUT = 60000;

async function downloadAreaData(browser, area, dates) {
  for (let i = 0; i < dates.length; ++i) {
    const page = await browser.newPage();
    const isIterationMultipleOfFive = (i + 1) % 5 === 0;

    if (isIterationMultipleOfFive) {
      console.log(
        "Waiting a bit more before continuing to avoid overloading the system\n"
      );
      await page.waitFor(TIME_TO_WAIT_FOR_LOAD * 10);
    } else {
      await page.waitFor(TIME_TO_WAIT_FOR_LOAD);
    }

    try {
      page.setDefaultNavigationTimeout(DEFAULT_NAVIGATION_TIMEOUT);
      await page.goto(FORM_URL, { waitUntil: "domcontentloaded" });
      const downloadInfos = await fillFormAndDownloadCSVs(page, area, dates[i]);

      if (!downloadInfos || downloadInfos.length === 0) {
        console.warn(`[WARN] Nothing to download found in form #${i + 1}\n\n`);
      }

      await page.waitFor(TIME_TO_WAIT_FOR_LOAD);
      await page.close();
      console.log(`Finished form #${i + 1}\n\n`);
    } catch (error) {
      console.error(`[ERROR] Error in form #${i + 1}\n\n`, error);
    }
  }
}

async function main() {
  const paramsPath = path.join(__dirname, "../parameters.json");
  const params = require(paramsPath);
  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: USER_DATA_DIR
  });

  for (let i = 0; i < params.length; ++i) {
    const { area, dates } = params[i];
    await downloadAreaData(browser, area, dates);
  }
}

main();
