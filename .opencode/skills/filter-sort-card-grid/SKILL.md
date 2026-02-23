---
name: filter-sort-card-grid
description: |
  Implement a filterable and sortable card grid with data attributes for content organization.
  Use when: (1) Creating index pages with many items, (2) Building portfolio galleries,
  (3) Organizing articles/projects with tags and dates. Supports tag filtering, date/title sorting,
  and bidirectional sort direction.
author: Claude Code
version: 1.0.0
date: 2026-02-23
---

# Filter and Sort Card Grid

## Problem
Index pages with many items need intuitive filtering and sorting to help users find content quickly.

## Solution
A card grid with data attributes for filtering and sorting, with a control bar for user interaction.

## HTML Structure

```html
<!-- Filter and Sort Controls -->
<div class="controls-bar">
    <div class="filter-group">
        <span class="control-label">Filter:</span>
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="ai">AI</button>
        <button class="filter-btn" data-filter="architecture">Architecture</button>
        <button class="filter-btn" data-filter="security">Security</button>
    </div>

    <div class="sort-group">
        <span class="control-label">Sort:</span>
        <button class="sort-btn active" data-sort="date" data-direction="desc">
            Date <i class="fa-solid fa-arrow-down"></i>
        </button>
        <button class="sort-btn" data-sort="title" data-direction="asc">
            Title <i class="fa-solid fa-arrow-up"></i>
        </button>
    </div>
</div>

<!-- Card Grid -->
<div class="cards-grid" id="cardsGrid">
    <a href="page1.html" class="card-item" data-tags="ai,architecture" data-date="2026-02-20" data-title="AI Architecture Deep Dive">
        <div class="card-icon" style="background: var(--accent-coral);">
            <i class="fa-solid fa-brain"></i>
        </div>
        <div class="card-content">
            <h3>AI Architecture Deep Dive</h3>
            <p>Exploring the architecture of modern AI systems.</p>
            <div class="card-meta">
                <span class="card-date"><i class="fa-regular fa-calendar"></i> Feb 20, 2026</span>
                <div class="card-tags">
                    <span class="tag">AI</span>
                    <span class="tag">Architecture</span>
                </div>
            </div>
        </div>
    </a>

    <!-- More cards... -->
</div>
```

## CSS Styles

```css
/* ================================
   CONTROLS BAR
   ================================ */
.controls-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
  background: var(--bg-paper);
  border-radius: 12px;
  margin-bottom: 30px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.control-label {
  font-family: 'Patrick Hand', cursive;
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-right: 8px;
}

.filter-group,
.sort-group {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.filter-btn,
.sort-btn {
  padding: 6px 14px;
  border: 2px solid var(--pencil);
  background: var(--bg-cream);
  border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
  font-family: 'Patrick Hand', cursive;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover,
.sort-btn:hover {
  background: var(--accent-teal);
  color: white;
  transform: translateY(-2px);
}

.filter-btn.active,
.sort-btn.active {
  background: var(--accent-coral);
  color: white;
  border-color: var(--pencil);
}

/* ================================
   CARDS GRID
   ================================ */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 25px;
}

.card-item {
  display: flex;
  gap: 20px;
  padding: 25px;
  background: var(--bg-paper);
  border: 2px solid var(--pencil);
  border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
  text-decoration: none;
  color: var(--text-dark);
  transition: all 0.3s ease;
  box-shadow: 3px 4px 0 rgba(0,0,0,0.1);
}

.card-item:hover {
  transform: translateY(-5px) rotate(1deg);
  box-shadow: 5px 8px 0 rgba(0,0,0,0.15);
  border-color: var(--accent-coral);
}

.card-item.hidden {
  display: none;
}

.card-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: white;
  flex-shrink: 0;
}

.card-content {
  flex: 1;
  min-width: 0;
}

.card-content h3 {
  font-family: 'Caveat', cursive;
  font-size: 1.5rem;
  margin-bottom: 8px;
  color: var(--pencil);
}

.card-content p {
  font-size: 0.95rem;
  color: var(--text-muted);
  margin-bottom: 15px;
  line-height: 1.5;
}

.card-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

.card-date {
  font-size: 0.85rem;
  color: var(--text-muted);
  font-family: 'Patrick Hand', cursive;
}

.card-tags {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
}

.tag {
  padding: 3px 10px;
  border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
  font-size: 0.75rem;
  font-family: 'Patrick Hand', cursive;
  background: var(--bg-cream);
  border: 1px solid var(--pencil);
}

/* Responsive */
@media (max-width: 768px) {
  .cards-grid {
    grid-template-columns: 1fr;
  }

  .card-item {
    flex-direction: column;
    align-items: flex-start;
  }

  .card-icon {
    width: 50px;
    height: 50px;
    font-size: 1.2rem;
  }
}
```

## JavaScript Implementation

```javascript
// State
currentFilter = 'all';
currentSort = 'date';
currentDirection = 'desc';

// DOM Elements
const cardsGrid = document.getElementById('cardsGrid');
const filterBtns = document.querySelectorAll('.filter-btn');
const sortBtns = document.querySelectorAll('.sort-btn');

// Filter functionality
filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    // Update active state
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    // Apply filter
    currentFilter = btn.dataset.filter;
    applyFiltersAndSort();
  });
});

// Sort functionality
sortBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const sortType = btn.dataset.sort;

    // Toggle direction if clicking same sort
    if (currentSort === sortType) {
      currentDirection = currentDirection === 'asc' ? 'desc' : 'asc';
    } else {
      currentSort = sortType;
      currentDirection = 'desc'; // Default to newest first for dates
    }

    // Update active state
    sortBtns.forEach(b => {
      b.classList.remove('active');
      if (b.dataset.sort === currentSort) {
        b.classList.add('active');
      }
    });

    // Update icon direction
    sortBtns.forEach(b => {
      const icon = b.querySelector('i');
      if (icon) {
        if (b.dataset.sort === currentSort) {
          icon.className = currentDirection === 'asc'
            ? 'fa-solid fa-arrow-up'
            : 'fa-solid fa-arrow-down';
        } else {
          icon.className = 'fa-solid fa-arrow-up';
        }
      }
    });

    applyFiltersAndSort();
  });
});

// Apply filters and sorting
function applyFiltersAndSort() {
  const cards = Array.from(document.querySelectorAll('.card-item'));

  // Filter
  cards.forEach(card => {
    const cardTags = card.dataset.tags.split(',');
    if (currentFilter === 'all' || cardTags.includes(currentFilter)) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });

  // Sort visible cards
  const visibleCards = cards.filter(card => !card.classList.contains('hidden'));
  visibleCards.sort((a, b) => {
    if (currentSort === 'date') {
      return currentDirection === 'asc'
        ? new Date(a.dataset.date) - new Date(b.dataset.date)
        : new Date(b.dataset.date) - new Date(a.dataset.date);
    } else {
      return currentDirection === 'asc'
        ? a.dataset.title.localeCompare(b.dataset.title)
        : b.dataset.title.localeCompare(a.dataset.title);
    }
  });

  // Re-append in sorted order
  visibleCards.forEach(card => {
    cardsGrid.appendChild(card);
  });
}

// Initialize
applyFiltersAndSort();
```

## Data Attributes Reference

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `data-tags` | Comma-separated tags for filtering | `data-tags="ai,architecture"` |
| `data-date` | ISO date for sorting | `data-date="2026-02-20"` |
| `data-title` | Title for alphabetical sorting | `data-title="AI Architecture"` |

## Browser Support

- All modern browsers (Chrome, Firefox, Safari, Edge)
- IE11+ (with flexbox fallback if needed)
- Mobile browsers (iOS Safari, Chrome Android)
