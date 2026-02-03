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
        <div class=\"post-meta\">FEB 03 // 17:15 UTC // SOURCE: TECH YAHOO</div>
        <h3>🦾 The Physical AI Craze: Robotic Arms & Cobots</h3>
        <div class=\"short-desc\">
            <p>Manufacturers are rapidly adopting physical AI to fill labor shortages, with robotic arms and cobots handling repetitive tasks autonomously.</p>
        </div>
        <div class=\"long-desc\">
            <p>The boundary between digital and physical intelligence is blurring. <strong>Physical AI</strong> is no longer just a laboratory concept; it is being deployed at scale. In early 2026, we are seeing a massive surge in the use of robotic arms and collaborative robots (cobots) across the manufacturing sector.</p>
            <p><br><strong>Key Impact:</strong></p>
            <ul>
                <li><strong>Labor Gap Closure:</strong> AI-driven robotics are filling critical shortages in repetitive industrial roles.</li>
                <li><strong>Safe Collaboration:</strong> Modern cobots use advanced spatial reasoning to work alongside humans without safety cages.</li>
                <li><strong>Autonomy:</strong> These systems learn and adapt to new tasks in real-time, reducing downtime and reconfiguration costs.</li>
            </ul>
            <div class=\"tag-pill\">Physical AI</div>
            <div class=\"tag-pill\">Automation</div>
            <div class=\"tag-pill\">Robotics</div>
        </div>
        <div class=\"tag-pill\">Physical AI</div>
    </div>

    <div class=\"blog-post\" onclick=\"showDetail(this)\">
        <div class=\"post-meta\">FEB 03 // 17:10 UTC // SOURCE: INTERNATIONAL BANKER</div>
        <h3>🌐 Agentic AI: The New Efficiency Frontier</h3>
        <div class=\"short-desc\">
            <p>Agentic AI is revolutionizing resource efficiency and complex task automation, introducing entirely new business innovations beyond traditional models.</p>
        </div>
        <div class=\"long-desc\">
            <p>As we move into 2026, <strong>Agentic AI</strong> has emerged as the defining technology for enterprise efficiency. Unlike static models, these agents can reason, use tools, and execute multi-step workflows with minimal human supervision.</p>
            <p><br><strong>Why It Matters:</strong></p>
            <ul>
                <li><strong>Complex Task Mastery:</strong> Agents are now handling end-to-step procurement, customer support triage, and software engineering.</li>
                <li><strong>Business Innovation:</strong> Companies are launching entire service lines that are managed 100% by autonomous agent swarms.</li>
                <li><strong>Resource Optimization:</strong> Real-time data processing by agents is cutting operational waste by an average of 30% in early adopters.</li>
            </ul>
            <div class=\"tag-pill\">Agentic AI</div>
            <div class=\"tag-pill\">Efficiency</div>
            <div class=\"tag-pill\">Enterprise</div>
        </div>
        <div class=\"tag-pill\">Agentic AI</div>
    </div>

    <div class=\"blog-post\" onclick=\"showDetail(this)\">
        <div class=\"post-meta\">FEB 03 // 17:05 UTC // SOURCE: UX TIGERS</div>
        <h3>🧠 Beyond Software: AI as Workforce Reorganization</h3>
        <div class=\"short-desc\">
            <p>In 2026, AI has transitioned from a software update to a structural reorganization of the global workforce. The agentic economy is here.</p>
        </div>
        <div class=\"long-desc\">
            <p>The 2026 landscape shows that AI is no longer a tool we \"use,\" but a coworker we \"orchestrate.\" <strong>UX Tigers</strong> reports that the most successful organizations have completely restructured their hierarchy to accommodate AI agents at every level.</p>
            <p><br><strong>Structural Shifts:</strong></p>
            <ul>
                <li><strong>From Doers to Architects:</strong> The human role has shifted from manual execution to high-level intent architecture.</li>
                <li><strong>Autonomous Departments:</strong> Entire sub-sections of companies (especially in data analysis and dev) are now operating autonomously.</li>
                <li><strong>Real-Time Adaptation:</strong> Workforce scaling is now handled by agents based on real-time market demand.</li>
            </ul>
            <div class=\"tag-pill\">Workforce 2026</div>
            <div class=\"tag-pill\">Strategy</div>
            <div class=\"tag-pill\">Agent Economy</div>
        </div>
        <div class=\"tag-pill\">Future of Work</div>
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
