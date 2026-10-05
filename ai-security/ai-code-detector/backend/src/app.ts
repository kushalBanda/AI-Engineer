// This builds the Express app and registers the routes
import express from "express";
import cors from "cors";
import healthRouter from "./routes/health";
import detectRouter from "./routes/detect";

export const createApp = () => {
    const app = express();
    app.use(cors())
    app.use(express.json())
    app.use("/health", healthRouter);
    app.use("/api/detect", detectRouter);
    return app;
}