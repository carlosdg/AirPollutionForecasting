# Helper Program To Download Canary Islands Air Quality Data

This is a helper program for a project. The goal was to use air quality data for a data science project. The problem was that the [page for downloading the data](http://www.gobiernodecanarias.org/medioambiente/calidaddelaire/datosHistoricos.do) doesn't have an API for programmatically downloading the data, a form has to be filled for each year, month and area and it takes a lot of time. Also it is very easy to do something wrong. So this project was made to make the form fill easier without abusing the system and trying to make the POST request directly.

## Use

- After downloading/cloning the repository run `npm install` to install the project's dependencies
- Fill the `parameters.json` file with the parameters that you want to insert into the form. The JSON object representing the parameters has to have the following structure:

  ```json
    { 
      "year": 2016, 
      "monthIndex": 0, 
      "area": "casa cuna" 
    },
  ```

  Where `year` is an integer between 2008 and the current year (included), `monthIndex` is an integer between 0 and 11 (included, in case of the year being the current year the monthIndex cannot be passed than the current month). And `area` is the area exact name (case insensitive).

  `parameters.json` expects an array of these objects.

- Run with `npm start`. A chromium browser will show and a new tab will be opened for each element in the array with the form filled.

__Note:__ The browser's user data is store in a Operating System tmp directory. This is in case the user wants to customize some settings they will be persisted until the tmp directory is emptied (normally they are automatically emptied by the OS on reboot). This is, for example, to not having to change the `Downloads` location everytime we run the application