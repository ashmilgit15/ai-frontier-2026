import json

tools_data = [
    {
        "name": "ChatGPT",
        "cat": "Assistants",
        "cat_class": "cat-ide",
        "desc": "The industry pioneer by OpenAI. In 2026, it features advanced multi-modal reasoning and seamless integration with personal devices via the 'Omni' engine.",
        "limit": "Free tier available / Plus $20/mo",
        "link": "https://chatgpt.com"
    },
    {
        "name": "Claude",
        "cat": "Assistants",
        "cat_class": "cat-ide",
        "desc": "Anthropic's flagship model known for high emotional intelligence and complex reasoning. Features a massive 200k+ context window for deep document analysis.",
        "limit": "Free tier / Pro $20/mo",
        "link": "https://claude.ai"
    },
    {
        "name": "Gemini",
        "cat": "Assistants",
        "cat_class": "cat-ide",
        "desc": "Google's natively multi-modal agent. Deeply integrated into the Google Workspace ecosystem with a staggering 1M+ token context window in the Ultra version.",
        "limit": "Free / Advanced $20/mo",
        "link": "https://gemini.google.com"
    },
    {
        "name": "Llama",
        "cat": "Open Source",
        "cat_class": "cat-stack",
        "desc": "Meta's open-weights champion. The backbone of the 2026 local-LLM movement, allowing for high-performance intelligence on consumer hardware.",
        "limit": "Free / Open Weights",
        "link": "https://llama.meta.com"
    },
    {
        "name": "DeepSeek-R1",
        "cat": "Reasoning",
        "cat_class": "cat-ide",
        "desc": "The breakout reasoning model of 2026. Features competitive performance with top-tier models at a fraction of the inference cost, powering a new wave of efficient agents.",
        "limit": "Free Chat / Low-cost API",
        "link": "https://deepseek.com"
    },
    {
        "name": "Manus AI",
        "cat": "General Agent",
        "cat_class": "cat-special",
        "desc": "A general-purpose autonomous agent that can navigate the web, manage files, and execute complex tasks across multiple platforms with human-like agency.",
        "limit": "Subscription / Beta Access",
        "link": "https://manus.ai"
    },
    {
        "name": "Perplexity Deep Research",
        "cat": "Research",
        "cat_class": "cat-research",
        "desc": "The ultimate research companion. Synthesizes thousands of real-time sources into comprehensive, cited reports with autonomous deep-dive capabilities.",
        "limit": "5 Pro Researches / Day",
        "link": "https://perplexity.ai"
    },
    {
        "name": "Cursor v4",
        "cat": "Coding IDE",
        "cat_class": "cat-ide",
        "desc": "The gold standard for AI coding. Features the Omni-Edit engine, which predicts entire architectural refactors before you even finish your prompt.",
        "limit": "5000 completions/mo + Community Cloud",
        "link": "https://cursor.com"
    },
    {
        "name": "Windsurf",
        "cat": "Autonomous Dev",
        "cat_class": "cat-ide",
        "desc": "Integrates Devin's autonomous problem-solving directly into the editor for 'Self-Healing' production code and complex implementation planning.",
        "limit": "Unlimited Flow-mode for Hobbyists",
        "link": "https://codeium.com/windsurf"
    },
    {
        "name": "Trae",
        "cat": "AI IDE",
        "cat_class": "cat-ide",
        "desc": "ByteDance's native AI IDE. Offers seamless 'State-Sync' between mobile and desktop coding environments with an 'Unlimited Context' tier.",
        "limit": "Unlimited Reasoning (Limited Time)",
        "link": "https://trae.ai"
    },
    {
        "name": "Aider",
        "cat": "CLI Coding",
        "cat_class": "cat-ide",
        "desc": "The 2026 CLI King. Remains the highest-ranked agent on coding benchmarks. Perfect for terminal-based power users who want speed over GUI bloat.",
        "limit": "Open Source / Local-LLM Friendly",
        "link": "https://aider.chat"
    },
    {
        "name": "v0.dev",
        "cat": "Gen UI",
        "cat_class": "cat-ui",
        "desc": "Vercel's Intent Engine. Generates full-stack logic and high-fidelity UI components based on sketches and natural language descriptions.",
        "limit": "50 Generations/Week (High Fidelity)",
        "link": "https://v0.dev"
    },
    {
        "name": "Bolt.new",
        "cat": "Full Stack",
        "cat_class": "cat-stack",
        "desc": "Pioneer of Shared Web Containers. Allows multiple agents to collaborate in a single browser-based environment to ship SaaS products in seconds.",
        "limit": "Unlimited Sandbox Deploys",
        "link": "https://bolt.new"
    },
    {
        "name": "Lovable",
        "cat": "SaaS Builder",
        "cat_class": "cat-stack",
        "desc": "Leader in SaaS compliance. Automatically handles GDPR, user auth, and payment gateways through a simple chat interface.",
        "limit": "Free staging for 1 Project",
        "link": "https://lovable.dev"
    },
    {
        "name": "Midjourney v8",
        "cat": "Image Gen",
        "cat_class": "cat-creative",
        "desc": "The 2026 gold standard for AI art. Features perfect spatial consistency, flawless text rendering, and advanced style-matching capabilities.",
        "limit": "Daily Community Vote Credits",
        "link": "https://midjourney.com"
    },
    {
        "name": "Flux",
        "cat": "Image Gen",
        "cat_class": "cat-creative",
        "desc": "High-fidelity open-weights image generation by Black Forest Labs. Known for incredible prompt adherence and realistic human features.",
        "limit": "Free (Schnell) / API (Pro)",
        "link": "https://blackforestlabs.ai"
    },
    {
        "name": "Sora v2",
        "cat": "Video Gen",
        "cat_class": "cat-creative",
        "desc": "OpenAI's cinematic engine. Generates up to 2-minute clips with perfect physics and temporal consistency for short film production.",
        "limit": "1 Minute High-Res / Mo",
        "link": "https://openai.com/sora"
    },
    {
        "name": "Luma Dream Machine",
        "cat": "Video Gen",
        "cat_class": "cat-creative",
        "desc": "Highly efficient video generation model capable of creating realistic and imaginative scenes with high temporal stability.",
        "limit": "Free / Subscription tiers",
        "link": "https://lumalabs.ai"
    },
    {
        "name": "Suno v5",
        "cat": "Audio/Music",
        "cat_class": "cat-creative",
        "desc": "Revolutionizing music production with studio-quality tracks, full stem separation, and professional-grade audio engineering features.",
        "limit": "50 Credits / Day (Renewable)",
        "link": "https://suno.com"
    },
    {
        "name": "ElevenLabs",
        "cat": "Speech/Audio",
        "cat_class": "cat-creative",
        "desc": "The global leader in AI voice synthesis. Features low-latency speech generation, voice cloning, and multi-lingual support.",
        "limit": "Free tier (10k chars) / Sub",
        "link": "https://elevenlabs.io"
    },
    {
        "name": "Udio",
        "cat": "Music Gen",
        "cat_class": "cat-creative",
        "desc": "A powerhouse for high-fidelity music generation, allowing users to create full tracks with complex arrangements and vocals.",
        "limit": "Free / Subscription",
        "link": "https://udio.com"
    },
    {
        "name": "Runway Gen-3",
        "cat": "Creative Suite",
        "cat_class": "cat-creative",
        "desc": "The next generation of video-to-video and text-to-video tools. Essential for the 2026 digital artist's workflow.",
        "limit": "Subscription based",
        "link": "https://runwayml.com"
    },
    {
        "name": "Kling AI",
        "cat": "Video Gen",
        "cat_class": "cat-creative",
        "desc": "A cutting-edge video generation model known for long-duration clips and high consistency across complex movement patterns.",
        "limit": "Free daily credits",
        "link": "https://klingai.com"
    },
    {
        "name": "Notion AI",
        "cat": "Productivity",
        "cat_class": "cat-data",
        "desc": "Turn notes into actionable data. Notion AI can summarize databases, draft content, and act as a local knowledge graph for your team.",
        "limit": "Add-on for Notion users",
        "link": "https://notion.so"
    },
    {
        "name": "Grok-3",
        "cat": "Assistants",
        "cat_class": "cat-ide",
        "desc": "xAI's model with real-time access to the global conversation. Optimized for rapid information retrieval and bold, un-filtered reasoning.",
        "limit": "X Premium+ Subscribers",
        "link": "https://x.ai"
    },
    {
        "name": "Perplexity",
        "cat": "AI Search",
        "cat_class": "cat-research",
        "desc": "The search engine of the agentic era. Provides direct answers with citations, replacing the need for traditional blue-link browsing.",
        "limit": "Free / Pro subscription",
        "link": "https://perplexity.ai"
    },
    {
        "name": "Adobe Firefly",
        "cat": "Design",
        "cat_class": "cat-creative",
        "desc": "Ethically trained generative AI for designers. Integrated into Photoshop and Illustrator for seamless generative fill and vector creation.",
        "limit": "Credit-based / Creative Cloud",
        "link": "https://adobe.com/firefly"
    },
    {
        "name": "Jasper",
        "cat": "Marketing",
        "cat_class": "cat-writing",
        "desc": "The enterprise content engine. Trained on brand voices to generate consistent marketing copy across all digital channels.",
        "limit": "Subscription based",
        "link": "https://jasper.ai"
    },
    {
        "name": "Synthesia",
        "cat": "AI Video",
        "cat_class": "cat-creative",
        "desc": "The leader in AI avatars. Generate training videos and presentations with hyper-realistic digital humans in over 120 languages.",
        "limit": "Subscription based",
        "link": "https://synthesia.io"
    },
    {
        "name": "Descript",
        "cat": "Audio/Video",
        "cat_class": "cat-data",
        "desc": "Edit audio and video by editing text. Features 'Underlord' - an AI assistant that automates the tedious parts of the editing process.",
        "limit": "Free tier / Subscription",
        "link": "https://descript.com"
    },
    {
        "name": "Grammarly",
        "cat": "Writing",
        "cat_class": "cat-writing",
        "desc": "The writing assistant that goes beyond grammar. In 2026, it suggests stylistic shifts and structural changes based on the intended audience.",
        "limit": "Free / Premium / Business",
        "link": "https://grammarly.com"
    },
    {
        "name": "Otter.ai",
        "cat": "Transcription",
        "cat_class": "cat-data",
        "desc": "The meeting assistant that never sleeps. Automatically records, transcribes, and summarizes meetings with real-time action item tracking.",
        "limit": "Free / Pro / Business",
        "link": "https://otter.ai"
    },
    {
        "name": "Character.ai",
        "cat": "Conversational",
        "cat_class": "cat-special",
        "desc": "The leader in roleplay and persona-based AI. Features ultra-low latency voice chat and highly customizable digital personalities.",
        "limit": "Free / c.ai+ subscription",
        "link": "https://character.ai"
    },
    {
        "name": "GitHub Copilot",
        "cat": "Coding",
        "cat_class": "cat-ide",
        "desc": "The most widely used AI pair programmer. Deeply integrated into VS Code with support for multi-file editing and automated testing.",
        "limit": "$10/mo Individuals",
        "link": "https://github.com/features/copilot"
    },
    {
        "name": "Replit",
        "cat": "Cloud Dev",
        "cat_class": "cat-stack",
        "desc": "A complete collaborative coding environment in the browser with a powerful agent that can build and deploy apps autonomously.",
        "limit": "Free tier / Core $15/mo",
        "link": "https://replit.com"
    },
    {
        "name": "Tabnine",
        "cat": "Coding",
        "cat_class": "cat-ide",
        "desc": "The privacy-first AI coding assistant. Can be run entirely locally or in a private cloud to ensure zero data leakage.",
        "limit": "Free / Pro / Enterprise",
        "link": "https://tabnine.com"
    },
    {
        "name": "Continue.dev",
        "cat": "Coding Framework",
        "cat_class": "cat-stack",
        "desc": "Open-source bridge for coding agents. Allows you to bring your own models (local or API) into your existing IDE workflow.",
        "limit": "100% Free / OSS",
        "link": "https://continue.dev"
    },
    {
        "name": "Zed AI",
        "cat": "High Perf Editor",
        "cat_class": "cat-ide",
        "desc": "A lightning-fast, collaborative code editor built in Rust with native AI features designed for low-latency implementations.",
        "limit": "Free / OSS",
        "link": "https://zed.dev"
    },
    {
        "name": "Supermaven",
        "cat": "Fast Context",
        "cat_class": "cat-stack",
        "desc": "Known for the fastest autocomplete and a massive 1M+ token context window, allowing it to reason across entire codebases.",
        "limit": "Free tier / Pro sub",
        "link": "https://supermaven.com"
    },
    {
        "name": "Plandex",
        "cat": "Complex Tasks",
        "cat_class": "cat-ide",
        "desc": "Terminal-based AI coding engine for long-running, multi-file tasks. Focuses on planning and architectural integrity.",
        "limit": "Free / Pro tiers",
        "link": "https://plandex.ai"
    },
    {
        "name": "Melty",
        "cat": "Open Source IDE",
        "cat_class": "cat-ide",
        "desc": "The first open-source AI IDE that learns your coding style and provides hyper-personalized assistance based on your local history.",
        "limit": "Free / OSS",
        "link": "https://melty.builtwithdark.com"
    },
    {
        "name": "Void Editor",
        "cat": "Privacy IDE",
        "cat_class": "cat-ide",
        "desc": "A VS Code alternative focused on privacy. Runs local models for completions and agents without any cloud dependency.",
        "limit": "Free / OSS",
        "link": "https://voideditor.com"
    },
    {
        "name": "Julius AI",
        "cat": "Data Scientist",
        "cat_class": "cat-data",
        "desc": "An AI agent for advanced data analysis. Can clean data, perform complex statistical tests, and generate publication-quality charts.",
        "limit": "15 Messages / Month (Free)",
        "link": "https://julius.ai"
    },
    {
        "name": "Snyk AI",
        "cat": "Security",
        "cat_class": "cat-sec",
        "desc": "Automatically finds and fixes security vulnerabilities in your code and dependencies using a developer-friendly agentic workflow.",
        "limit": "Free for OSS",
        "link": "https://snyk.io"
    },
    {
        "name": "Mistral",
        "cat": "Open Source",
        "cat_class": "cat-stack",
        "desc": "The European champion of open-weights. Mistral Large and Pixtral models are renowned for their efficiency and power, rivaling the best proprietary systems.",
        "limit": "Usage-based / Open Weights",
        "link": "https://mistral.ai"
    },
    {
        "name": "Stable Diffusion",
        "cat": "Image Gen",
        "cat_class": "cat-creative",
        "desc": "The open-weights king by Stability AI. Powers thousands of local and hosted image generators with unparalleled customizability via LoRAs and ControlNet.",
        "limit": "100% Free (Local) / DreamStudio",
        "link": "https://stability.ai"
    },
    {
        "name": "Whisper",
        "cat": "Audio/STT",
        "cat_class": "cat-data",
        "desc": "OpenAI's industry-standard speech-to-text model. Highly accurate translation and transcription across dozens of languages. Essential for audio agents.",
        "limit": "Open Source / API",
        "link": "https://openai.com/research/whisper"
    },
    {
        "name": "Poe",
        "cat": "Aggregator",
        "cat_class": "cat-special",
        "desc": "Quora's platform that brings every major LLM into one interface. Allows for the creation of custom prompt-bots and easy comparison of model outputs.",
        "limit": "Free tier / Subscription",
        "link": "https://poe.com"
    },
    {
        "name": "Pi",
        "cat": "Personal AI",
        "cat_class": "cat-special",
        "desc": "The companion AI by Inflection. Designed for high-quality, empathetic conversation and personalized assistance with a unique focus on 'emotional IQ'.",
        "limit": "Free Access",
        "link": "https://pi.ai"
    },
    {
        "name": "Genspark",
        "cat": "AI Search",
        "cat_class": "cat-research",
        "desc": "An 'Agentic Search Engine' that creates custom, dynamically updated Sparkpages for every query, aggregating the web into a coherent structure.",
        "limit": "Free tier available",
        "link": "https://genspark.ai"
    },
    {
        "name": "Phind",
        "cat": "Developer Search",
        "cat_class": "cat-research",
        "desc": "The search engine for developers. Connects your codebase to the web to solve complex technical problems with cited documentation and code examples.",
        "limit": "Free daily uses / Pro sub",
        "link": "https://phind.com"
    },
    {
        "name": "Skyvern",
        "cat": "Browser Agent",
        "cat_class": "cat-special",
        "desc": "An open-source browser automation agent that uses LLMs to navigate complex websites and execute workflows without brittle CSS selectors.",
        "limit": "Open Source / Hosted Cloud",
        "link": "https://skyvern.com"
    },
    {
        "name": "MultiOn",
        "cat": "Action Agent",
        "cat_class": "cat-special",
        "desc": "An agent that can take actions on your behalf across the web—from booking flights to ordering food. The leading edge of the LAM (Large Action Model) space.",
        "limit": "API / Browser Extension",
        "link": "https://multion.ai"
    },
    {
        "name": "E2B",
        "cat": "Agent Infrastructure",
        "cat_class": "cat-devops",
        "desc": "Provides secure, sandboxed cloud environments for AI agents. Essential for any application that lets an agent write and execute code in the cloud.",
        "limit": "Generous Free Tier / Usage",
        "link": "https://e2b.dev"
    },
    {
        "name": "Pulumi AI",
        "cat": "Infrastructure",
        "cat_class": "cat-devops",
        "desc": "Describe your cloud architecture in natural language and Pulumi AI generates the required Infrastructure as Code (IaC) in your language of choice.",
        "limit": "Free Personal tier",
        "link": "https://pulumi.com"
    }
]

def generate_card(tool):
    return f"""
            <div class="tool-card">
                <div class="tool-header">
                    <div class="tool-name">{tool['name']}</div>
                    <div class="tool-cat {tool['cat_class']}">{tool['cat']}</div>
                </div>
                <p class="tool-desc">
                    {tool['desc']}
                </p>
                <div class="limit-box">
                    <span class="limit-label">Status / Limits</span>
                    <span class="limit-val">{tool['limit']}</span>
                </div>
                <a href="{tool['link']}" target="_blank" class="tool-link">Access {tool['name']}</a>
            </div>"""

cards_html = "\\n".join([generate_card(t) for t in tools_data])

with open('repos/ai-frontier-2026/tools.html', 'r') as f:
    html = f.read()

# Replace the grid content
# Find the tools-grid div and everything inside it until the closing tag
import re
pattern = re.compile(r'(<div class="tools-grid">)(.*?)(</div>\\s*</div>\\s*</body>)', re.DOTALL | re.IGNORECASE)

new_html = pattern.sub(rf'\\1{cards_html}\\n            \\3', html)

with open('repos/ai-frontier-2026/tools.html', 'w') as f:
    f.write(new_html)

print(f"Updated tools.html with {len(tools_data)} tools.")
