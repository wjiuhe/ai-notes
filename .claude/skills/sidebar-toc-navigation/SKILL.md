---
name: sidebar-toc-navigation
description: |
  Implement a sidebar table of contents with scroll spy highlighting and smooth scrolling.
  Use when: (1) Creating documentation pages with section navigation, (2) Building long-form
  content with jump links, (3) Implementing documentation sites with persistent navigation.
  Includes mobile-responsive toggle, grouped sections, and active state highlighting.
author: Claude Code
version: 1.0.0
date: 2026-02-23
---

# Sidebar TOC Navigation

## Problem
Long-form content pages need persistent, contextual navigation that highlights the current section and allows quick jumps to content.

## Solution
A fixed sidebar with scroll spy functionality, grouped sections, and mobile-responsive design.

## HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page with Sidebar TOC</title>
    <!-- Mobile toggle button -->
    <button class="toc-toggle" id="tocToggle" aria-label="Toggle navigation">
        <i class="fa-solid fa-bars"></i>
    </button>

    <div class="page-wrapper">
        <!-- Sidebar Table of Contents -->
        <nav class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-title">Page Title</div>
                <div class="sidebar-subtitle">Navigation</div>
            </div>

            <div class="toc-section">
                <div class="toc-title">
                    <i class="fa-solid fa-layer-group"></i> Overview
                </div>
                <ul class="toc-list">
                    <li><a href="#introduction" onclick="scrollToSection('introduction')">1. Introduction</a></li>
                    <li><a href="#overview" onclick="scrollToSection('overview')">2. Overview</a></li>
                </ul>
            </div>

            <div class="toc-section">
                <div class="toc-title">
                    <i class="fa-solid fa-code"></i> Technical
                </div>
                <ul class="toc-list">
                    <li><a href="#implementation" onclick="scrollToSection('implementation')">3. Implementation</a></li>
                    <li><a href="#examples" onclick="scrollToSection('examples')">4. Examples</a></li>
                </ul>
            </div>

            <div class="toc-section" style="margin-top: 25px; padding-top: 18px; border-top: 2px dashed rgba(0,0,0,0.1);">
                <a href="index.html" style="display: flex; align-items: center; gap: 8px; color: var(--accent-teal); text-decoration: none; font-weight: 600; font-family: 'Patrick Hand', cursive;">
                    <i class="fa-solid fa-arrow-left"></i> Back to Home
                </a>
            </div>
        </nav>

        <!-- Main Content -->
        <main class="main-content">
            <div class="container">
                <header>
                    <h1>Page Title</h1>
                    <p class="subtitle">Subtitle describing the page</p>
                </header>

                <section class="card" id="introduction">
                    <h2><i class="fa-solid fa-icon-name fa-icon"></i>1. Introduction</h2>
                    <!-- content -->
                </section>

                <section class="card" id="overview">
                    <h2><i class="fa-solid fa-icon-name fa-icon"></i>2. Overview</h2>
                    <!-- content -->
                </section>

                <!-- More sections... -->
            </div>
        </main>
    </div>

    <script>
        // Smooth scroll to section
        function scrollToSection(id) {
            const element = document.getElementById(id);
            if (element) {
                const offset = 30;
                const elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
                window.scrollTo({ top: elementPosition - offset, behavior: 'smooth' });
            }
        }

        // Scroll spy for TOC highlighting
        const sections = document.querySelectorAll('.card[id]');
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

        // Mobile TOC toggle
        const tocToggle = document.getElementById('tocToggle');
        const sidebar = document.getElementById('sidebar');

        if (tocToggle && sidebar) {
            tocToggle.addEventListener('click', () => {
                sidebar.classList.toggle('open');
            });

            // Close sidebar when clicking on a link (mobile)
            tocLinks.forEach(link => {
                link.addEventListener('click', () => {
                    sidebar.classList.remove('open');
                });
            });
        }
    </script>
</body>
</html>
```

## CSS Styles

```css
/* ================================
   PAGE WRAPPER
   ================================ */
.page-wrapper {
  display: flex;
  max-width: 1400px;
  margin: 0 auto;
  position: relative;
}

/* ================================
   SIDEBAR TOC STYLES
   ================================ */
.sidebar {
  width: 280px;
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  background: linear-gradient(180deg, var(--bg-paper) 0%, #F8F4EF 100%);
  border-right: 3px solid var(--pencil);
  padding: 30px 20px;
  overflow-y: auto;
  z-index: 100;
  box-shadow: 3px 0 10px rgba(0,0,0,0.1);
}

.sidebar-header {
  text-align: center;
  margin-bottom: 25px;
  padding-bottom: 20px;
  border-bottom: 2px dashed rgba(0,0,0,0.15);
}

.sidebar-title {
  font-family: 'Caveat', cursive;
  font-size: 1.6rem;
  color: var(--pencil);
  margin-bottom: 5px;
}

.sidebar-subtitle {
  font-family: 'Patrick Hand', cursive;
  font-size: 0.85rem;
  color: var(--text-muted);
}

.toc-section {
  margin-bottom: 18px;
}

.toc-title {
  font-family: 'Patrick Hand', cursive;
  font-size: 0.95rem;
  color: var(--pencil);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
}

.toc-list {
  list-style: none;
  padding-left: 0;
}

.toc-list li {
  margin-bottom: 4px;
}

.toc-list a {
  display: block;
  padding: 5px 10px;
  color: var(--text-dark);
  text-decoration: none;
  font-size: 0.85rem;
  border-radius: 8px;
  transition: all 0.2s ease;
  border-left: 3px solid transparent;
}

.toc-list a:hover {
  background: rgba(78, 205, 196, 0.15);
  border-left-color: var(--accent-teal);
  transform: translateX(3px);
}

.toc-list a.active {
  background: rgba(255, 107, 107, 0.15);
  border-left-color: var(--accent-coral);
  font-weight: 600;
}

/* ================================
   MAIN CONTENT
   ================================ */
.main-content {
  margin-left: 280px;
  flex: 1;
  padding: 40px 40px;
  max-width: calc(100vw - 320px);
  min-width: 0;
}

.container {
  max-width: 100%;
  margin: 0 auto;
}

/* ================================
   MOBILE TOC TOGGLE
   ================================ */
.toc-toggle {
  display: none;
  position: fixed;
  top: 20px;
  left: 20px;
  z-index: 200;
  background: var(--accent-coral);
  color: white;
  border: none;
  padding: 12px 15px;
  border-radius: 50%;
  font-size: 1.2rem;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

/* ================================
   RESPONSIVE BREAKPOINTS
   ================================ */
@media (max-width: 1200px) {
  .sidebar {
    transform: translateX(-100%);
    transition: transform 0.3s ease;
  }

  .sidebar.open {
    transform: translateX(0);
  }

  .sidebar.open .sidebar-header {
    padding-top: 60px;
  }

  .main-content {
    margin-left: 0;
    padding: 40px 20px;
    max-width: 100%;
  }

  .toc-toggle {
    display: block;
  }

  .back-link {
    margin-top: 50px;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 20px 15px;
  }

  h1 {
    font-size: 2.2rem;
  }

  h2 {
    font-size: 1.6rem;
  }
}
```

## Usage Notes

### Section IDs

Each section must have an `id` attribute matching the TOC href:

```html
<section class="card" id="introduction">
    <h2>Introduction</h2>
    <!-- content -->
</section>
```

### Smooth Scroll Offset

The `scrollToSection` function includes an offset to account for fixed headers:

```javascript
const offset = 30; // Adjust based on your fixed header height
const elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
window.scrollTo({ top: elementPosition - offset, behavior: 'smooth' });
```

### Scroll Spy Threshold

The `highlightToc` function uses a 150px threshold to determine the active section:

```javascript
if (window.scrollY >= sectionTop - 150) {
    current = section.getAttribute('id');
}
```

Adjust this value based on your layout needs.

## Accessibility

- The mobile toggle button has an `aria-label` for screen readers
- Sidebar has proper `z-index` to overlay content on mobile
- Active states are clearly indicated with color and border changes
- Hover states provide visual feedback on interactive elements
