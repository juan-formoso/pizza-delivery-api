import { DocumentDefinition } from "mongoose";
import UserModel, { UserDocument } from "../models/user.model";

export const createUser = async (
  input: DocumentDefinition<
    Omit<UserDocument, "createdAt" | "updatedAt" | "comparePassword">
  >
) => {
  try {
    const user = await UserModel.create(input);
    return user;
  } catch (error: any) {
    throw new Error(error);
  }
};
