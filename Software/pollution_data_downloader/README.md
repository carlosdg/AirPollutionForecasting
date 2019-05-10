# Helper Program To Download Canary Islands Air Quality Data

This is a helper program for a project. The goal was to use air quality data for a data science project. The problem was that the [page for downloading the data](http://www.gobiernodecanarias.org/medioambiente/calidaddelaire/datosHistoricos.do) doesn't have an API for programmatically downloading the data, a form has to be filled for each year, month and area and it takes a lot of time. Also it is very easy to do something wrong. So this project was made to make the form fill easier without abusing the system and trying to make the POST request directly.

## Use

- After downloading/cloning the repository run `npm install` to install the project's dependencies and create the `src/downloads` directory.

  ```sh
    npm install && mkdir src/downloads
  ```

- Fill the `parameters.json` file with the parameters that you want to insert into the form. The JSON object representing the parameters has to have the following structure:

  ```json
  {
    "area": "casa cuna",
    "dates": [{ "year": 2019, "monthIndex": 3 }]
  }
  ```

  Where `year` is an integer between the first possible year and the current year (included), `monthIndex` is an integer between 0 and 11 (included, in case of the year being the current year the monthIndex cannot be passed than the current month). And `area` is the area exact name (case insensitive).

  `parameters.json` expects an array of these objects. Example:

```json
[
  {
    "area": "casa cuna",
    "dates": [{ "year": 2019, "monthIndex": 3 }]
  },
  {
    "area": "tome cano",
    "dates": [
      { "year": 2019, "monthIndex": 0 },
      { "year": 2019, "monthIndex": 1 },
      { "year": 2019, "monthIndex": 2 },
      { "year": 2019, "monthIndex": 3 }
    ]
  }
]
```

- Run with `npm start`. A chromium browser will open and progressively fill each form, go to the result page and download all the CSVs. Each CSV will be located inside a `downloads` folder located where you run the script

**Note:** The browser's user data is store in a `src/puppeteer_user_data_dir` directory. This is in case the user wants to customize some settings they will be persisted.
