import sys
import json
import re
import os

def update_index():
    file_path = 'repos/ai-frontier-2026/index.html'
    
    with open(file_path, 'r') as f:
        content = f.read()

    # New posts to prepend
    new_posts = """
    <div class=\"blog-post\" onclick=\"showDetail(this)\">
        <div class=\"post-meta\">FEB 04 // 03:45 UTC // SOURCE: AI BUSINESS</div>
        <h3>🚀 The $1.25 Trillion Merger: xAI + SpaceX</h3>
        <div class=\"short-desc\">
            <p>Elon Musk's xAI and SpaceX have officially merged in a deal valued at $1.25 trillion, aiming to integrate advanced AI into deep space exploration.</p>
        </div>
        <div class=\"long-desc\">
            <p>In a historic move, <strong>xAI and SpaceX</strong> have combined forces to accelerate the development of autonomous spacecraft and planetary colonization systems. This merger creates a tech behemoth focused on "Interstellar Intelligence."</p>
            <p><br><strong>Projected Impact:</strong></p>
            <ul>
                <li><strong>Autonomous Navigation:</strong> AI agents will now handle 99% of flight operations for Starship missions.</li>
                <li><strong>Resource Extraction:</strong> Specialized AI models are being trained to manage mining robots on the Lunar surface.</li>
                <li><strong>Unified Neural Link:</strong> Rumors suggest a deeper integration between Starlink and xAI's real-time processing capabilities.</li>
            </ul>
            <div class=\"tag-pill\">SpaceX</div>
            <div class=\"tag-pill\">xAI</div>
            <div class=\"tag-pill\">Space Tech</div>
        </div>
        <div class=\"tag-pill\">Merger</div>
    </div>

    <div class=\"blog-post\" onclick=\"showDetail(this)\">
        <div class=\"post-meta\">FEB 04 // 03:30 UTC // SOURCE: CIO MAGAZINE</div>
        <h3>🛠️ From Coding to Engineering: The Rise of Autonomous Agents</h3>
        <div class=\"short-desc\">
            <p>2026 marks the year where AI evolved from writing snippets to managing entire software engineering lifecycles autonomously.</p>
        </div>
        <div class=\"long-desc\">
            <p>Simple code completion is a thing of the past. Today's <strong>Autonomous Engineering Agents</strong> are capable of taking a high-level requirement and turning it into a deployed, tested, and monitored microservice architecture.</p>
            <p><br><strong>What's New:</strong></p>
            <ul>
                <li><strong>Self-Healing Pipelines:</strong> Agents now detect and fix deployment failures in real-time without human intervention.</li>
                <li><strong>Contextual Architecture:</strong> AI can now reason about the long-term implications of architectural decisions across massive codebases.</li>
                <li><strong>Automated Debt Reduction:</strong> Dedicated "Janitor" agents continuously refactor legacy code to maintain system health.</li>
            </ul>
            <div class=\"tag-pill\">DevOps</div>
            <div class=\"tag-pill\">Autonomous Engineering</div>
            <div class=\"tag-pill\">Software Lifecycle</div>
        </div>
        <div class=\"tag-pill\">Engineering</div>
    </div>
    """

    # Find the blog-stream div and prepend the new posts
    pattern = re.compile(r'(<div class=\"blog-stream\">)', re.IGNORECASE)
    new_content = pattern.sub(r'\1' + new_posts, content)

    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print("Website updated successfully.")

if __name__ == "__main__":
    update_index()
