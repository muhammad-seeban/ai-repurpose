# 🎬 AI Content Repurposing Engine

**Turn 1 YouTube video into 5+ high-quality social posts in under 30 seconds.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📌 Overview

This is a production-ready microservice that takes a YouTube URL and a tone (professional, casual, funny) and generates platform-optimized posts for:

- **LinkedIn** – thought leadership posts
- **Twitter / X** – short, punchy threads
- **Blog** – full-length articles
- **Instagram Caption** – engaging hooks with emojis
- **Newsletter** – subscriber-friendly summaries

It uses **Hugging Face Inference API** (free tier) with the **Mistral-7B-Instruct** model to generate human-like, engaging content. The entire app runs on **Railway** free tier with zero cold-start delays — always responsive.

---

## 🚀 Why This Exists

Content creators, agencies, and brands spend **hours** repurposing one video into multiple posts. This engine does it in **seconds**. It's built for:

- ✅ YouTubers who want to grow on other platforms
- ✅ Marketing agencies handling multiple clients
- ✅ Solopreneurs who want to scale content without hiring writers
- ✅ Brands that need consistent multi-channel presence

---

## 🧠 How It Works


---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.10 + Flask |
| AI API | Hugging Face Inference (Mistral-7B-Instruct) |
| Deployment | Railway (free tier, always-on) |
| Auth (future) | JWT + Stripe |
| Version Control | Git + GitHub |

---

## 📦 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ai-repurpose.git
cd ai-repurpose
