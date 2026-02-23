---
name: hand-drawn-article-styling
description: |
  Create visually rich, hand-drawn style articles with card-based layouts, severity badges,
  layered visualizations, and structured content sections. Use when: (1) Building educational
  documentation with visual hierarchy, (2) Creating security/technical study guides,
  (3) Designing content with attack/defense patterns, risk levels, or structured data.
  Includes card components, badges, layered defenses, timelines, and tool displays.
author: Claude Code
version: 1.0.0
date: 2026-02-23
---

# Hand-Drawn Article Styling

## Problem
Technical documentation and educational content often lacks visual structure, making it hard to distinguish between different types of information (attacks vs defenses, severity levels, steps in a process).

## Solution
A hand-drawn security-themed design system with attack/defense cards, risk badges, and layered defense visualizations.

## Core Components

### 1. Attack Card

Shows vulnerability details with severity-based styling:

```css
.attack-card {
    background: var(--bg-paper);
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    padding: 20px;
    margin: 15px 0;
    border: 2px solid var(--pencil);
    transition: all 0.3s ease;
}

.attack-card:hover {
    transform: translateX(5px);
    box-shadow: 3px 4px 0 rgba(0,0,0,0.1);
}

/* Severity levels with colored left borders */
.attack-card.critical { border-left: 5px solid var(--accent-coral); }
.attack-card.high { border-left: 5px solid var(--accent-orange); }
.attack-card.medium { border-left: 5px solid var(--accent-sunflower); }
```

### 2. Attack Label (Category Badge)

```css
.attack-label {
    display: inline-block;
    font-family: 'Patrick Hand', cursive;
    font-size: 0.8rem;
    padding: 3px 10px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    margin-bottom: 10px;
    font-weight: 700;
}

/* Category colors */
.attack-label.direct { background: #FFCDD2; color: #C62828; }
.attack-label.indirect { background: #FFE0B2; color: #EF6C00; }
.attack-label.extraction { background: #E1BEE7; color: #7B1FA2; }
.attack-label.supply { background: #BBDEFB; color: #1565C0; }
.attack-label.poison { background: #C8E6C9; color: #2E7D32; }
.attack-label.output { background: #FFCDD2; color: #C62828; }
.attack-label.agency { background: #B3E5FC; color: #0277BD; }
.attack-label.rag { background: #F8BBD9; color: #C2185B; }
.attack-label.misinfo { background: #D7CCC8; color: #5D4037; }
.attack-label.resource { background: #FFE082; color: #F57F17; }
```

### 3. Risk Level Badge

```css
.risk-level {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 10px;
}

.risk-critical { background: #FFEBEE; color: #C62828; }
.risk-high { background: #FFF3E0; color: #EF6C00; }
.risk-medium { background: #FFFDE7; color: #F9A825; }
```

### 4. Defense Layers

Visual representation of layered security:

```css
.defense-layers {
    display: flex;
    gap: 15px;
    margin: 25px 0;
    flex-wrap: wrap;
}

.defense-layer {
    flex: 1;
    min-width: 130px;
    padding: 20px 12px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    text-align: center;
    border: 3px solid var(--pencil);
    transition: all 0.3s ease;
    position: relative;
}

/* Decorative underline */
.defense-layer::after {
    content: '';
    position: absolute;
    bottom: 8px;
    left: 50%;
    transform: translateX(-50%);
    width: 30px;
    height: 4px;
    background: currentColor;
    opacity: 0.3;
    border-radius: 2px;
}

.defense-layer:hover {
    transform: translateY(-8px) rotate(-2deg);
    box-shadow: 4px 8px 0 rgba(0,0,0,0.15);
}

/* Layer types with color coding */
.defense-layer.input {
    background: linear-gradient(180deg, #E3F2FD 0%, #BBDEFB 100%);
    border-color: #1976D2;
}

.defense-layer.process {
    background: linear-gradient(180deg, #FFF3E0 0%, #FFE0B2 100%);
    border-color: #F57C00;
}

.defense-layer.output {
    background: linear-gradient(180deg, #F3E5F5 0%, #E1BEE7 100%);
    border-color: #7B1FA2;
}

.defense-icon-large {
    font-size: 2.2rem;
    margin-bottom: 10px;
    display: inline-block;
    padding: 12px;
    border-radius: 50%;
    background: white;
    border: 2px solid currentColor;
    box-shadow: 2px 3px 0 rgba(0,0,0,0.1);
}

.defense-layer.input .defense-icon-large { color: #1565C0; }
.defense-layer.process .defense-icon-large { color: #E65100; }
.defense-layer.output .defense-icon-large { color: #6A1B9A; }

.defense-label {
    font-family: 'Patrick Hand', cursive;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-dark);
}

.defense-desc {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-top: 5px;
    line-height: 1.4;
}
```

### 5. Mitigation Card

```css
.mitigation-card {
    background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    padding: 20px;
    margin: 15px 0;
    border: 2px solid var(--accent-green);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

/* Decorative radial gradient */
.mitigation-card::before {
    content: '';
    position: absolute;
    top: -20px;
    right: -20px;
    width: 80px;
    height: 80px;
    background: radial-gradient(circle, rgba(39, 174, 96, 0.15) 0%, transparent 70%);
    border-radius: 50%;
}

.mitigation-card:hover {
    transform: scale(1.02);
    box-shadow: 4px 6px 0 rgba(0,0,0,0.1);
}

.mitigation-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 15px;
    padding-bottom: 12px;
    border-bottom: 2px dashed rgba(39, 174, 96, 0.3);
}

.mitigation-icon-large {
    width: 55px;
    height: 55px;
    background: linear-gradient(135deg, #27AE60, #2ECC71);
    color: white;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    border: 2px solid #1E8449;
    box-shadow: 2px 3px 0 rgba(0,0,0,0.15);
}

.mitigation-title-text {
    font-family: 'Caveat', cursive;
    font-size: 1.5rem;
    color: #1E8449;
    font-weight: 700;
}

.mitigation-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.mitigation-list li {
    padding: 8px 0 8px 32px;
    position: relative;
    font-size: 0.95rem;
    color: #33691E;
    border-bottom: 1px dashed rgba(39, 174, 96, 0.2);
}

.mitigation-list li:last-child {
    border-bottom: none;
}

.mitigation-list li::before {
    content: '\f00c';
    font-family: 'Font Awesome 6 Free', sans-serif;
    font-weight: 900;
    position: absolute;
    left: 0;
    color: #27AE60;
    font-size: 0.9rem;
}
```

### 6. Timeline Component

```css
.timeline-item {
    position: relative;
    padding-left: 40px;
    margin: 20px 0;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: 15px;
    top: 8px;
    width: 12px;
    height: 12px;
    background: var(--accent-coral);
    border: 2px solid var(--pencil);
    border-radius: 50%;
    transform: rotate(5deg);
}

.timeline-item::after {
    content: '';
    position: absolute;
    left: 20px;
    top: 25px;
    width: 2px;
    height: calc(100% + 10px);
    background: repeating-linear-gradient(
        to bottom,
        var(--pencil) 0px,
        var(--pencil) 5px,
        transparent 5px,
        transparent 10px
    );
    opacity: 0.3;
}

.timeline-item:last-child::after {
    display: none;
}
```

### 7. Tool Badge

```css
.tool-badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    font-size: 0.75rem;
    font-weight: 600;
    margin: 2px;
    border: 1px solid;
}

.tool-badge.promptfoo { background: #FFE082; color: #F57F17; border-color: #FFB300; }
.tool-badge.garak { background: #80DEEA; color: #0097A7; border-color: #00ACC1; }
.tool-badge.lakera { background: #CE93D8; color: #7B1FA2; border-color: #8E24AA; }
.tool-badge.rebuff { background: #A5D6A7; color: #388E3C; border-color: #4CAF50; }
```

### 8. Decorative Elements

```css
/* Corner accent for visual interest */
.corner-accent {
    position: absolute;
    top: -10px;
    right: -10px;
    width: 40px;
    height: 40px;
    border-top: 3px solid var(--accent-coral);
    border-right: 3px solid var(--accent-coral);
    border-radius: 0 15px 0 0;
    opacity: 0.6;
}

/* Wavy divider */
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

/* Sketchy badge variations */
.sketchy-badge {
    display: inline-block;
    padding: 6px 16px;
    font-family: 'Patrick Hand', cursive;
    font-size: 0.9rem;
    font-weight: 700;
    border: 2px solid var(--pencil);
    margin: 5px;
    transition: all 0.3s ease;
}

.sketchy-badge:hover {
    transform: rotate(-3deg) scale(1.05);
}

.sketchy-badge.rounded {
    border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
}
```

## Usage Example

```html
<section class="card" id="vulnerability" style="position: relative;">
    <div class="corner-accent"></div>

    <h2>
        <i class="fa-solid fa-bug fa-icon" style="color: var(--accent-coral);"></i>
        Vulnerability Name
        <span class="risk-level risk-critical">Critical</span>
    </h2>

    <div class="attack-card critical">
        <div class="attack-label direct"><i class="fa-solid fa-bolt"></i> Direct Attack</div>
        <div class="attack-title">Attack Name</div>
        <div class="attack-example">Example payload or attack code</div>
    </div>

    <h4><i class="fa-solid fa-route"></i> Defense Flow</h4>
    <div class="defense-layers">
        <div class="defense-layer input">
            <div class="defense-icon-large"><i class="fa-solid fa-filter"></i></div>
            <div class="defense-label">Input Filter</div>
            <div class="defense-desc">Clean inputs</div>
        </div>
        <div class="defense-layer process">
            <div class="defense-icon-large"><i class="fa-solid fa-ghost"></i></div>
            <div class="defense-label">Validation</div>
            <div class="defense-desc">Check patterns</div>
        </div>
        <div class="defense-layer output">
            <div class="defense-icon-large"><i class="fa-solid fa-check-double"></i></div>
            <div class="defense-label">Output Check</div>
            <div class="defense-desc">Final filter</div>
        </div>
    </div>

    <div class="mitigation-card">
        <div class="mitigation-header">
            <div class="mitigation-icon-large"><i class="fa-solid fa-shield-cat"></i></div>
            <div class="mitigation-title-text">Best Practices</div>
        </div>
        <ul class="mitigation-list">
            <li>Implement input validation</li>
            <li>Use parameterized queries</li>
            <li>Monitor for suspicious patterns</li>
        </ul>
    </div>
</section>
```

## Key Styling Tips

1. **Hand-drawn feel**: Use `border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px` for organic shapes

2. **Visual hierarchy**:
   - Critical attacks: coral/red border
   - High attacks: orange border
   - Medium attacks: yellow border

3. **Hover interactions**: Slight transforms add life:
   ```css
   .card:hover { transform: translateX(5px); }
   .defense-layer:hover { transform: translateY(-8px) rotate(-2deg); }
   ```

4. **Dashed borders**: Use for "attack" or "problem" elements to differentiate from solid "solution" elements

5. **Decorative corners**: Add `.corner-accent` to cards for visual interest

6. **Sketched dividers**: Use wavy/tilde dividers instead of straight lines

7. **Layer depth**: Use different background gradients to show defense layers (input/process/output)

8. **Check marks**: Mitigation lists use checkmark icons instead of bullets
