# Architecture

## High-Level Overview

The AI Career Agent is composed of several independent modules.

Each module performs one responsibility.

```

```

             +----------------------+
             |    Job Sources       |
             +----------+-----------+
                        |
        +---------------+----------------+
        |                                |
     APIs                         Web Scrapers
        |                                |
        +---------------+----------------+
                        |
                Job Aggregator
                        |
                Job Normalizer
                        |
              Duplicate Removal
                        |
                 Job Filter Engine
                        |
                 AI Ranking Engine
                        |
               Recommendation Engine
                        |
         +--------------+---------------+
         |                              |
     CV Tailoring               Cover Letter
         |                              |
         +--------------+---------------+
                        |
                  User Dashboard

```

---

## Modules

### Job Sources

Responsible for collecting jobs.

Examples:

- APIs
- Company career websites
- Job boards

---

### Aggregator

Collects jobs from all sources.

---

### Normalizer

Converts every job into one standard format.

Example

```

Company
Title
Location
Remote
URL
Posted Date

```

---

### Duplicate Detector

Removes duplicate listings.

---

### Filter Engine

Filters based on:

- Career Profile
- Experience
- Location
- Remote preference

---

### Ranking Engine

Ranks jobs according to relevance.

---

### CV Tailoring

Adapts the CV to each role.

---

### Cover Letter Generator

Creates personalized cover letters.

---

### Dashboard

Displays recommended opportunities.

---

## Development Principles

- One responsibility per module
- Reusable components
- Easy to test
- Easy to extend
- Prefer free APIs
- Use web scraping where appropriate and permitted

---

## Future Modules

- Interview Preparation
- Salary Analysis
- Skill Gap Analysis
- Learning Recommendations
- Career Analytics
```
