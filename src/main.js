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

  for (let i = 0; i < params.length; ++i) {
    const page = await browser.newPage();

    try {
      await page.waitFor(1000);
      await page.goto(formUrl, { waitUntil: "domcontentloaded" });
      await fillFormAndDownloadCSVs(page, params[i]);

      console.log(`Finished filling form #${i + 1}\n\n`);
      await page.waitFor(1000);
      await page.close();
    } catch (error) {
      console.error(`Error in form #${i + 1}\n\n`, error);
    }
  }
}

main();
