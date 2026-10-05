import { Router } from "express";
import { getHealth } from "../services/health"

export const healthRouter = Router();

healthRouter.get("/", (_req, res) => {
    res.json(getHealth());
});

export default healthRouter;