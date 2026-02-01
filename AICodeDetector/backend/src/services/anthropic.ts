import "dotenv/config";
import express from "express";
import cors from "cors";
import Anthropic from "@anthropic-ai/sdk";
import { pool } from "../db";

const app = express();
app.use(cors());
app.use(express.json());

const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
});


const port = 3001;
const model = "claude-haiku-4-5-20251001";
const systemPrompt = "You classify if code is AI-generated. Return ONLY JSON with keys: score (0-1), label (ai|human|uncertain), rationale (short).";
const userPrompt = "Code: {code}\nLanguage: {language} Return Json only, no other text.";
const maxTokens = 300;
const temperature = 0;


const extractJson = (text: string) => {
    const start = text.indexOf("{");
    const end = text.lastIndexOf("}");
    if (start === -1 || end === -1) return null;
    try {
        return JSON.parse(text.slice(start, end + 1));
    } catch {
        return null;
    }
};

app.get("/health", (_req, res) => {
    res.json({ ok: true });
});


app.post("/api/detect", async (req, res) => {
    const { code, language } = req.body;

    const response = await anthropic.messages.create({
        model,
        max_tokens: maxTokens,
        temperature,
        system: systemPrompt,
        messages: [
        {
            role: "user",
            content: [
            {
                type: "text",
                text: userPrompt.replace("{code}", code).replace("{language}", language),
            }
            ]
        }
        ]
    });

    const text = response.content.find((b) => b.type === "text")?.text ?? "";
    const parsed = extractJson(text) ?? {
        score: 0, 
        label: "uncertain",
        rationale: "No JSON found"
    };

    await pool.query(
        "INSERT INTO code_review.detection_requests (code, language, result) VALUES ($1, $2, $3)",
        [code, language ?? null, JSON.stringify(parsed)]
    );

    res.json(parsed);
});


app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
