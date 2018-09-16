const path = require("path");
const fillForm = require("./fillForm");
const automatedFillForms = require("./automatedFillForms");

// Load the json file with the parameters
const PARAMS = require(path.join(__dirname, "../parameters.json"));

const FORM_URL =
  "http://www.gobiernodecanarias.org/medioambiente/calidaddelaire/datosHistoricos.do";

// Fill the forms and after each is done log a message
automatedFillForms(FORM_URL, fillForm, PARAMS).then(promises =>
  promises.map((promise, index) =>
    promise
      .then(() => console.log(`Finished filling form #${index}`))
      .catch(error => console.error(`Error in form #${index}`, error))
  )
);
