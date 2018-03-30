/**
 * This function automates the task of filling the form of air data quality of the
 * Canary Islands government.
 * 
 * This function has to be copied to the console of the page where the form is located.
 * Then it has to be called like 
 * 
 *      fillForm(2015, "parque la granja")
 * 
 * If the year or the area is invalid then a message will let you know it. Once the function is
 * called you have to wait a little bit and the page will navigate to where the data is.
 * There you can use the downloadAllCsv function to download all csv files.
 * 
 * Maybe you need to change the milliseconds specified to wait, because that is to wait 
 * for HTTP requests.
 * 
 * @param {Number} year Integer denoting the year
 * @param {String} area Area to download data from
 */
function fillForm(year = 2015, area = "") {
    // First year in the select list (index 0)
    const FIRST_POSSIBLE_YEAR = 2008;

    // Index of the year asked in the select list
    const yearIndex = Math.floor(year - FIRST_POSSIBLE_YEAR);

    // Check that the year is valid
    if (yearIndex < 0 || year > (new Date()).getFullYear()) {
        console.error(`Invalid year "${year}"`);
        return;
    }

    // Select daily historical data
    document.getElementById('pinteg').selectedIndex = 2;

    // Select January as initial month
    document.getElementById('selMesIni').selectedIndex = 0;

    // Select initial year
    document.getElementById('selAnioIni').selectedIndex = yearIndex;

    // This is a function defined in the page, this updates the calendar based on the previous selections
    updateCalIni();

    // Select December as final month
    document.getElementById('selMesFin').selectedIndex = 11;

    // Select final year
    document.getElementById('selAnioFin').selectedIndex = yearIndex;

    // This is a function defined in the page, this updates the calendar based on the previous selections
    updateCalFin();

    // Select first day of the initial calendar
    document.querySelector('#cal1 td a').click();

    // Select last day in the final calendar
    // (We conver the node list to an array and take the last element with pop)
    [...document.querySelectorAll('#cal2 td a')].pop().click();

    // Select the area
    const stationSelect = document.getElementById('tbEstaciones');   // HTML select element
    const options = [...stationSelect.options];                      // array of HTML options

    // Look for the options that matches the area asked
    const validOptions = options.filter(option => option.textContent.toUpperCase().includes(area.toUpperCase()));
    if (validOptions.length > 0) {
        // Take the first valid option
        stationSelect.selectedIndex = validOptions.shift().index;

        // Trigger the "change" event
        stationSelect.dispatchEvent(new Event('change'));
    
        // We have to wait for the previous event to be done because it sends an HTTP request that has to be
        // resolved before continuing
        const millisecondsToWaitToClick = 1000;
        window.setTimeout(() => {
            document.querySelector('input[type="button"][name="btAgregar"][value="Agregar"]').click();

            // Finally click the submit button to submit the form
            window.setTimeout(() => {
                document.getElementById('btEnviar').click();
            }, millisecondsToWaitToClick);
        }, millisecondsToWaitToClick);
    }
    else {
        console.error(`Couldn't find area "${area}". Maybe there is a tilde missing`);
    }
}