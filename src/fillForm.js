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
module.exports = function fillForm({
  year = 2015,
  monthIndex = 0,
  area = ""
} = {}) {
  // First year in the select list (index 0)
  const FIRST_POSSIBLE_YEAR = 2008;

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
};
