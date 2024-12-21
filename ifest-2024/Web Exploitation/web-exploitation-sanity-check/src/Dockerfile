FROM node:18-alpine

COPY package* .

RUN npm install

COPY . .

RUN npm run build

RUN cp -r src/views dist/

EXPOSE 3000

CMD ["npm", "run", "start"]