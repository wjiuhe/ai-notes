# Mind & Machine - Style Guide

This document provides the CSS styling conventions used across the Mind & Machine website.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Common CSS Variables](#common-css-variables)
3. [External Dependencies](#external-dependencies)
4. [Hand-Drawn Style System](#hand-drawn-style-system)
5. [CSS Organization](#css-organization)
6. [Base Styles](#base-styles)
7. [Typography](#typography)
8. [Components](#components)
9. [Utility Classes](#utility-classes)
10. [Scroll Reveal Animation](#scroll-reveal-animation)
11. [Complete HTML Template](#complete-html-template)
12. [Common Font Awesome Icons](#common-font-awesome-icons)
13. [Adding New Pages to Index](#adding-new-pages-to-index)
14. [Sidebar Table of Contents](#sidebar-table-of-contents)
15. [Dual-Theme System](#dual-theme-system-light-vs-dark)
16. [Content Page Rules](#content-page-rules)
17. [Committing Changes](#committing-changes)

## Claude Code Skills

The following reusable skills have been extracted from this codebase:

| Skill | Description | Use When |
|-------|-------------|----------|
| `dual-theme-web-system` | Parallel light/dark themes with CSS variables | Creating websites with multiple visual themes |
| `hand-drawn-css-components` | Sketchy, organic UI using pure CSS | Building notebook/doodle-style interfaces |
| `sidebar-toc-navigation` | Fixed sidebar with scroll spy | Documentation pages with section navigation |
| `filter-sort-card-grid` | Filterable/sortable card grid | Index pages with tag filtering and date sorting |

---

## Quick Start

For new pages, use this minimal template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&family=Nunito:wght@400;600;700&family=Patrick+Hand&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Page Title</h1>
            <p class="subtitle">Subtitle describing the page</p>
        </header>

        <section class="card reveal">
            <h2><i class="fa-solid fa-icon-name fa-icon"></i>Section Title</h2>
            <!-- content -->
        </section>
    </div>

    <script>
        // Scroll reveal
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
</body>
</html>
```

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

