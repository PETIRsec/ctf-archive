import { v4 } from "uuid";
import { Safe } from "../types/safe";
import dotenv from "dotenv";

dotenv.config()


export const safeList : Safe[] = [
    {
        id: v4(),
        title: "Liqued's secret",
        password: "liqued",
        content: "I just bought PS5 last week, please dont tell my parent's they will kill me !"
    },
    {
        id: v4(),
        title: "Flag ? maybe ?",
        password: v4(),
        content: process.env.FLAG || "IFEST{fake_flag}"
    }
]