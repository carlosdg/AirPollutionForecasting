## Remember to set the API_BASE_URL 
## environment variable at build time and the 
## PORT environment variable at run time
FROM node:11

WORKDIR /web

# Install the static server that will serve the contents
RUN yarn global add serve

# Copy package.json and install dependencies
COPY package.json ./
RUN yarn

# Copy code
ADD . ./

# Require the API URI environment variable
# with some default value
ARG API_BASE_URL=http://localhost:5000

# Set the API URI environment variable & build the app for production
ENV API_BASE_URL=$API_BASE_URL
RUN yarn run build

CMD serve --listen $PORT --single dist --no-clipboard