# Helper Functions To Download Canary Islands Air Quality Data

These are some helpers functions made for a college project. The goal was to use air quality data for a data science project. The problem was that the [page for downloading the data](http://www.gobiernodecanarias.org/medioambiente/calidaddelaire/datosHistoricos.do) is not very friendly, a form has to be filled for each year and area and it takes a lot of time. Also it is very easy to do something wrong. So these functions were made to make that task easier.

## Author

* Carlos Domínguez García (alu0100966589@ull.edu.es)

## How to use

These functions were made to use in the console of [the web page](http://www.gobiernodecanarias.org/medioambiente/calidaddelaire/datosHistoricos.do). You have to copy and paste the functions there and call them like shown below

### Fill form

We wanted to download daily data for particular areas, so the only thing that was different from one request and the next was the area and/or the year (because we can only download a year at a time). So filling the form for each year and area was a tedious job.

The `fillForm` function is there to help doing that job. You only have to specify the year and area that you want and it will fill and submit the form.

Example of calling the function (remember that has to be in the console of the page)

```
fillForm(2017, "parque la granja");
```

### Download all CSV

Once submitted the form, you'll see the data that you requested, there we were interested in the CSV files and because there were a few of them and the page size could be very large, the `downloadAllCsv` function was made to download all CSV files there.

Example of calling the function (remember that has to be in the console of the page with the data to download)

```
downloadAllCsv();
```
