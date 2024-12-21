import express, { Express, Request, Response } from "express";
import dotenv from "dotenv";
import { router } from "./router";

dotenv.config();

const app: Express = express();
const port = process.env.PORT || 3000;
app.set('views', __dirname + '/views')
app.set('view engine', 'ejs');


app.use(router)

app.listen(port, () => {
  console.log(`[server]: Server is running at http://localhost:${port}`);
});