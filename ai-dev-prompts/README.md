# Official Prompting Guides

A curated index of prompting guides published **by the model providers themselves**. No third-party blogs, no "ultimate prompt" threads. If a provider ships a model-specific guide, it is listed next to the general one, because advice changes between model generations.

Every guide that is a public web page also has an offline PDF copy in a per-provider folder (`anthropic/`, `openai/`, `google/`, ...), captured in October 2026. The links are the source of truth; the PDFs are snapshots and will go stale as providers update their docs.

## Contents

- [Anthropic (Claude)](#anthropic-claude)
- [OpenAI (GPT, o-series, Codex)](#openai-gpt-o-series-codex)
- [Google (Gemini, Gemma)](#google-gemini-gemma)
- [Meta (Llama)](#meta-llama)
- [Mistral](#mistral)
- [Cohere (Command)](#cohere-command)
- [xAI (Grok)](#xai-grok)
- [DeepSeek](#deepseek)
- [Alibaba (Qwen)](#alibaba-qwen)
- [Moonshot (Kimi)](#moonshot-kimi)
- [Amazon (Nova, Bedrock)](#amazon-nova-bedrock)
- [Microsoft (Azure OpenAI)](#microsoft-azure-openai)
- [IBM (Granite)](#ibm-granite)
- [AI21 (Jamba)](#ai21-jamba)
- [Perplexity (Sonar)](#perplexity-sonar)
- [Files in this folder](#files-in-this-folder)

## Anthropic (Claude)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Where to start, when prompting is (and isn't) the fix | [PDF](./anthropic/Claude%20Prompt%20Engineering%20Overview.pdf) |
| [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | The living reference: clarity, examples, XML tags, roles, thinking, long context, agents | [PDF](./anthropic/Claude%20Prompting%20Best%20Practices.pdf) |
| [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) | Model-specific notes for Opus 5.5 | [PDF](./anthropic/Prompting%20Claude%20Opus%205.5.pdf) |
| [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) | Model-specific notes for Sonnet 5.5 | [PDF](./anthropic/Prompting%20Claude%20Sonnet%205.5.pdf) |
| [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) | Model-specific notes for Haiku 5.5 | [PDF](./anthropic/Prompting%20Claude%20Haiku%205.5.pdf) |
| [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) | Model-specific notes for Fable 5.1 | [PDF](./anthropic/Prompting%20Claude%20Fable%205.1.pdf) |
| [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) | Prompting and budgeting reasoning | [PDF](./anthropic/Claude%20Extended%20Thinking.pdf) |
| [System prompt release notes](https://platform.claude.com/docs/en/release-notes/system-prompts/overview) | Anthropic's own published claude.ai system prompts | — |
| [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 9-chapter hands-on course (Jupyter) | — |
| [Anthropic courses](https://github.com/anthropics/courses) | API fundamentals, real-world prompting, prompt evals, tool use | — |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context as a finite resource for agents | [PDF](./anthropic/Effective%20Context%20Engineering%20for%20AI%20Agents.pdf) |
| [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Tool descriptions as prompts | [PDF](./anthropic/Writing%20Tools%20for%20Agents.pdf) |
| [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices) | Prompting an agentic coding tool | [PDF](./anthropic/Claude%20Code%20Best%20Practices.pdf) |

## OpenAI (GPT, o-series, Codex)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompting](https://developers.openai.com/api/docs/guides/prompting) | Current general guide: messages, roles, reusable prompts | [PDF](./openai/OpenAI%20Prompting.pdf) |
| [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) | Core strategies and message formatting | [PDF](./openai/OpenAI%20Prompt%20Engineering.pdf) |
| [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra) | Latest model family, with a prompting best practices section | [PDF](./openai/Using%20GPT-6.pdf) |
| [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices) | How to prompt reasoning models differently from chat models | [PDF](./openai/OpenAI%20Reasoning%20Best%20Practices.pdf) |
| [GPT-5.2 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide) | `reasoning_effort`, verbosity, agentic scaffolding | [PDF](./openai/GPT-5.2%20Prompting%20Guide.pdf) |
| [GPT-5.1 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5-1_prompting_guide) | Personality, steerability, `none` reasoning mode | [PDF](./openai/GPT-5.1%20Prompting%20Guide.pdf) |
| [GPT-5 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide) | Agentic eagerness, tool preambles, coding | [PDF](./openai/GPT-5%20Prompting%20Guide.pdf) |
| [GPT-4.1 prompting guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide) | Literal instruction following, long context, agent prompts | [PDF](./openai/GPT-4.1%20Prompting%20Guide.pdf) |
| [o3 / o4-mini prompting guide](https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide) | Function calling with reasoning models | [PDF](./openai/o3%20and%20o4-mini%20Prompting%20Guide.pdf) |
| [Codex prompting guide (cookbook)](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) | Prompting Codex models for coding agents | [PDF](./openai/Codex%20Prompting%20Guide.pdf) |
| [Prompting Codex](https://developers.openai.com/codex/prompting) | Writing good tasks for the Codex agent | [PDF](./openai/Prompting%20Codex.pdf) |
| [Prompt optimization cookbook](https://cookbook.openai.com/examples/gpt-5/prompt-optimization-cookbook) | Using the prompt optimizer to fix contradictions and ambiguity | [PDF](./openai/Prompt%20Optimization%20Cookbook.pdf) |
| [Prompting Realtime models](https://developers.openai.com/api/docs/guides/voice-prompting) | Voice agents: tone, pacing, turn-taking | [PDF](./openai/Prompting%20Realtime%20Models.pdf) |
| [Realtime prompting guide (cookbook)](https://cookbook.openai.com/examples/realtime_prompting_guide) | Worked voice-agent prompt examples | [PDF](./openai/Realtime%20Prompting%20Guide.pdf) |
| [Prompting GPT-Live](https://developers.openai.com/api/docs/guides/live-prompting) | Live speech model prompting | [PDF](./openai/Prompting%20GPT-Live.pdf) |
| [Image prompting](https://developers.openai.com/api/docs/guides/image-prompting) | Prompting image generation and editing | [PDF](./openai/OpenAI%20Image%20Prompting.pdf) |
| [Image gen models prompting guide](https://cookbook.openai.com/examples/multimodal/image-gen-models-prompting-guide) | Worked image prompt examples | [PDF](./openai/Image%20Gen%20Models%20Prompting%20Guide.pdf) |
| [Sora 2 prompting guide](https://cookbook.openai.com/examples/sora/sora2_prompting_guide) | Video: shots, camera, timing, style | [PDF](./openai/Sora%202%20Prompting%20Guide.pdf) |
| [A practical guide to building agents (PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | Agent instructions, tools, guardrails | [PDF](./openai/A%20Practical%20Guide%20to%20Building%20Agents.pdf) |

## Google (Gemini, Gemma)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) | Core Gemini API prompting guide | [PDF](./google/Gemini%20Prompt%20Design%20Strategies.pdf) |
| [Gemini 3 developer guide](https://ai.google.dev/gemini-api/docs/gemini-3) | Gemini 3 prompting changes: temperature, thinking level, shorter prompts | [PDF](./google/Gemini%203%20Developer%20Guide.pdf) |
| [What's new in Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5) | Migration and prompting notes for 3.5 | [PDF](./google/Whats%20New%20in%20Gemini%203.5%20Flash.pdf) |
| [File prompting strategies](https://ai.google.dev/gemini-api/docs/file-prompting-strategies) | Prompting with images, video, audio, PDFs | [PDF](./google/Gemini%20File%20Prompting%20Strategies.pdf) |
| [Image generation (Nano Banana)](https://ai.google.dev/gemini-api/docs/image-generation) | Image prompts and editing | [PDF](./google/Gemini%20Image%20Generation.pdf) |
| [Video generation (Veo 3.1)](https://ai.google.dev/gemini-api/docs/veo) | Veo 3.1 usage and prompt guide | [PDF](./google/Veo%203.1%20Video%20Generation%20and%20Prompt%20Guide.pdf) |
| [Lyria prompt guide](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide) | Music generation prompting | [PDF](./google/Lyria%20Prompt%20Guide.pdf) |
| [Introduction to prompting (Google Cloud)](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design) | Enterprise prompting docs and strategies | [PDF](./google/Google%20Cloud%20Introduction%20to%20Prompting.pdf) |
| [Gemma prompt structure](https://ai.google.dev/gemma/docs/core/prompt-structure) | Gemma chat template and formatting | [PDF](./google/Gemma%20Prompt%20Structure.pdf) |
| [Gemini for Workspace prompt guide](https://workspace.google.com/learning/content/gemini-prompt-guide) | Prompting Gemini in Docs, Gmail, Sheets | — |
| [Prompt engineering whitepaper](https://www.kaggle.com/whitepaper-prompt-engineering) | Google's 68-page model-agnostic whitepaper | [PDF](./google/Prompt%20Engineering%20Whitepaper.pdf) |

## Meta (Llama)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt engineering](https://www.llama.com/docs/how-to-guides/prompting/) | Official Llama prompting how-to | [PDF](./meta/Llama%20Prompt%20Engineering.pdf) |
| [Model cards and prompt formats](https://www.llama.com/docs/model-cards-and-prompt-formats/) | Special tokens and chat templates per Llama version | [PDF](./meta/Llama%20Model%20Cards%20and%20Prompt%20Formats.pdf) |

## Mistral

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompting capabilities](https://docs.mistral.ai/guides/prompting_capabilities) | System vs user prompts, Markdown/XML structure, few-shot, worked examples | [PDF](./mistral/Mistral%20Prompting%20Capabilities.pdf) |

## Cohere (Command)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Crafting effective prompts](https://docs.cohere.com/docs/crafting-effective-prompts) | General Command prompting | [PDF](./cohere/Cohere%20Crafting%20Effective%20Prompts.pdf) |
| [Prompting Command R / R+](https://docs.cohere.com/docs/prompting-command-r) | Model-specific template, RAG and tool-use prompts | [PDF](./cohere/Prompting%20Command%20R.pdf) |

## xAI (Grok)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Speech-to-speech prompting guide](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech/prompting-guide) | Prompting Grok voice agents | [PDF](./xai/Grok%20Speech-to-Speech%20Prompting%20Guide.pdf) |

xAI has no general text prompting guide right now. See the [docs home](https://docs.x.ai/docs).

## DeepSeek

| Guide | Covers | Offline |
| --- | --- | --- |
| [DeepSeek-R1 usage recommendations](https://github.com/deepseek-ai/DeepSeek-R1#usage-recommendations) | Temperature, no few-shot, math directive, forcing `<think>` | [PDF](./deepseek/DeepSeek-R1%20Usage%20Recommendations.pdf) |
| [Thinking mode guide](https://api-docs.deepseek.com/guides/thinking_mode) | Using thinking mode via API | [PDF](./deepseek/DeepSeek%20Thinking%20Mode%20Guide.pdf) |
| [Prompt library](https://api-docs.deepseek.com/prompt-library/) | Official example prompts by task | — |

## Alibaba (Qwen)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Qwen documentation](https://qwen.readthedocs.io/en/latest/) | Chat templates, thinking mode, function calling | — |

## Moonshot (Kimi)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Best practices for prompts](https://platform.kimi.ai/docs/guide/prompt-best-practice) | Official Kimi prompting guide | [PDF](./moonshot/Kimi%20Prompt%20Best%20Practices.pdf) |

## Amazon (Nova, Bedrock)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Nova 2 prompt engineering guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompt-engineering-guide.html) | Current Nova generation | [PDF](./amazon/Amazon%20Nova%202%20Prompt%20Engineering%20Guide.pdf) |
| [Nova (v1) prompting best practices](https://docs.aws.amazon.com/nova/latest/userguide/prompting.html) | Text, vision, image/video gen, speech | [PDF](./amazon/Amazon%20Nova%20Prompting%20Best%20Practices.pdf) |
| [Bedrock prompt engineering concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html) | Hub linking to each Bedrock model's guide | [PDF](./amazon/Bedrock%20Prompt%20Engineering%20Concepts.pdf) |

## Microsoft (Azure OpenAI)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering) | System messages, few-shot, grounding on Azure OpenAI | [PDF](./microsoft/Azure%20OpenAI%20Prompt%20Engineering%20Techniques.pdf) |

## IBM (Granite)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Granite prompt engineering guide](https://www.ibm.com/granite/docs/use-cases/prompt-engineering) | Prompt templates and techniques for Granite | [PDF](./ibm/Granite%20Prompt%20Engineering%20Guide.pdf) |

## AI21 (Jamba)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt engineering for Jamba](https://docs.ai21.com/docs/prompt-engineering) | Jamba-specific prompting | [PDF](./ai21/Jamba%20Prompt%20Engineering.pdf) |

## Perplexity (Sonar)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt guide](https://docs.perplexity.ai/docs/agent-api/prompt-guide) | Prompting search-grounded models | [PDF](./perplexity/Perplexity%20Prompt%20Guide.pdf) |

## Files in this folder

PDFs are grouped by provider: `anthropic/`, `openai/`, `google/`, `meta/`, `mistral/`, `cohere/`, `xai/`, `deepseek/`, `moonshot/`, `amazon/`, `microsoft/`, `ibm/`, `ai21/`, `perplexity/`.

- Web pages were printed with headless Chrome, and large images were downscaled to keep the folder small.
- The Amazon Nova guides are split across many pages online, so each PDF merges a whole section into one file.
- `openai/GPT-4.1 Prompting Guide.pdf` and `openai/A Practical Guide to Building Agents.pdf` are OpenAI's own PDFs, and `google/Prompt Engineering Whitepaper.pdf` is Google's.
- No PDFs for GitHub repos, docs home pages, or the Gemini for Workspace guide (it is behind a sign-up form).

## Contributing

Add a guide only if the model's provider publishes it. Put the newest model-specific guide first in its provider's table, and drop a PDF snapshot in the provider's folder.
