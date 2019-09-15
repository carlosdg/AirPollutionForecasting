# Web page

Here you can find the code for the web page. This page connects to the API and shows the latest measures in the system and allows the users to see forecasts for the mean of PM2.5 in the next 24 hours from a given timestamp.

## Run

Set the location of the API in a `.env` file as seen in `.env.example`. Then run:

```
yarn start
```

To build the docker image you need to specify the location to the API. For example:

```
docker build -t web --build-arg API_BASE_URL=http://localhost:5000 .
```