FROM node:8.9.0-alpine
WORKDIR /app

COPY package*.json ./

# RUN cp ~/.npmrc ~/.npmrc.bak
# RUN npm config del _token   
RUN npm install

COPY src /app

EXPOSE 8080

CMD ["node", "server.js"]
