import { Request, Response, Router } from "express";
import { safeList } from "../../utils/constant";

export const router : Router = Router()

router.get("/", (req : Request, res : Response)=>{
    return res.render("home", {safeList: safeList})
})