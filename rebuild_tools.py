import json

tools_data = [
    # --- ASSISTANTS & GENERAL LLMS (1-10) ---
    {"name": "ChatGPT", "cat": "Assistants", "cat_class": "cat-ide", "desc": "OpenAI's flagship assistant. Multi-modal, web-connected, and capable of complex reasoning.", "limit": "Free / Plus $20/mo", "link": "https://chatgpt.com"},
    {"name": "Claude", "cat": "Assistants", "cat_class": "cat-ide", "desc": "Anthropic's model known for high quality writing and nuanced reasoning. Large context window.", "limit": "Free / Pro $20/mo", "link": "https://claude.ai"},
    {"name": "Gemini", "cat": "Assistants", "cat_class": "cat-ide", "desc": "Google's natively multi-modal AI. Integrated into Workspace with a 1M+ token window.", "limit": "Free / Advanced $20/mo", "link": "https://gemini.google.com"},
    {"name": "Pi", "cat": "Personal AI", "cat_class": "cat-special", "desc": "Empathetic companion AI by Inflection. Focused on high-quality conversation and EQ.", "limit": "Free Access", "link": "https://pi.ai"},
    {"name": "Grok-3", "cat": "Assistants", "cat_class": "cat-ide", "desc": "xAI's model with real-time X data access and bold, un-filtered reasoning.", "limit": "X Premium+", "link": "https://x.ai"},
    {"name": "DeepSeek-R1", "cat": "Reasoning", "cat_class": "cat-ide", "desc": "Powerful open-weights reasoning model with high-tier performance at low cost.", "limit": "Free Chat / API", "link": "https://deepseek.com"},
    {"name": "Mistral Large", "cat": "Open Source", "cat_class": "cat-stack", "desc": "Mistral AI's flagship model. European powerhouse for efficiency and reasoning.", "limit": "Usage-based", "link": "https://mistral.ai"},
    {"name": "Llama 3.1", "cat": "Open Source", "cat_class": "cat-stack", "desc": "Meta's highly capable open-weights models powering the local-LLM ecosystem.", "limit": "Free / Open Weights", "link": "https://llama.meta.com"},
    {"name": "Gemma 2", "cat": "Open Source", "cat_class": "cat-stack", "desc": "Google's lightweight open-model family built for efficiency and research.", "limit": "Free / Open Weights", "link": "https://ai.google.dev/gemma"},
    {"name": "Falcon 2", "cat": "Open Source", "cat_class": "cat-stack", "desc": "TII's high-performance open-source model suite from the UAE.", "limit": "Free / Open Weights", "link": "https://falconllm.tii.ae"},

    # --- DEVELOPMENT & CODING (11-30) ---
    {"name": "Cursor v4", "cat": "Coding IDE", "cat_class": "cat-ide", "desc": "The ultimate AI IDE. Omni-Edit predicts entire architectural refactors.", "limit": "Free tier / Pro", "link": "https://cursor.com"},
    {"name": "Windsurf", "cat": "Autonomous Dev", "cat_class": "cat-ide", "desc": "Integrates Devin's autonomous planning directly into the editor for self-healing code.", "limit": "Unlimited Flow-mode", "link": "https://codeium.com/windsurf"},
    {"name": "Trae", "cat": "AI IDE", "cat_class": "cat-ide", "desc": "ByteDance's AI IDE with state-sync and unlimited reasoning for developers.", "limit": "Unlimited (Limited Time)", "link": "https://trae.ai"},
    {"name": "Aider", "cat": "CLI Coding", "cat_class": "cat-ide", "desc": "CLI champion for rapid multi-file editing and autonomous coding workflows.", "limit": "Open Source", "link": "https://aider.chat"},
    {"name": "GitHub Copilot", "cat": "Coding Assistant", "cat_class": "cat-ide", "desc": "The standard in AI pair programming, deeply integrated into VS Code and JetBrains.", "limit": "$10/mo Individuals", "link": "https://github.com/features/copilot"},
    {"name": "Zed AI", "cat": "High Perf Editor", "cat_class": "cat-ide", "desc": "Rust-built editor with neural-sync for a zero-latency AI experience.", "limit": "Free / OSS", "link": "https://zed.dev"},
    {"name": "Codeium", "cat": "Coding Assistant", "cat_class": "cat-ide", "desc": "Free-for-individuals alternative to Copilot with strong context awareness.", "limit": "Free for Individuals", "link": "https://codeium.com"},
    {"name": "Tabnine", "cat": "Coding Assistant", "cat_class": "cat-ide", "desc": "Privacy-first coding assistant that can run entirely on-prem or local.", "limit": "Free / Pro", "link": "https://tabnine.com"},
    {"name": "Continue.dev", "cat": "Dev Bridge", "cat_class": "cat-stack", "desc": "Open-source library to plug any model into your IDE's agentic loop.", "limit": "100% Free / OSS", "link": "https://continue.dev"},
    {"name": "Melty", "cat": "Open Source IDE", "cat_class": "cat-ide", "desc": "An IDE that learns your style and Frustration levels to provide better help.", "limit": "Free / OSS", "link": "https://melty.builtwithdark.com"},
    {"name": "Void Editor", "cat": "Privacy IDE", "cat_class": "cat-ide", "desc": "VS Code fork built for Local-LLM integration without data telemetry.", "limit": "Free / OSS", "link": "https://voideditor.com"},
    {"name": "Plandex", "cat": "Task Agent", "cat_class": "cat-ide", "desc": "CLI tool for long-running, multi-file tasks with automated planning.", "limit": "Free / Pro", "link": "https://plandex.ai"},
    {"name": "Mintlify", "cat": "Documentation", "cat_class": "cat-ui", "desc": "AI-powered platform to build beautiful, automated technical documentation.", "limit": "Free tier / Pro", "link": "https://mintlify.com"},
    {"name": "OpenHands", "cat": "OSS Agent", "cat_class": "cat-ide", "desc": "Autonomous open-source agent capable of full project implementations.", "limit": "Free / OSS", "link": "https://github.com/All-Hands-AI/OpenHands"},
    {"name": "Cody (Sourcegraph)", "cat": "Coding AI", "cat_class": "cat-ide", "desc": "Codebase-aware agent by Sourcegraph for searching and fixing large repos.", "limit": "Free tier available", "link": "https://sourcegraph.com/cody"},
    {"name": "Mutable.ai", "cat": "Software Engineering", "cat_class": "cat-ide", "desc": "Accelerates software development with high-quality AI-generated code and docs.", "limit": "Free tier available", "link": "https://mutable.ai"},
    {"name": "Amazon CodeWhisperer", "cat": "Coding Assistant", "cat_class": "cat-ide", "desc": "AWS-optimized AI coding assistant for secure, high-quality development.", "limit": "Free for Individuals", "link": "https://aws.amazon.com/codewhisperer"},
    {"name": "Replit Agent", "cat": "Cloud Agent", "cat_class": "cat-stack", "desc": "Build and deploy full-stack apps entirely through a natural language chat.", "limit": "Core Subscription", "link": "https://replit.com/ai"},
    {"name": "Fig (Postman)", "cat": "CLI Tools", "cat_class": "cat-ide", "desc": "Adds visual autocomplete and AI command generation to your terminal.", "limit": "Free for Individuals", "link": "https://fig.io"},
    {"name": "Blackbox AI", "cat": "Coding Search", "cat_class": "cat-ide", "desc": "In-editor AI for searching code snippets and generating functions instantly.", "limit": "Free tier available", "link": "https://useblackbox.io"},

    # --- IMAGE GENERATION (31-50) ---
    {"name": "Midjourney v8", "cat": "Image Gen", "cat_class": "cat-creative", "desc": "The 2026 standard for high-fidelity AI art and stylistic consistency.", "limit": "Subscription based", "link": "https://midjourney.com"},
    {"name": "DALL-E 3", "cat": "Image Gen", "cat_class": "cat-creative", "desc": "OpenAI's image engine. Known for perfect prompt adherence and easy ChatGPT use.", "limit": "Included in Plus", "link": "https://openai.com/dall-e-3"},
    {"name": "Flux.1", "cat": "Image Gen", "cat_class": "cat-creative", "desc": "Open-weights image generator by Black Forest Labs with realistic human features.", "limit": "Free (Schnell) / API", "link": "https://blackforestlabs.ai"},
    {"name": "Stable Diffusion 3", "cat": "Image Gen", "cat_class": "cat-creative", "desc": "Stability AI's latest. Multimodal diffusion transformer for hyper-realism.", "limit": "Free (Local) / API", "link": "https://stability.ai"},
    {"name": "Ideogram 2.0", "cat": "Image Gen", "cat_class": "cat-creative", "desc": "The king of text-in-images. Creates perfect typography and graphic designs.", "limit": "Free daily uses", "link": "https://ideogram.ai"},
    {"name": "Leonardo.ai", "cat": "Creative Suite", "cat_class": "cat-creative", "desc": "Production-grade image platform with fine-tuned models for games and art.", "limit": "Daily Free Tokens", "link": "https://leonardo.ai"},
    {"name": "Recraft V3", "cat": "Vector/UI Gen", "cat_class": "cat-creative", "desc": "AI for graphic designers. Generates vectors, icons, and consistent sets.", "limit": "Free tier available", "link": "https://recraft.ai"},
    {"name": "Krea AI", "cat": "Image Enhancer", "cat_class": "cat-creative", "desc": "Real-time AI generation and high-quality upscaling for designers.", "limit": "Free tier / Pro", "link": "https://krea.ai"},
    {"name": "Playground AI", "cat": "Creative Tools", "cat_class": "cat-creative", "desc": "User-friendly platform for combining and editing AI-generated images.", "limit": "Free tier / Sub", "link": "https://playground.com"},
    {"name": "Magnific AI", "cat": "Upscaler", "cat_class": "cat-creative", "desc": "The most powerful AI detail enhancer and upscaler in the world.", "limit": "Subscription only", "link": "https://magnific.ai"},
    {"name": "Adobe Firefly", "cat": "Design Gen", "cat_class": "cat-creative", "desc": "Ethically trained generative AI integrated into Creative Cloud tools.", "limit": "Credit-based / Free", "link": "https://firefly.adobe.com"},
    {"name": "Canva Magic Media", "cat": "Design Tool", "cat_class": "cat-creative", "desc": "Text-to-image and text-to-video generation within the Canva ecosystem.", "limit": "Free / Pro", "link": "https://canva.com"},
    {"name": "NightCafe Creator", "cat": "AI Art", "cat_class": "cat-creative", "desc": "Community-driven AI art platform with multiple model algorithms.", "limit": "Credit-based / Free", "link": "https://nightcafe.studio"},
    {"name": "Artbreeder", "cat": "Image Mixing", "cat_class": "cat-creative", "desc": "Collaborative image tool for 'breeding' and evolving AI portraits and landscapes.", "limit": "Free tier available", "link": "https://artbreeder.com"},
    {"name": "Photoroom", "cat": "Photo Editing", "cat_class": "cat-creative", "desc": "AI-powered background removal and professional product photography generation.", "limit": "Free / Pro", "link": "https://photoroom.com"},
    {"name": "Lensa AI", "cat": "Mobile Creative", "cat_class": "cat-creative", "desc": "All-in-one photo editor known for Magic Avatars and AI image styles.", "limit": "Free trial / Sub", "link": "https://prisma-ai.com/lensa"},
    {"name": "DeepArt", "cat": "Style Transfer", "cat_class": "cat-creative", "desc": "Turns your photos into artworks using the styles of famous painters.", "limit": "Free to try", "link": "https://deepart.io"},
    {"name": "Craiyon", "cat": "Lightweight Image", "cat_class": "cat-creative", "desc": "Simple, free text-to-image generator formerly known as DALL-E mini.", "limit": "Free / Ad-supported", "link": "https://craiyon.com"},
    {"name": "VanceAI", "cat": "Photo Enhancement", "cat_class": "cat-creative", "desc": "AI tools for sharpening, denoising, and restoring old photographs.", "limit": "Credit-based", "link": "https://vanceai.com"},
    {"name": "Looka", "cat": "Logo Design", "cat_class": "cat-creative", "desc": "AI logo maker and brand builder for entrepreneurs and small businesses.", "limit": "Pay-per-design", "link": "https://looka.com"},

    # --- VIDEO & MOTION (51-70) ---
    {"name": "Sora v2", "cat": "Video Gen", "cat_class": "cat-creative", "desc": "OpenAI's cinematic engine. Generates 2-min clips with perfect temporal physics.", "limit": "Subscription only", "link": "https://openai.com/sora"},
    {"name": "Runway Gen-3", "cat": "Video Gen", "cat_class": "cat-creative", "desc": "High-end video-to-video and text-to-video tool for professional VFX.", "limit": "Subscription based", "link": "https://runwayml.com"},
    {"name": "Luma Dream Machine", "cat": "Video Gen", "cat_class": "cat-creative", "desc": "Rapid video generation from text or images with high realism.", "limit": "Free 30 Gens / Mo", "link": "https://lumalabs.ai"},
    {"name": "Kling AI", "cat": "Video Gen", "cat_class": "cat-creative", "desc": "Advanced video generator known for long clips and complex movements.", "limit": "Free daily credits", "link": "https://klingai.com"},
    {"name": "Pika 1.5", "cat": "Animation", "cat_class": "cat-creative", "desc": "Famous for physics-defying effects and creative animation styles.", "limit": "Free tier available", "link": "https://pika.art"},
    {"name": "Haiper AI", "cat": "Video Gen", "cat_class": "cat-creative", "desc": "Visual foundation model for artistic and high-quality video generation.", "limit": "Free daily credits", "link": "https://haiper.ai"},
    {"name": "Synthesia", "cat": "AI Avatars", "cat_class": "cat-creative", "desc": "Create video presentations with realistic digital actors in 120+ languages.", "limit": "Subscription only", "link": "https://synthesia.io"},
    {"name": "HeyGen", "cat": "AI Video", "cat_class": "cat-creative", "desc": "Leading platform for AI video translation and lip-syncing avatars.", "limit": "Free tier / Sub", "link": "https://heygen.com"},
    {"name": "InVideo AI", "cat": "Video Editor", "cat_class": "cat-creative", "desc": "Generate full YouTube or TikTok videos from a single text prompt.", "limit": "Free tier available", "link": "https://invideo.io"},
    {"name": "Veed.io", "cat": "Video Editing", "cat_class": "cat-creative", "desc": "Cloud-based video editor with heavy AI for captions, cuts, and translations.", "limit": "Free tier / Sub", "link": "https://veed.io"},
    {"name": "Captions.ai", "cat": "Content Studio", "cat_class": "cat-creative", "desc": "Full mobile studio for creators with AI eye contact and captions.", "limit": "Subscription based", "link": "https://captions.ai"},
    {"name": "OpusClip", "cat": "Short-form Gen", "cat_class": "cat-creative", "desc": "Turns long-form videos into high-engagement shorts and reels automatically.", "limit": "Free tier / Pro", "link": "https://opus.pro"},
    {"name": "Munch", "cat": "Social Clips", "cat_class": "cat-creative", "desc": "AI platform that extracts viral moments from long-form video content.", "limit": "Subscription based", "link": "https://getmunch.com"},
    {"name": "Riverside.fm AI", "cat": "Podcast Studio", "cat_class": "cat-data", "desc": "Remote recording with AI-powered cleaning, clips, and magic tools.", "limit": "Free tier available", "link": "https://riverside.fm"},
    {"name": "Descript Underlord", "cat": "Video Assistant", "cat_class": "cat-data", "desc": "Personal AI editor that automates tedious cuts, zooms, and cleaning.", "limit": "Free / Sub", "link": "https://descript.com"},
    {"name": "Colossyan", "cat": "Video Avatars", "cat_class": "cat-creative", "desc": "AI video creator for training with high-quality digital presenters.", "limit": "Free trial available", "link": "https://colossyan.com"},
    {"name": "Elai.io", "cat": "AI Video", "cat_class": "cat-creative", "desc": "Generate learning and development videos from text with AI avatars.", "limit": "Free trial available", "link": "https://elai.io"},
    {"name": "DeepBrain AI", "cat": "AI Avatars", "cat_class": "cat-creative", "desc": "Real-time AI video generators featuring highly realistic human avatars.", "limit": "Free trial available", "link": "https://deepbrain.io"},
    {"name": "Wondershare Virbo", "cat": "Video Creator", "cat_class": "cat-creative", "desc": "AI avatar video creator for marketing and social media.", "limit": "Free tier available", "link": "https://virbo.wondershare.com"},
    {"name": "D-ID", "cat": "Animation AI", "cat_class": "cat-creative", "desc": "Animate still photos and create talking avatars with AI technology.", "limit": "Free trial available", "link": "https://d-id.com"},

    # --- AUDIO & MUSIC (71-90) ---
    {"name": "Suno v5", "cat": "Music Gen", "cat_class": "cat-creative", "desc": "Full song generation including lyrics, vocals, and arrangements.", "limit": "50 Credits / Day", "link": "https://suno.com"},
    {"name": "Udio", "cat": "Music Gen", "cat_class": "cat-creative", "desc": "High-fidelity music creation with studio-grade arrangements and vocals.", "limit": "Free / Subscription", "link": "https://udio.com"},
    {"name": "ElevenLabs", "cat": "Speech Gen", "cat_class": "cat-creative", "desc": "World leader in realistic text-to-speech and voice cloning technology.", "limit": "Free 10k Chars / Mo", "link": "https://elevenlabs.io"},
    {"name": "Whisper V3", "cat": "Audio/STT", "cat_class": "cat-data", "desc": "Industry-standard open-weights speech recognition and translation.", "limit": "Open Source / API", "link": "https://openai.com/research/whisper"},
    {"name": "Stable Audio 2.0", "cat": "Music/SFX", "cat_class": "cat-creative", "desc": "Generate long musical tracks and sound effects from text descriptions.", "limit": "Free tier / Sub", "link": "https://stableaudio.com"},
    {"name": "Voice.ai", "cat": "Voice Changer", "cat_class": "cat-creative", "desc": "Real-time AI voice changer with a library of thousands of voices.", "limit": "Free to use", "link": "https://voice.ai"},
    {"name": "Rask AI", "cat": "Localization", "cat_class": "cat-creative", "desc": "One-click video dubbing and translation for global content.", "limit": "Free trial available", "link": "https://rask.ai"},
    {"name": "AIVA", "cat": "Music Comp", "cat_class": "cat-creative", "desc": "AI music composer specialized in cinematic soundtracks and scores.", "limit": "Free for personal use", "link": "https://aiva.ai"},
    {"name": "Spleeter", "cat": "Audio Separator", "cat_class": "cat-data", "desc": "Professional tool to separate music into vocals, drums, and instruments.", "limit": "Open Source", "link": "https://github.com/deezer/spleeter"},
    {"name": "Hume AI", "cat": "Empathic Voice", "cat_class": "cat-creative", "desc": "Empathic AI voice interface that understands and reacts to human emotion.", "limit": "Free demo / API", "link": "https://hume.ai"},
    {"name": "Soundraw", "cat": "Music Creation", "cat_class": "cat-creative", "desc": "AI music generator that lets you customize songs to fit your project.", "limit": "Free to generate", "link": "https://soundraw.io"},
    {"name": "Boomy", "cat": "Music Maker", "cat_class": "cat-creative", "desc": "Create and publish AI songs to streaming services in seconds.", "limit": "Free tier available", "link": "https://boomy.com"},
    {"name": "Voicemod", "cat": "Real-time Voice", "cat_class": "cat-creative", "desc": "Real-time voice changer and soundboard for gamers and streamers.", "limit": "Free tier available", "link": "https://voicemod.net"},
    {"name": "Resemble AI", "cat": "Voice Synthesis", "cat_class": "cat-creative", "desc": "Generate synthetic voices with high customizability and API access.", "limit": "Usage based", "link": "https://resemble.ai"},
    {"name": "Murf.ai", "cat": "Voiceover AI", "cat_class": "cat-creative", "desc": "Studio-quality AI voiceovers for e-learning, ads, and presentations.", "limit": "Free trial available", "link": "https://murf.ai"},
    {"name": "Mubert", "cat": "Generative Streams", "cat_class": "cat-creative", "desc": "AI-powered real-time music for videos and live streams.", "limit": "Free tier available", "link": "https://mubert.com"},
    {"name": "Speechify", "cat": "TTS Reader", "cat_class": "cat-creative", "desc": "Reads documents, articles, and PDFs aloud with natural AI voices.", "limit": "Free tier available", "link": "https://speechify.com"},
    {"name": "Listnr", "cat": "Audio Platform", "cat_class": "cat-creative", "desc": "AI voice platform for creating podcasts and audio content at scale.", "limit": "Free tier available", "link": "https://listnr.tech"},
    {"name": "Landr AI", "cat": "Music Mastering", "cat_class": "cat-data", "desc": "AI-powered music mastering, distribution, and plugins for musicians.", "limit": "Free to try", "link": "https://landr.com"},
    {"name": "Adobe Enhance", "cat": "Audio Cleaning", "cat_class": "cat-data", "desc": "Web tool that makes poor quality recordings sound like professional studio audio.", "limit": "Free Access", "link": "https://podcast.adobe.com/enhance"},

    # --- SEARCH & RESEARCH (91-110) ---
    {"name": "Perplexity Pro", "cat": "AI Search", "cat_class": "cat-research", "desc": "AI-native search engine providing direct answers with full citations.", "limit": "Free / Pro $20/mo", "link": "https://perplexity.ai"},
    {"name": "Genspark", "cat": "Agentic Search", "cat_class": "cat-research", "desc": "Search engine that autonomously builds web pages for your query.", "limit": "Free tier available", "link": "https://genspark.ai"},
    {"name": "Phind", "cat": "Dev Search", "cat_class": "cat-research", "desc": "Search engine optimized for developers with code-first answers.", "limit": "Free tier / Pro", "link": "https://phind.com"},
    {"name": "Consensus", "cat": "Science Search", "cat_class": "cat-research", "desc": "Search engine that answers questions using peer-reviewed papers.", "limit": "Free search", "link": "https://consensus.app"},
    {"name": "Elicit", "cat": "Research Assistant", "cat_class": "cat-research", "desc": "Automates literature reviews and data extraction for researchers.", "limit": "Free trial available", "link": "https://elicit.com"},
    {"name": "Scholarcy", "cat": "Paper Summary", "cat_class": "cat-research", "desc": "Reads and summarizes long research papers into flashcards.", "limit": "Free extension", "link": "https://scholarcy.com"},
    {"name": "Exa AI", "cat": "Neural Search", "cat_class": "cat-research", "desc": "The search engine for AI agents to find high-quality information.", "limit": "Free API tier", "link": "https://exa.ai"},
    {"name": "Tavily", "cat": "Search API", "cat_class": "cat-research", "desc": "Search engine optimized specifically for autonomous agents.", "limit": "Free API tier", "link": "https://tavily.com"},
    {"name": "You.com", "cat": "AI Search", "cat_class": "cat-research", "desc": "Private and customizable AI search engine with integrated tools.", "limit": "Free tier available", "link": "https://you.com"},
    {"name": "Scite.ai", "cat": "Smart Citations", "cat_class": "cat-research", "desc": "Verify research papers by seeing how they have been cited.", "limit": "Free trial available", "link": "https://scite.ai"},
    {"name": "Kaitiaki", "cat": "Research Agent", "cat_class": "cat-research", "desc": "Autonomous agent for environmental and conservation research.", "limit": "Open Access", "link": "https://kaitiaki.ai"},
    {"name": "WolframAlpha", "cat": "Computational", "cat_class": "cat-data", "desc": "The definitive source for computational knowledge and math.", "limit": "Free / Pro", "link": "https://wolframalpha.com"},
    {"name": "Semantic Scholar", "cat": "Academic Search", "cat_class": "cat-research", "desc": "AI-powered search for finding and citing scientific literature.", "limit": "Free to use", "link": "https://semanticscholar.org"},
    {"name": "ResearchRabbit", "cat": "Literature Mapping", "cat_class": "cat-research", "desc": "Visual discovery tool for mapping out scientific citations and networks.", "limit": "Free to use", "link": "https://researchrabbitapp.com"},
    {"name": "Iris.ai", "cat": "Scientific Agent", "cat_class": "cat-research", "desc": "Autonomous researcher for corporate R&D and scientific discovery.", "limit": "Professional access", "link": "https://iris.ai"},
    {"name": "Connected Papers", "cat": "Research Mapping", "cat_class": "cat-research", "desc": "Visualize connections between research papers in a specific field.", "limit": "Free tier available", "link": "https://connectedpapers.com"},
    {"name": "OpenAlex", "cat": "Open Research", "cat_class": "cat-research", "desc": "Open index of the world's scholarly research system.", "limit": "Free API", "link": "https://openalex.org"},
    {"name": "Base Search", "cat": "Academic Index", "cat_class": "cat-research", "desc": "One of the world's most voluminous search engines for academic resources.", "limit": "Free to use", "link": "https://base-search.net"},
    {"name": "Dimensions AI", "cat": "Research Data", "cat_class": "cat-data", "desc": "Platform that connects research across grants, patents, and papers.", "limit": "Free personal use", "link": "https://dimensions.ai"},
    {"name": "DeepKnowledge", "cat": "Library Agent", "cat_class": "cat-research", "desc": "Agentic interface for massive academic and institutional libraries.", "limit": "Sub based", "link": "https://deepknowledge.ai"}
]

def generate_card(tool):
    search_data = f"{tool['name']} {tool['cat']} {tool['desc']}".lower()
    return f"""
            <div class="tool-card" data-search="{search_data}">
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

        .hero-section {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 60px;
            flex-wrap: wrap;
            gap: 40px;
        }}

        .page-title {{
            font-family: 'Syncopate', sans-serif;
            font-size: clamp(2rem, 5vw, 4rem);
            text-transform: uppercase;
            background: linear-gradient(to right, #fff, var(--accent-lime));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .search-container {{
            position: relative;
            width: 100%;
            max-width: 450px;
        }}

        #toolSearch {{
            width: 100%;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--glass-border);
            padding: 18px 30px;
            border-radius: 100px;
            color: #fff;
            font-family: 'Space Mono', monospace;
            outline: none;
            transition: 0.3s;
            font-size: 1rem;
        }}

        #toolSearch:focus {{
            border-color: var(--accent-cyan);
            background: rgba(255,255,255,0.08);
            box-shadow: 0 0 30px rgba(0, 242, 255, 0.15);
        }}

        .page-subtitle {{
            color: var(--text-dim);
            max-width: 600px;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-top: 20px;
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

        #noResults {{
            display: none;
            text-align: center;
            padding: 100px 0;
            color: var(--text-dim);
            font-family: 'Space Mono', monospace;
            grid-column: 1 / -1;
            font-size: 1.2rem;
            letter-spacing: 2px;
        }}

    </style>
</head>
<body>
    <div class="grid-overlay"></div>

    <header>
        <a href="index.html" class="logo">AI FRONTIER <span>2026</span></a>
        <a href="index.html" class="back-link">// RETURN TO FEED</a>
    </header>

    <div class="container">
        <div class="hero-section">
            <div>
                <h1 class="page-title">The Vibe Coder's<br>Toolkit</h1>
                <p class="page-subtitle">
                    A comprehensive index of 100+ high-performance AI tools and models. 
                    Real-time search enabled for the complete 2026 datastream.
                </p>
            </div>
            <div class="search-container">
                <input type="text" id="toolSearch" placeholder="Search by name, category, or task...">
            </div>
        </div>

        <div class="tools-grid" id="toolsGrid">
{cards_html}
            <div id="noResults">// NO MATCHING AGENTS FOUND IN DATASTREAM</div>
        </div>
    </div>

    <script>
        const searchInput = document.getElementById('toolSearch');
        const toolCards = document.querySelectorAll('.tool-card');
        const noResults = document.getElementById('noResults');

        searchInput.addEventListener('input', (e) => {{
            const query = e.target.value.toLowerCase().trim();
            let visibleCount = 0;

            toolCards.forEach(card => {{
                const searchData = card.getAttribute('data-search');
                if (searchData.includes(query)) {{
                    card.style.display = 'flex';
                    visibleCount++;
                }} else {{
                    card.style.display = 'none';
                }}
            }});

            if (visibleCount === 0) {{
                noResults.style.display = 'block';
            }} else {{
                noResults.style.display = 'none';
            }}
        }});
    </script>
</body>
</html>"""

with open('repos/ai-frontier-2026/tools.html', 'w') as f:
    f.write(html_template)

print(f"Updated tools.html with {len(tools_data)} tools and real-time search.")
