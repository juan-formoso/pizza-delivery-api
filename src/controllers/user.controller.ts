import { Request, Response } from "express";
import { CreateUserInput } from "../schemas/user.schema";
import { createUser } from "../services/user.service";
import pino from "../utils/logger";

export const createUserHandler = async (
  req: Request<{}, {}, CreateUserInput["body"]>,
  res: Response
) => {
  try {
    // call create user service
    const user = await createUser(req.body);
    return user;
  } catch (error: any) {
    // if this function throws it will be because it has violated the unique email restriction in UserModel
    pino.error(error);
    return res.status(409).send(error.message); // conflict
  }
};
