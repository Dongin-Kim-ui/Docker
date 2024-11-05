FROM node:lts-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/joe-brothers/minesweeper.git
WORKDIR /minesweeper
RUN npm install

EXPOSE 3000

CMD ["npm", "start"]

