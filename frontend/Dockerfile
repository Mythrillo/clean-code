FROM node:19-alpine

WORKDIR /app

COPY package.json .
COPY package-lock.json .
COPY yarn.lock .

RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY . .
CMD ["npm", "start"]
