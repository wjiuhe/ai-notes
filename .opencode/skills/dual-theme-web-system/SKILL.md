---
name: dual-theme-web-system
description: |
  Implement a dual-theme (light/dark) website system with shared component architecture.
  Use when: (1) Creating websites with day/night or casual/professional modes,
  (2) Building theme switchable interfaces, (3) Implementing consistent component libraries
  across multiple visual styles. Supports parallel index pages, shared CSS variables,
  and seamless theme navigation.
author: Claude Code
version: 1.0.0
date: 2026-02-23
---

# Dual-Theme Website System

## Problem
Websites often need multiple visual themes (light/dark, casual/professional) but maintaining separate codebases creates duplication and inconsistency.

## Solution
A parallel architecture with shared components and theme-specific styling via CSS variables.

## Architecture

### File Structure
```
/project-root
├── index.html              # Light theme homepage
├── index_dark.html         # Dark theme homepage
├── page-light.html         # Light content page
├── page-dark.html          # Dark content page
├── static/
│   ├── styles.css         # Light theme styles
│   └── dark-theme.css     # Dark theme styles
└── AGENT.md               # Design system documentation
```

### CSS Variable Architecture

**Light Theme (`styles.css`)**
```css
:root {
  /* Backgrounds */
  --bg-cream: #FDF8F3;
  --bg-paper: #FFFEF9;

  /* Accents */
  --accent-coral: #FF6B6B;
  --accent-teal: #4ECDC4;
  --accent-sunflower: #FFE66D;
  --accent-lavender: #C9B1FF;

  /* Text */
  --text-dark: #2D3436;
  --text-muted: #636E72;
  --pencil: #2B2B2B;

  /* Fonts */
  --font-heading: 'Caveat', cursive;
  --font-ui: 'Patrick Hand', cursive;
  --font-body: 'Nunito', sans-serif;
}
```

**Dark Theme (`dark-theme.css`)**
```css
:root {
  /* Backgrounds - Pitch Black Void */
  --bg-primary: #050505;
  --bg-secondary: #0a0a0a;
  --bg-tertiary: #141414;

  /* Accents - Dracula-inspired */
  --accent-purple: #bd93f9;
  --accent-pink: #ff79c6;
  --accent-cyan: #8be9fd;
  --accent-green: #50fa7b;
  --accent-orange: #ffb86c;

  /* Text */
  --fg-primary: #f8f8f2;
  --fg-secondary: #bfbfbf;
  --fg-muted: #6272a4;

  /* Fonts */
  --font-mono: 'Courier New', monospace;
  --font-hand: 'Caveat', cursive;
}
```

### Component Consistency

**Card Component - Both Themes**
```css
/* Light Theme */
.card {
  background: var(--bg-paper);
  border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
  border: 2px solid var(--pencil);
  box-shadow: 3px 4px 0 rgba(0,0,0,0.1);
}

/* Dark Theme */
.article-card {
  background: var(--bg-secondary);
  border: 1px solid #3d3d3d;
  border-radius: 8px;
}
```

## Cross-Theme Navigation

### Portal Links

**Light Theme (index.html)**
```html
<a href="index_dark.html" style="color: #5d4037;">
  <i class="fa-solid fa-moon"></i> Enter the Night Mode
</a>
```

**Dark Theme (index_dark.html)**
```html
<a href="index.html" class="portal-back">
  <span>Return to Daylight</span>
</a>
```

## Implementation Checklist

- [ ] Create base CSS with variables for theme 1
- [ ] Create parallel CSS with variables for theme 2
- [ ] Build index.html for theme 1
- [ ] Build index_dark.html for theme 2
- [ ] Add cross-theme portal links
- [ ] Document component usage in AGENT.md
- [ ] Test component consistency across both themes

## When to Use Each Theme

**Use Light Theme for:**
- Technical tutorials and documentation
- Architecture deep-dives
- Educational content
- Professional presentations
- Standard articles

**Use Dark Theme for:**
- Late night thoughts and reflections
- Personal philosophy pieces
- Coffee/culture content
- "Overtime" style content
- Humor about coding struggles
