from flask import Flask, request, jsonify, render_template_string
import requests
import os

app = Flask(__name__)

HF_TOKEN = os.environ.get("HF_TOKEN", "")

def query_hf(prompt):
    if not HF_TOKEN:
        return f"[MOCK] Generated post: {prompt[:50]}... (Get HF_TOKEN for real AI)"
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 300, "temperature": 0.7}}
    try:
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        if resp.status_code == 200:
            return resp.json()[0]["generated_text"]
        else:
            return f"[Error] {resp.text}"
    except Exception as e:
        return f"[Fallback] Could not generate: {str(e)}"

HTML = """
<!DOCTYPE html>
<html>
<head><title>AI Repurposer</title></head>
<body>
<h2>🎬 YouTube → 5 Posts in 1 Click</h2>
<form method="POST" action="/generate">
  <input type="text" name="url" placeholder="YouTube URL" size="50" required><br>
  <select name="tone">
    <option value="professional">Professional</option>
    <option value="casual">Casual</option>
    <option value="funny">Funny</option>
  </select><br>
  <button type="submit">Generate Posts</button>
</form>
<p style="color:gray;">First 5 uses free. Then $9.99 one-time.</p>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML)

@app.route("/generate", methods=["POST"])
def generate():
    url = request.form.get("url")
    tone = request.form.get("tone", "professional")
    video_id = url.split("v=")[-1].split("&")[0]
    sample_transcript = f"Transcript of {video_id}: AI is transforming content creation."
    platforms = ["LinkedIn", "Twitter", "Blog", "Instagram Caption", "Newsletter"]
    results = {}
    for p in platforms:
        prompt = f"Write a {tone} {p} post (max 280 chars for Twitter) based on: {sample_transcript}. Include 3 hashtags."
        results[p] = query_hf(prompt)
    return jsonify({
        "video_id": video_id,
        "tone": tone,
        "posts": results,
        "message": "✅ Free demo complete. Contact for bulk at $200/month."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)