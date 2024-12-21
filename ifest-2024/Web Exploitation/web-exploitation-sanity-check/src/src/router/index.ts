import express, { Router } from "express"
import { router as homeRoute } from "./home/route"
import { router as secretRoute } from "./secret/route"

export const router : Router = Router()

router.use(homeRoute)
router.use(secretRoute)