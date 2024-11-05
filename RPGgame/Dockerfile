FROM node:lts-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/delaford/game.git
WORKDIR /game
RUN npm install

EXPOSE 8080

CMD ["npm", "start"]

