import json

tools_data = [
    {"name": "ChatGPT", "cat": "Assistants", "cat_class": "cat-ide", "desc": "The industry pioneer by OpenAI. In 2026, it features advanced multi-modal reasoning and seamless integration with personal devices.", "limit": "Free / Plus $20/mo", "link": "https://chatgpt.com"},
    {"name": "Claude", "cat": "Assistants", "cat_class": "cat-ide", "desc": "Anthropic's flagship model known for high emotional intelligence and complex reasoning. Massive context window for deep analysis.", "limit": "Free / Pro $20/mo", "link": "https://claude.ai"},
    {"name": "Gemini", "cat": "Assistants", "cat_class": "cat-ide", "desc": "Google's natively multi-modal agent. Deeply integrated into Workspace with a 1M+ token context window.", "limit": "Free / Advanced $20/mo", "link": "https://gemini.google.com"},
    {"name": "Llama", "cat": "Open Source", "cat_class": "cat-stack", "desc": "Meta's open-weights champion. The backbone of the 2026 local-LLM movement.", "limit": "Free / Open Weights", "link": "https://llama.meta.com"},
    {"name": "DeepSeek-R1", "cat": "Reasoning", "cat_class": "cat-ide", "desc": "The breakout reasoning model of 2026. Competitive performance at a fraction of the cost.", "limit": "Free Chat / Low-cost API", "link": "https://deepseek.com"},
    {"name": "Manus AI", "cat": "General Agent", "cat_class": "cat-special", "desc": "A general-purpose autonomous agent that can navigate the web and execute complex tasks with human-like agency.", "limit": "Subscription / Beta", "link": "https://manus.ai"},
    {"name": "Perplexity Deep Research", "cat": "Research", "cat_class": "cat-research", "desc": "Ultimate research companion. Synthesizes thousands of sources into comprehensive reports.", "limit": "5 Pro Researches / Day", "link": "https://perplexity.ai"},
    {"name": "Genspark", "cat": "AI Search", "cat_class": "cat-research", "desc": "Agentic search engine that creates custom Sparkpages for every query.", "limit": "Free tier available", "link": "https://genspark.ai"},
    {"name": "MultiOn", "cat": "Action Agent", "cat_class": "cat-special", "desc": "An agent that can take actions on your behalf across the web—from booking flights to ordering food.", "limit": "API / Extension", "link": "https://multion.ai"},
    {"name": "Cursor v4", "cat": "Coding IDE", "cat_class": "cat-ide", "desc": "The gold standard for AI coding. Features the Omni-Edit engine for predictive refactoring.", "limit": "Free tier / Pro", "link": "https://cursor.com"},
    {"name": "Windsurf", "cat": "Autonomous Dev", "cat_class": "cat-ide", "desc": "Integrates Devin's autonomous problem-solving directly into the editor for 'Self-Healing' code.", "limit": "Unlimited Flow-mode", "link": "https://codeium.com/windsurf"},
    {"name": "Trae", "cat": "AI IDE", "cat_class": "cat-ide", "desc": "ByteDance's native AI IDE. Offers seamless 'State-Sync' and 'Unlimited Context' tier.", "limit": "Unlimited (Limited Time)", "link": "https://trae.ai"},
    {"name": "Aider", "cat": "CLI Coding", "cat_class": "cat-ide", "desc": "The 2026 CLI King. Highest-ranked agent on coding benchmarks. Perfect for power users.", "limit": "Open Source", "link": "https://aider.chat"},
    {"name": "v0.dev", "cat": "Gen UI", "cat_class": "cat-ui", "desc": "Vercel's Intent Engine. Generates full-stack logic and UI components from sketches.", "limit": "50 Gens / Week", "link": "https://v0.dev"},
    {"name": "Bolt.new", "cat": "Full Stack", "cat_class": "cat-stack", "desc": "Shared Web Containers for agent collaboration. Ship SaaS products in seconds.", "limit": "Unlimited Sandbox", "link": "https://bolt.new"},
    {"name": "Lovable", "cat": "SaaS Builder", "cat_class": "cat-stack", "desc": "SaaS compliance leader. Handles GDPR, auth, and payments via chat.", "limit": "Free staging", "link": "https://lovable.dev"},
    {"name": "Midjourney v8", "cat": "Image Gen", "cat_class": "cat-creative", "desc": "The 2026 gold standard for AI art. Perfect spatial consistency and flawless text.", "limit": "Daily Credits", "link": "https://midjourney.com"},
    {"name": "Flux", "cat": "Image Gen", "cat_class": "cat-creative", "desc": "High-fidelity open-weights image generation. Incredible prompt adherence.", "limit": "Free / API", "link": "https://blackforestlabs.ai"},
    {"name": "Sora v2", "cat": "Video Gen", "cat_class": "cat-creative", "desc": "OpenAI's cinematic engine. Generates up to 2-minute clips with perfect physics.", "limit": "1 Min / Mo", "link": "https://openai.com/sora"},
    {"name": "Luma Dream Machine", "cat": "Video Gen", "cat_class": "cat-creative", "desc": "Efficient video generation with high temporal stability and realism.", "limit": "Free / Subscription", "link": "https://lumalabs.ai"},
    {"name": "Suno v5", "cat": "Audio/Music", "cat_class": "cat-creative", "desc": "Music production with stem separation and 'Vocal-Swap' features.", "limit": "50 Credits / Day", "link": "https://suno.com"},
    {"name": "ElevenLabs", "cat": "Speech/Audio", "cat_class": "cat-creative", "desc": "Global leader in voice synthesis. Features voice cloning and multi-lingual support.", "limit": "Free tier (10k chars)", "link": "https://elevenlabs.io"},
    {"name": "Udio", "cat": "Music Gen", "cat_class": "cat-creative", "desc": "High-fidelity music generation with complex arrangements and vocals.", "limit": "Free / Subscription", "link": "https://udio.com"},
    {"name": "Runway Gen-3", "cat": "Creative Suite", "cat_class": "cat-creative", "desc": "Next generation video-to-video and text-to-video suite.", "limit": "Subscription", "link": "https://runwayml.com"},
    {"name": "Kling AI", "cat": "Video Gen", "cat_class": "cat-creative", "desc": "Video generation known for long-duration clips and high consistency.", "limit": "Free daily credits", "link": "https://klingai.com"},
    {"name": "Notion AI", "cat": "Productivity", "cat_class": "cat-data", "desc": "Turn notes into data. Summarize databases and draft content.", "limit": "Subscription", "link": "https://notion.so"},
    {"name": "Grok-3", "cat": "Assistants", "cat_class": "cat-ide", "desc": "xAI's model with real-time access to global conversations.", "limit": "X Premium+", "link": "https://x.ai"},
    {"name": "Adobe Firefly", "cat": "Design", "cat_class": "cat-creative", "desc": "Ethically trained generative AI integrated into Creative Cloud.", "limit": "Credit-based", "link": "https://adobe.com/firefly"},
    {"name": "Jasper", "cat": "Marketing", "cat_class": "cat-writing", "desc": "Enterprise content engine trained on brand voices.", "limit": "Subscription", "link": "https://jasper.ai"},
    {"name": "Synthesia", "cat": "AI Video", "cat_class": "cat-creative", "desc": "AI avatars in 120+ languages for training and presentations.", "limit": "Subscription", "link": "https://synthesia.io"},
    {"name": "Descript", "cat": "Audio/Video", "cat_class": "cat-data", "desc": "Edit audio and video by editing text. Features 'Underlord' automation.", "limit": "Free / Subscription", "link": "https://descript.com"},
    {"name": "Grammarly", "cat": "Writing", "cat_class": "cat-writing", "desc": "AI assistant for stylistic shifts and structural changes.", "limit": "Free / Premium", "link": "https://grammarly.com"},
    {"name": "Otter.ai", "cat": "Transcription", "cat_class": "cat-data", "desc": "Meeting assistant that records, transcribes, and summarizes.", "limit": "Free / Pro", "link": "https://otter.ai"},
    {"name": "Character.ai", "cat": "Conversational", "cat_class": "cat-special", "desc": "Leader in roleplay and persona-based AI voice chat.", "limit": "Free / Plus", "link": "https://character.ai"},
    {"name": "GitHub Copilot", "cat": "Coding", "cat_class": "cat-ide", "desc": "Most widely used AI pair programmer. VS Code integrated.", "limit": "$10/mo Individuals", "link": "https://github.com/features/copilot"},
    {"name": "Replit", "cat": "Cloud Dev", "cat_class": "cat-stack", "desc": "Collaborative coding environment with a powerful agent.", "limit": "Free / Core $15/mo", "link": "https://replit.com"},
    {"name": "Tabnine", "cat": "Coding", "cat_class": "cat-ide", "desc": "Privacy-first assistant that can be run entirely locally.", "limit": "Free / Pro", "link": "https://tabnine.com"},
    {"name": "Continue.dev", "cat": "Coding Framework", "cat_class": "cat-stack", "desc": "Bridge for coding agents. Bring your own models to any IDE.", "limit": "100% Free", "link": "https://continue.dev"},
    {"name": "Zed AI", "cat": "High Perf Editor", "cat_class": "cat-ide", "desc": "Fast Rust-built editor with native low-latency AI.", "limit": "Free / OSS", "link": "https://zed.dev"},
    {"name": "Supermaven", "cat": "Fast Context", "cat_class": "cat-stack", "desc": "Fastest autocomplete with a 1M+ token context window.", "limit": "Free / Pro", "link": "https://supermaven.com"},
    {"name": "Plandex", "cat": "Complex Tasks", "cat_class": "cat-ide", "desc": "AI coding engine for long-running, multi-file tasks.", "limit": "Free / Pro", "link": "https://plandex.ai"},
    {"name": "Melty", "cat": "Open Source IDE", "cat_class": "cat-ide", "desc": "First open-source AI IDE that learns your coding style.", "limit": "Free / OSS", "link": "https://melty.builtwithdark.com"},
    {"name": "Void Editor", "cat": "Privacy IDE", "cat_class": "cat-ide", "desc": "VS Code alternative focused on privacy and local models.", "limit": "Free / OSS", "link": "https://voideditor.com"},
    {"name": "Julius AI", "cat": "Data Scientist", "cat_class": "cat-data", "desc": "AI agent for advanced data analysis and visualization.", "limit": "15 Messages / Mo", "link": "https://julius.ai"},
    {"name": "Snyk AI", "cat": "Security", "cat_class": "cat-sec", "desc": "Finds and fixes security vulnerabilities automatically.", "limit": "Free for OSS", "link": "https://snyk.io"},
    {"name": "Mistral", "cat": "Open Source", "cat_class": "cat-stack", "desc": "European champion of open-weights models like Large and Pixtral.", "limit": "Open Weights", "link": "https://mistral.ai"},
    {"name": "Stable Diffusion", "cat": "Image Gen", "cat_class": "cat-creative", "desc": "The open-weights king for local image generation.", "limit": "100% Free (Local)", "link": "https://stability.ai"},
    {"name": "Whisper", "cat": "Audio/STT", "cat_class": "cat-data", "desc": "Industry-standard speech-to-text model by OpenAI.", "limit": "Open Source", "link": "https://openai.com/research/whisper"},
    {"name": "Poe", "cat": "Aggregator", "cat_class": "cat-special", "desc": "Platform bringing every major LLM into one interface.", "limit": "Free / Sub", "link": "https://poe.com"},
    {"name": "Pi", "cat": "Personal AI", "cat_class": "cat-special", "desc": "Companion AI designed for high-quality, empathetic conversation.", "limit": "Free Access", "link": "https://pi.ai"},
    {"name": "Phind", "cat": "Dev Search", "cat_class": "cat-research", "desc": "Search engine for developers. Connects codebase to web.", "limit": "Free / Pro", "link": "https://phind.com"},
    {"name": "Skyvern", "cat": "Browser Agent", "cat_class": "cat-special", "desc": "Open-source browser automation agent using LLMs.", "limit": "Open Source", "link": "https://skyvern.com"},
    {"name": "E2B", "cat": "Agent Infra", "cat_class": "cat-devops", "desc": "Secure, sandboxed cloud environments for AI agents.", "limit": "Generous Free Tier", "link": "https://e2b.dev"},
    {"name": "Pulumi AI", "cat": "Infrastructure", "cat_class": "cat-devops", "desc": "Generate cloud infrastructure code using natural language.", "limit": "Free Personal", "link": "https://pulumi.com"}
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

cards_html = "\n".join([generate_card(t) for t in tools_data])

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Tools Resource | AI Frontier 2026</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;600;800&family=Space+Mono&family=Syncopate:wght@700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #050505;
            --card-bg: rgba(255, 255, 255, 0.03);
            --accent-cyan: #00f2ff;
            --accent-magenta: #ff00ff;
            --accent-lime: #ccff00;
            --text-main: #f8fafc;
            --text-dim: #94a3b8;
            --glass-border: rgba(255, 255, 255, 0.1);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            cursor: crosshair;
        }}

        body {{
            background-color: var(--bg);
            color: var(--text-main);
            font-family: 'Outfit', sans-serif;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 20% 30%, rgba(0, 242, 255, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(255, 0, 255, 0.05) 0%, transparent 50%);
        }}

        .grid-overlay {{
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: 
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 40px 40px;
            z-index: -1;
            transform: perspective(500px) rotateX(60deg) translateY(-100px);
            animation: gridMove 20s linear infinite;
        }}

        @keyframes gridMove {{
            0% {{ background-position: 0 0; }}
            100% {{ background-position: 0 1000px; }}
        }}

        header {{
            padding: 40px 10%;
            border-bottom: 1px solid var(--glass-border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(5,5,5,0.8);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .logo {{
            font-family: 'Syncopate', sans-serif;
            font-weight: 700;
            color: #fff;
            text-decoration: none;
            font-size: 1.2rem;
        }}

        .logo span {{ color: var(--accent-cyan); }}

        .back-link {{
            font-family: 'Space Mono', monospace;
            color: var(--text-dim);
            text-decoration: none;
            font-size: 0.8rem;
            border: 1px solid var(--glass-border);
            padding: 8px 16px;
            border-radius: 4px;
            transition: 0.3s;
        }}

        .back-link:hover {{
            border-color: var(--accent-cyan);
            color: var(--accent-cyan);
        }}

        .container {{
            padding: 60px 10%;
        }}

        .page-title {{
            font-family: 'Syncopate', sans-serif;
            font-size: clamp(2rem, 5vw, 4rem);
            margin-bottom: 20px;
            text-transform: uppercase;
            background: linear-gradient(to right, #fff, var(--accent-lime));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .page-subtitle {{
            color: var(--text-dim);
            max-width: 600px;
            margin-bottom: 60px;
            font-size: 1.1rem;
            line-height: 1.6;
        }}

        .tools-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
        }}

        .tool-card {{
            background: var(--card-bg);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 30px;
            transition: 0.3s;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        .tool-card:hover {{
            transform: translateY(-5px);
            border-color: var(--accent-lime);
            box-shadow: 0 10px 30px rgba(204, 255, 0, 0.1);
        }}

        .tool-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 20px;
        }}

        .tool-name {{
            font-family: 'Space Mono', monospace;
            font-size: 1.4rem;
            font-weight: 700;
            color: #fff;
        }}

        .tool-cat {{
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 4px 8px;
            border-radius: 4px;
            background: rgba(255,255,255,0.05);
            color: var(--text-dim);
        }}

        .tool-desc {{
            color: var(--text-dim);
            font-size: 0.9rem;
            line-height: 1.6;
            margin-bottom: 25px;
            flex-grow: 1;
        }}

        .limit-box {{
            background: rgba(0, 0, 0, 0.3);
            border-left: 2px solid var(--accent-lime);
            padding: 12px;
            margin-bottom: 25px;
        }}

        .limit-label {{
            font-size: 0.7rem;
            color: var(--accent-lime);
            text-transform: uppercase;
            margin-bottom: 4px;
            display: block;
            font-family: 'Space Mono', monospace;
        }}

        .limit-val {{
            font-size: 0.9rem;
            color: #fff;
        }}

        .tool-link {{
            text-decoration: none;
            text-align: center;
            padding: 12px;
            border: 1px solid var(--glass-border);
            color: #fff;
            font-family: 'Space Mono', monospace;
            text-transform: uppercase;
            font-size: 0.8rem;
            border-radius: 4px;
            transition: 0.3s;
        }}

        .tool-link:hover {{
            background: var(--accent-lime);
            color: #000;
            border-color: var(--accent-lime);
        }}

        /* Category colors */
        .cat-ide {{ color: var(--accent-cyan); border: 1px solid rgba(0, 242, 255, 0.3); }}
        .cat-ui {{ color: var(--accent-magenta); border: 1px solid rgba(255, 0, 255, 0.3); }}
        .cat-stack {{ color: var(--accent-lime); border: 1px solid rgba(204, 255, 0, 0.3); }}
        .cat-research {{ color: #a5f3fc; border: 1px solid rgba(165, 243, 252, 0.3); }}
        .cat-writing {{ color: #e9d5ff; border: 1px solid rgba(233, 213, 255, 0.3); }}
        .cat-creative {{ color: #f472b6; border: 1px solid rgba(244, 114, 182, 0.3); }}
        .cat-data {{ color: #6ee7b7; border: 1px solid rgba(110, 231, 183, 0.3); }}
        .cat-devops {{ color: #fdba74; border: 1px solid rgba(253, 186, 116, 0.3); }}
        .cat-sec {{ color: #f87171; border: 1px solid rgba(248, 113, 113, 0.3); }}
        .cat-special {{ color: #fde047; border: 1px solid rgba(253, 224, 71, 0.3); }}

    </style>
</head>
<body>
    <div class="grid-overlay"></div>

    <header>
        <a href="index.html" class="logo">AI FRONTIER <span>2026</span></a>
        <a href="index.html" class="back-link">// RETURN TO FEED</a>
    </header>

    <div class="container">
        <h1 class="page-title">The Vibe Coder's<br>Toolkit</h1>
        <p class="page-subtitle">
            A curated index of high-value autonomous agents and coding environments. 
            Filtered for generous free tiers to democratize the 2026 developer stack.
        </p>

        <div class="tools-grid">
{cards_html}
        </div>
    </div>
</body>
</html>"""

with open('repos/ai-frontier-2026/tools.html', 'w') as f:
    f.write(html_template)

print(f"Updated tools.html with {len(tools_data)} tools.")
