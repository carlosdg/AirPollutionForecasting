const path = require("path");
const puppeteer = require("puppeteer");
const fillFormAndDownloadCSVs = require("./automatedFillForms");

// Load the json file with the parameters
const params = require(path.join(__dirname, "../parameters.json"));
const formUrl =
  "http://www.gobiernodecanarias.org/medioambiente/calidaddelaire/datosHistoricos.do";

async function main() {
  const USER_DATA_DIR = path.join(__dirname, "puppeteer_user_data_dir");

  const browser = await puppeteer.launch({
    headless: false,
    userDataDir: USER_DATA_DIR
  });

  const timeToWaitForLoads = 1000;

  for (let i = 0; i < params.length; ++i) {
    const page = await browser.newPage();
    const isIterationMultipleOfFive = (i + 1) % 5 === 0;

    if (isIterationMultipleOfFive) {
      console.log(
        "Waiting a bit more before continuing to avoid overloading the system\n"
      );
      await page.waitFor(timeToWaitForLoads * 10);
    } else {
      await page.waitFor(timeToWaitForLoads);
    }

    try {
      await page.goto(formUrl, { waitUntil: "domcontentloaded" });
      const downloadInfos = await fillFormAndDownloadCSVs(page, params[i]);

      if (!downloadInfos || downloadInfos.length === 0) {
        console.warn(`[WARN] Nothing to download found in form #${i + 1}\n\n`);
      }

      await page.waitFor(timeToWaitForLoads);
      await page.close();
      console.log(`Finished form #${i + 1}\n\n`);
    } catch (error) {
      console.error(`[ERROR] Error in form #${i + 1}\n\n`, error);
    }
  }
}

main();
