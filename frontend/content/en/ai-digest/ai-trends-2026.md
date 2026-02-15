---
title: "AI Trends in 2026"
date: 2026-02-15T16:00:00+03:00
draft: false
tags: ["AI", "Machine Learning", "Trends"]
---

## The Future of AI

AI continues to verify rapidly.

<div class="my-8">
    <div class="flex gap-2 max-w-md mb-4">
        <input type="text" id="digest-topic" placeholder="Enter topic (e.g. Remote Work)" class="flex-1 px-4 py-2 rounded-lg border border-neutral-300 dark:border-neutral-700 dark:bg-neutral-900">
        <button id="generate-btn" onclick="generateDigest()" class="px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition">Generate</button>
    </div>
    <div id="digest-result"></div>
</div>

{{ partial "ai-digest-logic.html" . }}

