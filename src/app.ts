import express from "express";
import config from "config";
import connection from "./utils/connection";
import logger from "./utils/logger";
import routes from "./routes";

const port = config.get<number>("port");
const app = express();

app.listen(port, async () => {
  logger.info(`App is running at http://localhost:${port}`);

  await connection();

  routes(app);
});
