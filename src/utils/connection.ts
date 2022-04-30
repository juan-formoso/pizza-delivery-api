import mongoose from "mongoose";
import config from "config";
import logger from "./logger";

const connection = async () => {
  const dbUrl = config.get<string>("dbUrl");

  try {
    await mongoose.connect(dbUrl);
    logger.info(`Connected to ${dbUrl}`);
  } catch (error) {
    logger.error("Error connecting to database: ", error);
    process.exit(1);
  }
};

export default connection;
