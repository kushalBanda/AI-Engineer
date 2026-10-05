import Anthropic from "@anthropic-ai/sdk";
import { getPool } from "../db/db";
import { extractJson } from "../utils/extractJson";

const model = "claude-haiku-4-5-20251001";
const systemPrompt = "You classify if code is AI-generated. Return ONLY JSON with keys: score (0-1), label (ai|human|uncertain), rationale (short).";
const userPrompt =
    "Code: {code}\nLanguage: {language} Return Json only, no other text.";
const maxTokens = 300;
const temperature = 0;

const detectCode = async (code: string, language?: string) => {
    const anthropic = new Anthropic({
        apiKey: process.env.ANTHROPIC_API_KEY,
    });

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
            text: userPrompt.replace("{code}", code).replace("{language}", language ?? ""),
        },
        ],
    },
    ],
});

    const text = response.content.find((b) => b.type === "text")?.text ?? "";
    const parsed =
        extractJson(text) ?? { score: 0, label: "uncertain", rationale: "No JSON found" };

    await getPool().query(
        "INSERT INTO code_review.detection_requests (code, language, result) VALUES ($1, $2, $3)",
        [code, language ?? null, JSON.stringify(parsed)]
    );

    return parsed;
};

export default detectCode;