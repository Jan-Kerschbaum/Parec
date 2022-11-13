#version 1
FROM node:16-alpine

WORKDIR /app
COPY . ./
RUN npm install

CMD ["npm", "run", "prod"]

#version 2
# FROM node:18 AS build

# WORKDIR /app

# COPY package.json ./
# COPY package-lock.json ./
# RUN npm install
# COPY . ./
# RUN npm run build

# FROM nginx:1.19-alpine
# COPY --from=build /app/dist /usr/share/nginx/html