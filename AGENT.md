# Mind & Machine - Style Guide

This document provides the CSS styling conventions used across the Mind & Machine website.

## Common CSS Variables

```css
:root {
    --bg-cream: #FDF8F3;
    --bg-paper: #FFFEF9;
    --accent-coral: #FF6B6B;
    --accent-teal: #4ECDC4;
    --accent-sunflower: #FFE66D;
    --accent-lavender: #C9B1FF;
    --accent-sky: #A8E6CF;
    --accent-red: #E74C3C;
    --accent-green: #27AE60;
    --accent-orange: #E67E22;
    --text-dark: #2D3436;
    --text-muted: #636E72;
    --pencil: #2B2B2B;
}
```

## External Dependencies

Include these in the `<head>`:

```html
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&family=Nunito:wght@400;600;700&family=Patrick+Hand&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="static/styles.css">
```

## Hand-Drawn Style System

The Mind & Machine website uses a **custom hand-drawn/sketchy aesthetic** built with CSS, not a pre-made library. This gives the site its distinctive "notebook doodle" look.

### Hand-Drawn Fonts (Google Fonts)

We use three fonts to create the hand-drawn feel:

- **Caveat** - Headings and titles (cursive handwritten style)
- **Patrick Hand** - Subtitles, labels, and UI text (clean handwritten style)  
- **Nunito** - Body text (rounded sans-serif for readability)

### Sketchy Border Technique

The signature "wobbly" border effect is achieved with **asymmetric border-radius values**:

```css
.hand-drawn {
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
}
```

This creates an organic, slightly irregular shape that mimics hand-drawn lines.

### Visual Style Principles

1. **Sketchy Borders**: Use the asymmetric border-radius on cards, buttons, and containers
2. **Dashed Lines**: Use `border: 2px dashed` for dividers and secondary elements
3. **Paper Textures**: Off-white backgrounds (`--bg-cream: #FDF8F3`, `--bg-paper: #FFFEF9`)
4. **Pencil Colors**: Dark gray (`--pencil: #2B2B2B`) instead of pure black for softer contrast
5. **Highlighters**: Use gradient underlines to simulate marker highlights
6. **Shadows**: Slight offsets (`box-shadow: 3px 4px 0`) create depth without looking digital

### No External Drawing Libraries

We don't use libraries like:
- Rough.js
- Chart.js sketchy themes
- Excalidraw components
- Hand-drawn icon sets

Everything is pure CSS for better performance and consistency.

## CSS Organization

**Use the shared CSS first!** Unless you need to do something different, use the shared `static/styles.css`. This ensures consistent styling across all pages.

Only add page-specific CSS when:
- You need unique components not in the shared CSS
- You need to override shared styles for a specific page
- The page has special requirements that differ from the standard layout

## Base Styles

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Nunito', sans-serif;
    background: var(--bg-cream);
    color: var(--text-dark);
    line-height: 1.7;
    min-height: 100vh;
}

.container { max-width: 900px; margin: 0 auto; padding: 40px 20px; }
```

## Typography

### Headings

```css
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

h3 { font-family: 'Patrick Hand', cursive; font-size: 1.3rem; color: var(--text-dark); margin: 20px 0 10px; }
h4 { font-family: 'Patrick Hand', cursive; font-size: 1.15rem; color: var(--text-muted); margin: 15px 0 8px; }
```

### Subtitle

```css
.subtitle { 
    font-family: 'Patrick Hand', cursive; 
    font-size: 1.4rem; 
    color: var(--text-muted); 
    margin-top: 15px; 
}
```

### Page Header (Title, Author, Date)

For all content pages, use a centered header with title, subtitle, and author/date info:

```css
header { 
    text-align: center; 
    margin-bottom: 50px; 
}

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
```

HTML structure:
```html
<header>
    <h1>Page Title</h1>
    <p class="subtitle">Subtitle describing the page</p>
    <p style="margin-top: 20px; font-size: 0.9rem; color: var(--text-muted);">
        <i class="fa-solid fa-user"></i> Jiuhe Wang &nbsp;&nbsp;|&nbsp;&nbsp; 
        <i class="fa-regular fa-calendar"></i> Created: Feb 21, 2026
    </p>
</header>
```

Key points:
- Center the header with `text-align: center`
- Use 50px bottom margin for spacing before content
- Author name: "Jiuhe Wang"
- Date format: "Created: MMM DD, YYYY"
- Use `&nbsp;&nbsp;|&nbsp;&nbsp;` for separator spacing

## Components

### Card

Main content container with hand-drawn style:

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

### Section Title with Icon

```css
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

Usage:
```html
<h2><i class="fa-solid fa-icon-name fa-icon"></i>Section Title</h2>
```

### Comparison Table

```css
.comparison-table { 
    width: 100%; 
    border-collapse: separate; 
    border-spacing: 0; 
    margin: 22px 0; 
    font-size: 0.9rem; 
    border: 2px solid var(--pencil); 
    border-radius: 15px; 
    overflow: hidden; 
}

.comparison-table th, .comparison-table td { 
    padding: 14px 18px; 
    text-align: left; 
    border-bottom: 2px dashed rgba(0,0,0,0.15); 
}

.comparison-table th { 
    font-family: 'Patrick Hand', cursive; 
    font-size: 1.15rem; 
    background: #F5F0E8; 
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

### Enhanced Code Block

Use this format for code snippets with syntax highlighting and a macOS-style header:

```css
/* Code Block Container */
.code-block {
    background: linear-gradient(135deg, #1E272E 0%, #252F38 100%);
    color: #E8F4F8;
    padding: 0;
    border-radius: 20px;
    font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    font-size: 0.9rem;
    margin: 25px 0;
    overflow-x: auto;
    border: 3px solid var(--pencil);
    box-shadow: 4px 6px 0 rgba(0,0,0,0.2);
}

/* Code Header with macOS dots */
.code-header {
    background: linear-gradient(135deg, #2D3A47 0%, #384554 100%);
    padding: 12px 20px;
    border-bottom: 2px solid #343D46;
    display: flex;
    align-items: center;
    gap: 10px;
    font-family: 'Patrick Hand', cursive;
    font-size: 0.95rem;
    color: #8FA5B5;
}

.code-header .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
}

.code-header .dot.red { background: #FF5F56; }
.code-header .dot.yellow { background: #FFBD2E; }
.code-header .dot.green { background: #27CA40; }

/* Code Content */
.code-content {
    padding: 20px 25px;
    line-height: 1.7;
    white-space: pre;
    overflow-x: auto;
}

/* Syntax Highlighting */
.code-block .comment { color: #6A9955; font-style: italic; }
.code-block .key { color: #9CDCFE; font-weight: 600; }
.code-block .string { color: #CE9178; }
.code-block .number { color: #B5CEA8; }
.code-block .boolean { color: #569CD6; }
.code-block .keyword { color: #C586C0; }
.code-block .tag { color: #4EC9B0; }
.code-block .attr { color: #9CDCFE; }
.code-block .operator { color: #D4D4D4; }
.code-block .punctuation { color: #D4D4D4; }
```

HTML structure:
```html
<div class="code-block">
    <div class="code-header">
        <span class="dot red"></span>
        <span class="dot yellow"></span>
        <span class="dot green"></span>
        <span>filename.json</span>
    </div>
    <div class="code-content"><span class="key">"name"</span><span class="operator">:</span> <span class="string">"value"</span></div>
</div>
```

### Solution Box

```css
.solution-box {
    background: linear-gradient(135deg, #E8F8F5, #D1F2EB);
    border: 3px solid var(--accent-teal);
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
}

.solution-title {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.3rem;
    color: var(--accent-teal);
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}
```

### Recommendation Box

```css
.recommendation-box {
    background: linear-gradient(135deg, #E8F8F5, #D1F2EB);
    border: 3px solid var(--accent-green);
    border-radius: 20px;
    padding: 30px;
    margin: 25px 0;
}

.recommendation-title {
    font-family: 'Caveat', cursive;
    font-size: 1.6rem;
    color: var(--accent-green);
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 10px;
}
```

### Problem Box

```css
.problem-box {
    background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
    border: 3px dashed var(--accent-red);
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
}

.problem-title {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.3rem;
    color: var(--accent-red);
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}
```

### Hand-Drawn Border Style

Apply this border-radius for the hand-drawn/sketchy look:

```css
.hand-drawn {
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
}
```

### Component Box (Three in a Row)

```css
.three-components {
    display: flex;
    gap: 15px;
    margin: 30px 0;
    flex-wrap: wrap;
}

.component-box {
    flex: 1;
    min-width: 220px;
    padding: 25px 20px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    text-align: center;
    transition: all 0.35s ease;
    cursor: pointer;
    border: 3px solid var(--pencil);
}

.component-box:hover { transform: scale(1.03); }

.component-icon { font-size: 2.5rem; margin-bottom: 10px; }
.component-title { font-family: 'Patrick Hand', cursive; font-size: 1.4rem; font-weight: 700; margin-bottom: 8px; }
.component-desc { font-size: 0.9rem; color: var(--text-muted); }
```

### Flow Item

```css
.flow-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin: 25px 0;
    flex-wrap: wrap;
}

.flow-item {
    padding: 12px 20px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    border: 2px solid var(--pencil);
    font-family: 'Patrick Hand', cursive;
    font-size: 1rem;
    background: var(--bg-paper);
}

.flow-arrow { font-size: 1.5rem; color: var(--accent-lavender); }
```

### Metaphor Box (Visual Comparison)

```css
.visual-metaphor {
    background: linear-gradient(135deg, #F8F4FF, #E8F8F5);
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    padding: 30px;
    margin: 25px 0;
    border: 2px dashed var(--accent-lavender);
}

.metaphor-visual { display: flex; gap: 30px; justify-content: center; flex-wrap: wrap; margin: 25px 0; }

.metaphor-box {
    flex: 1;
    min-width: 280px;
    max-width: 380px;
    padding: 28px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    transition: transform 0.3s;
    border: 3px solid var(--pencil);
}

.metaphor-box:hover { transform: scale(1.02) rotate(1deg); }

.metaphor-icon { font-size: 3.5rem; text-align: center; margin-bottom: 15px; }
.metaphor-label { font-family: 'Caveat', cursive; font-size: 1.7rem; text-align: center; margin-bottom: 12px; }
.metaphor-example { font-size: 0.95rem; color: var(--text-muted); text-align: center; font-style: italic; line-height: 1.6; }
```

### Memory Circle (Interactive)

```css
.memory-circles {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    margin: 30px 0;
    flex-wrap: wrap;
}

.memory-circle {
    width: 110px;
    height: 110px;
    border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 3px solid var(--pencil);
    transition: all 0.3s;
    cursor: pointer;
    text-align: center;
    padding: 8px;
}

.memory-circle:hover { transform: scale(1.1); }

.memory-circle.working { background: linear-gradient(145deg, #E3F2FD, #BBDEFB); }
.memory-circle.episodic { background: linear-gradient(145deg, #FFEBEE, #FFCDD2); }
.memory-circle.semantic { background: linear-gradient(145deg, #E8F5E9, #C8E6C9); }
.memory-circle.procedural { background: linear-gradient(145deg, #FFF3E0, #FFE0B2); }

.memory-circle i { font-size: 1.5rem; margin-bottom: 3px; }
.memory-circle span { font-family: 'Patrick Hand', cursive; font-size: 1rem; font-weight: 700; }
```

### Process Circle (Step Flow)

```css
.process-flow {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin: 30px 0;
    flex-wrap: wrap;
}

.process-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.process-circle {
    width: 80px;
    height: 80px;
    border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    color: white;
    transition: transform 0.3s;
    cursor: pointer;
    border: 3px solid var(--pencil);
    box-shadow: 3px 4px 0 rgba(0,0,0,0.15);
}

.process-circle:hover { transform: scale(1.1) rotate(-3deg); }

.process-label { font-family: 'Patrick Hand', cursive; font-size: 1rem; color: var(--text-muted); }
```

### Action Card

```css
.action-card {
    background: linear-gradient(135deg, #F8F5FF, #F0FFFA);
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    padding: 28px;
    margin: 22px 0;
    border: 3px solid var(--accent-lavender);
    transition: all 0.3s;
}

.action-card:hover { border-color: var(--accent-coral); transform: rotate(0.5deg); }

.action-title { font-family: 'Patrick Hand', cursive; font-size: 1.4rem; margin-bottom: 15px; display: flex; align-items: center; gap: 12px; }

.action-number {
    width: 32px;
    height: 32px;
    background: var(--accent-coral);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.9rem;
    border: 2px solid var(--pencil);
}
```

### Badge (Small Tag)

```css
.badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 6px;
    border: 2px solid;
}

.badge-red { background: #FFE8E8; color: #D63031; border-color: #D63031; }
.badge-green { background: #E8FAF4; color: #00B894; border-color: #00B894; }
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

### Critique Box

```css
.critique-box {
    background: linear-gradient(135deg, #FFF5F5, #FFEBEE);
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    padding: 20px;
    margin: 20px 0;
    border-left: 5px solid var(--accent-coral);
}

.critique-title {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.2rem;
    color: var(--accent-coral);
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}
```

### Real World Example

```css
.real-world-example {
    background: linear-gradient(135deg, #FFF0F5, #F0F8FF);
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    padding: 24px;
    margin: 18px 0;
    border: 2px dashed var(--accent-coral);
}

.example-label { font-family: 'Patrick Hand', cursive; font-size: 1.15rem; color: var(--accent-coral); margin-bottom: 10px; }
```

### Tooltip

```css
.tooltip { position: relative; display: inline-block; cursor: help; border-bottom: 2px dotted var(--accent-teal); }
.tooltip::after {
    content: attr(data-tip);
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    background: var(--pencil);
    color: white;
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 0.8rem;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
    z-index: 10;
}
.tooltip:hover::after { opacity: 1; }
```

### Divider

```css
.divider { text-align: center; margin: 45px 0; }
.divider::before { 
    content: '~~~~~~~'; 
    font-family: 'Caveat', cursive;
    font-size: 1.5rem; 
    color: var(--accent-lavender); 
    letter-spacing: 10px; 
}
```

### Strategy Card (Grid Layout)

```css
.strategy-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    margin: 25px 0;
}

.strategy-card {
    background: var(--bg-paper);
    padding: 25px 20px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    border: 3px solid var(--pencil);
    transition: all 0.35s ease;
    cursor: pointer;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.strategy-card:hover {
    transform: scale(1.03) rotate(1deg);
    box-shadow: 4px 5px 0 rgba(0,0,0,0.1);
}

.strategy-num {
    width: 32px;
    height: 32px;
    background: var(--accent-coral);
    color: white;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.95rem;
    margin-bottom: 12px;
    border: 2px solid var(--pencil);
}

.strategy-title {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.25rem;
    margin-bottom: 8px;
    font-weight: 700;
}

.strategy-card i {
    font-size: 2.2rem;
    margin-bottom: 12px;
}
```

### Checklist

```css
.checklist { list-style: none; padding: 0; margin: 18px 0; }
.checklist li { padding: 12px 0; padding-left: 38px; position: relative; border-bottom: 2px dashed rgba(0,0,0,0.1); }
.checklist li::before { 
    content: '\f00c'; 
    font-family: 'Font Awesome 6 Free'; 
    font-weight: 900; 
    position: absolute; 
    left: 0; 
    font-size: 1rem; 
    color: var(--accent-teal); 
}
```

### Code Snippet

```css
.code-snippet {
    background: #1E272E;
    color: #C8D6E5;
    padding: 16px 20px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    font-family: 'Courier New', monospace;
    font-size: 0.85rem;
    margin: 14px 0;
    overflow-x: auto;
    border: 2px solid #343D46;
}
```

### Problem Box

```css
.problem-box {
    background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
    border: 3px dashed var(--accent-red);
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
}

.problem-title {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.3rem;
    color: var(--accent-red);
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}
```

### Analogy Box

```css
.analogy-box {
    background: linear-gradient(135deg, #FFF8E1, #FFECB3);
    border: 3px dashed var(--accent-orange);
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    text-align: center;
}

.analogy-title {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.3rem;
    color: var(--accent-orange);
    margin-bottom: 10px;
}
```

### Back Link

```css
.back-link {
    display: inline-block;
    color: var(--accent-teal);
    font-family: 'Patrick Hand', cursive;
    font-size: 1.1rem;
    text-decoration: none;
    margin-bottom: 30px;
    transition: color 0.3s;
}
.back-link:hover { color: var(--accent-coral); }
```

### TOC Auto-Highlight (Scroll Spy)

For pages with sidebar navigation, add this CSS and JavaScript to highlight the current section:

```css
.toc-list a.active {
    background: rgba(255, 107, 107, 0.15);
    border-left-color: var(--accent-coral);
    font-weight: 600;
}
```

JavaScript:
```html
<script>
    const sections = document.querySelectorAll('section[id]');
    const tocLinks = document.querySelectorAll('.toc-list a');

    function highlightToc() {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.scrollY >= sectionTop - 150) {
                current = section.getAttribute('id');
            }
        });

        tocLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    }

    window.addEventListener('scroll', highlightToc);
    highlightToc();
</script>
```

Note: Each section must have an `id` attribute (e.g., `<section id="overview">`)

### Feature List with Checkmarks

```css
.feature-list {
    list-style: none;
    padding: 0;
    margin: 15px 0;
}

.feature-list li {
    padding: 8px 0 8px 30px;
    position: relative;
}

.feature-list li::before {
    content: '\f00c';
    font-family: 'Font Awesome 6 Free', sans-serif;
    font-weight: 900;
    position: absolute;
    left: 0;
    color: var(--accent-teal);
}
```

## Utility Classes

### Text Highlights

```css
.highlight { 
    background: linear-gradient(180deg, transparent 65%, rgba(255, 230, 109, 0.5) 65%); 
}

.highlight-teal { 
    background: linear-gradient(180deg, transparent 65%, rgba(78, 205, 196, 0.35) 65%); 
}

.highlight-coral { 
    background: linear-gradient(180deg, transparent 65%, rgba(255, 107, 107, 0.35) 65%); 
}
```

Usage:
```html
<span class="highlight">highlighted text</span>
<span class="highlight-teal">teal highlight</span>
<span class="highlight-coral">coral highlight</span>
```

## Footer

```css
footer {
    text-align: center;
    padding: 30px;
    color: var(--text-muted);
    font-family: 'Patrick Hand', cursive;
}
```

## Scroll Reveal Animation

Add this JavaScript for smooth scroll reveal:

```html
<script>
    const revealElements = document.querySelectorAll('.reveal');
    const revealOnScroll = () => {
        revealElements.forEach(el => {
            const elementTop = el.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            if (elementTop < windowHeight - 50) { el.classList.add('visible'); }
        });
    };
    window.addEventListener('scroll', revealOnScroll);
    window.addEventListener('load', revealOnScroll);
</script>
```

Add this CSS:

```css
.reveal { opacity: 0; transform: translateY(30px); transition: all 0.7s ease; }
.reveal.visible { opacity: 1; transform: translateY(0); }
```

Add `class="reveal"` to sections you want to animate:

```html
<section class="card reveal">
    <!-- content -->
</section>
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
        /* Include CSS variables and styles from above */
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Back to Mind & Machine</a>
        
        <header>
            <h1>Page Title</h1>
            <p class="subtitle">Subtitle goes here</p>
            <p style="margin-top: 20px; font-size: 0.9rem; color: var(--text-muted);">
                <i class="fa-solid fa-user"></i> Jiuhe Wang &nbsp;&nbsp;|&nbsp;&nbsp; 
                <i class="fa-regular fa-calendar"></i> Created: Feb 21, 2026
            </p>
        </header>

        <section class="card reveal">
            <h2><i class="fa-solid fa-icon-name fa-icon"></i>Section Title</h2>
            <!-- content -->
        </section>

        <footer>
            <p><i class="fa-solid fa-paintbrush"></i> Mind & Machine | <a href="index.html">Back to Home</a></p>
        </footer>
    </div>

    <script>
        /* Include reveal script from above */
    </script>
</body>
</html>
```

## Common Font Awesome Icons

### General
- `fa-solid fa-shield-halved` - Security
- `fa-solid fa-layer-group` - Overview/Layers
- `fa-solid fa-list-check` - Checklist/Requirements
- `fa-solid fa-scale-balanced` - Comparison/Balance
- `fa-solid fa-trophy` - Recommendation/Award
- `fa-solid fa-flag-checkered` - Conclusion/Finish
- `fa-solid fa-arrow-left` - Back navigation
- `fa-solid fa-arrow-right` - Forward/Flow
- `fa-solid fa-paintbrush` - Footer/Artistic
- `fa-solid fa-box-open` - Package/Sandbox
- `fa-solid fa-fire` - Firecracker
- `fa-solid fa-glasses` - gVisor
- `fa-brands fa-docker` - Docker
- `fa-brands fa-python` - Python
- `fa-solid fa-check` - Checkmark
- `fa-solid fa-xmark` - Error/Bad
- `fa-solid fa-star` - Star/Recommendation
- `fa-solid fa-lightbulb` - Idea

### Medical/Hospital Theme
- `fa-solid fa-user-md` - Doctor/Expert
- `fa-solid fa-hospital` - Hospital/System
- `fa-solid fa-heart` - Heart/Heart specialist
- `fa-solid fa-brain` - Brain/Brain specialist
- `fa-solid fa-bone` - Bone/Bone specialist
- `fa-solid fa-hand` - Hand/Hand specialist
- `fa-solid fa-child` - Child/Kids specialist
- `fa-solid fa-user-injured` - Patient
- `fa-solid fa-crown` - Superstar/Best
- `fa-solid fa-moon` - Sleeping/Idle
- `fa-solid fa-spider` - Cobweb/Unused
- `fa-solid fa-leaf` - Dust/Idle

### Components & Features
- `fa-solid fa-circle-question` - Question/Big Question
- `fa-solid fa-puzzle-piece` - Component/Puzzle
- `fa-solid fa-code` - Code/Technical
- `fa-solid fa-mask` - Illusion
- `fa-solid fa-magnifying-glass` - Search/Investigate
- `fa-solid fa-file-lines` - Document/Read
- `fa-solid fa-hammer` - Tool/Action
- `fa-solid fa-rotate` - Repeat/Cycle
- `fa-solid fa-folder-open` - Open folder/Storage
- `fa-solid fa-wifi` - Network/Connected
- `fa-solid fa-bicycle` - Learning/Skill
- `fa-solid fa-cloud` - Knowledge/Cloud
- `fa-solid fa-gear` - Procedural/Settings
- `fa-solid fa-clipboard` - Working memory/Clipboard
- `fa-solid fa-film` - Episodic/History
- `fa-solid fa-book` - Semantic/Knowledge
- `fa-solid fa-clock-rotate-left` - Past experience
- `fa-solid fa-wrench` - Skills/Tools

### Status & Indicators
- `fa-solid fa-triangle-exclamation` - Warning/Problem
- `fa-solid fa-server` - GPU/Server
- `fa-solid fa-truck-loading` - Slow/Transport
- `fa-solid fa-building` - Building/GPU group
- `fa-solid fa-building-user` - Local building
- `fa-solid fa-calculator` - Calculation/Math
- `fa-solid fa-chart-line` - Chart/Growth
- `fa-solid fa-chart-simple` - Chart/Overview
- `fa-solid fa-rocket` - Launch/Start
- `fa-solid fa-bullseye` - Target/Goal
- `fa-solid fa-sliders` - Settings/Adjust
- `fa-solid fa-bolt` - Speed/Fast
- `fa-solid fa-stopwatch` - Timing
- `fa-solid fa-repeat` - Replication
- `fa-solid fa-plus` - Addition/More

## Adding New Pages to Index

When creating a new page, you **MUST** add it to `index.html` so users can discover it.

### Link Card Structure

Add a new `<a>` element inside the `<div class="links">` container in `index.html`:

```html
<a href="page-name.html" class="link-card" data-tags="tag1,tag2" data-date="2025-02-21" data-title="Page Title">
    <div class="link-icon" style="background: var(--accent-color);"><i class="fa-solid fa-icon-name"></i></div>
    <div class="link-text">
        <h2>Page Title <span class="tag new">New</span></h2>
        <p>Short description of the page content</p>
        <div class="link-meta">
            <span class="link-date"><i class="fa-regular fa-calendar"></i> Feb 21, 2025</span>
            <div class="link-tags">
                <span class="tag tag-name">Tag</span>
            </div>
        </div>
    </div>
</a>
```

### Required Attributes

1. **href**: Must match the new HTML file name (e.g., `sandbox-solutions.html`)
2. **data-tags**: Comma-separated tags for filtering (e.g., `ai,architecture`)
3. **data-date**: Publication date in YYYY-MM-DD format
4. **data-title**: Title for sorting (use the main heading)

### Link Meta Section

Each card should include:
- **link-date**: Calendar icon with formatted date (e.g., "Feb 21, 2025")
- **link-tags**: Tags for filtering (ai, architecture, security, moe, agile)

### Available Tags

| Tag | Display Name | Color |
|-----|--------------|-------|
| ai | AI | coral (#FF6B6B) |
| architecture | Architecture | teal (#4ECDC4) |
| security | Security | orange (#E67E22) |
| moe | MoE | lavender (#C9B1FF) |
| agile | Agile | sunflower (#FFE66D) |

### Available Accent Colors

Choose a unique color for each page's icon:
- `var(--accent-coral)` - #FF6B6B
- `var(--accent-teal)` - #4ECDC4
- `var(--accent-sunflower)` - #FFE66D
- `var(--accent-lavender)` - #C9B1FF
- `var(--accent-sky)` - #A8E6CF
- `var(--accent-orange)` - #E67E22

### Icon Selection

Choose a Font Awesome icon that matches the content. Common icons:
- `fa-solid fa-brain` - AI/Intelligence
- `fa-solid fa-microchip` - Hardware/Architecture
- `fa-solid fa-shield-halved` - Security
- `fa-solid fa-rocket` - Launch/Agile
- `fa-solid fa-robot` - Agent/Robot
- `fa-solid fa-clipboard-question` - Study/Research

### Example

```html
<a href="opencode-multiple-choice-study.html" class="link-card" data-tags="ai,architecture" data-date="2025-02-21" data-title="OpenCode Multiple Choice Interaction">
    <div class="link-icon" style="background: var(--accent-sky);"><i class="fa-solid fa-clipboard-question"></i></div>
    <div class="link-text">
        <h2>OpenCode Multiple Choice Interaction <span class="tag new">New</span></h2>
        <p>Deep dive into how the plan agent implements user interaction with multiple choice questions</p>
        <div class="link-meta">
            <span class="link-date"><i class="fa-regular fa-calendar"></i> Feb 21, 2025</span>
            <div class="link-tags">
                <span class="tag ai">AI</span>
                <span class="tag architecture">Architecture</span>
            </div>
        </div>
    </div>
</a>
```

### Checklist

- [ ] Page HTML file created
- [ ] Link added to `index.html` inside `<div class="links">`
- [ ] All required attributes set (`data-tags`, `data-date`, `data-title`)
- [ ] Appropriate icon and accent color selected
- [ ] Title and description written (description under 80 chars)
- [ ] "New" tag added for recent pages
- [ ] link-meta section with date and tags included

## Committing Changes

**IMPORTANT:** Commit each change immediately after it's completed.

### Why?
- Keeps the git history clean and granular
- Makes it easy to revert specific changes
- Provides clear documentation of what was done
- Prevents losing work

### Commit Process

1. **After completing any task**, immediately commit the changes:

```bash
# Check what files changed
git status

# Stage and commit
git add -A
git commit -m "Descriptive commit message explaining the change"
```

2. **Write good commit messages**:
   - Use present tense ("Add feature" not "Added feature")
   - Be descriptive but concise
   - Reference what was changed and why
   - For complex changes, use multi-line commits:

```bash
git commit -m "Add isolation hierarchy visualization to sandbox page

- Add stepped pyramid showing 5 isolation levels
- Include architecture diagrams for all 5 solutions
- Add security strength meters with color coding
- Use visual hierarchy to show VM > Kernel > Container > Process > Language"
```

3. **Commit message examples**:
   - ✅ "Remove spider web decorations from idle doctors"
   - ✅ "Add new page: sandbox-solutions.html with security comparisons"
   - ✅ "Update index.html with date filtering and tag system"
   - ❌ "Fix stuff"
   - ❌ "Update"
   - ❌ "Changes"

### Commit Checklist

- [ ] Changes are complete and tested
- [ ] Commit message describes what was done
- [ ] Files are properly staged
- [ ] Commit succeeded without errors
