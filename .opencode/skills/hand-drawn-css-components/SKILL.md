---
name: hand-drawn-css-components
description: |
  Create hand-drawn, sketchy UI components using pure CSS without external libraries.
  Use when: (1) Building notebook/doodle-style interfaces, (2) Creating organic
  non-digital-looking UIs, (3) Implementing sketchy borders and wobbly effects.
  Includes asymmetric border-radius technique, wavy dividers, and component library.
author: Claude Code
version: 1.0.0
date: 2026-02-23
---

# Hand-Drawn CSS Components

## Core Technique: Asymmetric Border Radius

The signature "wobbly" border effect is achieved with asymmetric border-radius values:

```css
.hand-drawn {
  border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
}
```

This creates an organic, slightly irregular shape that mimics hand-drawn lines.

## Visual Style Principles

1. **Sketchy Borders**: Use asymmetric border-radius on cards, buttons, and containers
2. **Dashed Lines**: Use `border: 2px dashed` for dividers and secondary elements
3. **Paper Textures**: Off-white backgrounds (`--bg-cream: #FDF8F3`, `--bg-paper: #FFFEF9`)
4. **Pencil Colors**: Dark gray (`--pencil: #2B2B2B`) instead of pure black for softer contrast
5. **Highlighters**: Use gradient underlines to simulate marker highlights
6. **Shadows**: Slight offsets (`box-shadow: 3px 4px 0`) create depth without looking digital

## Font Stack

```css
/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&family=Nunito:wght@400;600;700&family=Patrick+Hand&display=swap');

/* Font usage */
--font-heading: 'Caveat', cursive;      /* Handwritten headers */
--font-ui: 'Patrick Hand', cursive;      /* Handwritten UI text */
--font-body: 'Nunito', sans-serif;       /* Clean body text */
```

## Component Library

### Base Card

```css
.card {
  background: var(--bg-paper);
  padding: 35px;
  margin-bottom: 25px;
  box-shadow: 3px 4px 0 rgba(0,0,0,0.1);
  border: 2px solid var(--pencil);
  border-radius: 4px;
}
```

### Hand-Drawn Card

```css
.card-sketchy {
  background: var(--bg-paper);
  padding: 35px;
  margin-bottom: 25px;
  box-shadow: 3px 4px 0 rgba(0,0,0,0.1);
  border: 2px solid var(--pencil);
  border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
}
```

### Section Title with Icon

```css
h2 {
  font-family: 'Caveat', cursive;
  font-size: 1.9rem;
  color: var(--pencil);
  margin-bottom: 18px;
  padding-left: 45px;
  position: relative;
  min-height: 40px;
  display: flex;
  align-items: center;
}

h2 .fa-icon {
  position: absolute;
  left: 0;
  width: 38px;
  height: 38px;
  background: var(--bg-paper);
  border: 2px solid var(--pencil);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
}
```

### Quote Box

```css
.quote-box {
  background: linear-gradient(135deg, #FFF9E6, #FFF5D6);
  border-left: 5px solid var(--accent-sunflower);
  padding: 20px 25px;
  margin: 20px 0;
  border-radius: 0 16px 16px 0;
  font-size: 1.05rem;
  font-style: italic;
  border: 2px dashed var(--accent-sunflower);
}
```

### Insight Box

```css
.insight-box {
  background: linear-gradient(135deg, #FFFDE7, #FFF9C4);
  border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
  padding: 22px;
  margin: 22px 0;
  display: flex;
  align-items: flex-start;
  gap: 16px;
  border: 3px solid var(--accent-sunflower);
}

.insight-icon { font-size: 1.8rem; }
```

### Wavy Divider

```css
.wavy-divider {
  text-align: center;
  margin: 30px 0;
  position: relative;
}

.wavy-divider::before {
  content: '~ ~ ~ ~ ~';
  font-family: 'Caveat', cursive;
  font-size: 2rem;
  color: var(--accent-coral);
  letter-spacing: 15px;
  opacity: 0.6;
}
```

### Dashed Line Divider

```css
.divider {
  text-align: center;
  margin: 45px 0;
}

.divider::before {
  content: '~~~~~~~';
  font-family: 'Caveat', cursive;
  font-size: 1.5rem;
  color: var(--accent-lavender);
  letter-spacing: 10px;
}
```

## Complete HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&family=Nunito:wght@400;600;700&family=Patrick+Hand&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        /* CSS Variables */
        :root {
            --bg-cream: #FDF8F3;
            --bg-paper: #FFFEF9;
            --accent-coral: #FF6B6B;
            --accent-teal: #4ECDC4;
            --accent-sunflower: #FFE66D;
            --accent-lavender: #C9B1FF;
            --text-dark: #2D3436;
            --text-muted: #636E72;
            --pencil: #2B2B2B;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Nunito', sans-serif;
            background: var(--bg-cream);
            color: var(--text-dark);
            line-height: 1.7;
        }

        .container { max-width: 900px; margin: 0 auto; padding: 40px 20px; }

        /* Hand-drawn borders */
        .hand-drawn {
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
        }

        /* Typography */
        h1 {
            font-family: 'Caveat', cursive;
            font-size: 2.8rem;
            color: var(--pencil);
            position: relative;
            display: inline-block;
        }

        h1::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, var(--accent-coral), var(--accent-teal), var(--accent-sunflower));
            border-radius: 3px;
            opacity: 0.6;
        }

        /* Card */
        .card {
            background: var(--bg-paper);
            padding: 35px;
            margin-bottom: 25px;
            box-shadow: 3px 4px 0 rgba(0,0,0,0.1);
            border: 2px solid var(--pencil);
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hand-Drawn Title</h1>
        <div class="card">
            <p>This card has that sketchy, hand-drawn look.</p>
        </div>
    </div>
</body>
</html>
```

## No External Libraries Required

This approach uses pure CSS - no dependencies on:
- Rough.js
- Chart.js sketchy themes
- Excalidraw components
- Hand-drawn icon sets

Everything is pure CSS for better performance and consistency.
