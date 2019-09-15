# API

Here you can find the code of an API that connects to the data warehouse and provide three services:

- Information about the data. More specifically the name of the measure variables
    
    URL: /apf/api/v1.0/meta

- List of the last `n` measures in the system for the asked variable starting from a given offset:
    
    URL: /apf/api/v1.0/measures/[variable]/[n]/[offset]

- Forecasts the mean concentration of PM2.5 for the next 24 hours starting from the given timestamp:
    
    URL: /apf/api/v1.0/forecast/24/[timestamp]