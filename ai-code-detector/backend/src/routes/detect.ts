import { Router } from "express";
import detectCode from "../services/detect";

export const detectRouter = Router();

detectRouter.post("/", async (req, res) => {
    const { code, language } = req.body;
    const result = await detectCode(code, language);
    res.json(result);
});

export default detectRouter;