# Requirements

## Purpose

This document defines the functional and non-functional requirements for the AI Career Agent. Every implemented feature should satisfy one or more requirements in this document.

---

# Functional Requirements

## Job Discovery

### FR-001

The system shall discover job opportunities from multiple sources.

### FR-002

The system shall support collecting jobs from public APIs.

### FR-003

The system shall support collecting jobs from company career pages.

### FR-004

The system shall normalize all collected jobs into a common internal format.

### FR-005

The system shall detect and remove duplicate job postings.

---

## Job Filtering

### FR-006

The system shall filter jobs based on selected career profiles.

### FR-007

The system shall support filtering by location.

### FR-008

The system shall support filtering by job type (Internship, Graduate, Entry-Level, etc.).

### FR-009

The system shall rank opportunities by relevance.

### FR-010

The system shall recommend a limited set of high-quality opportunities per day.

---

## Career Profiles

### FR-011

The system shall support Software Engineering career opportunities.

### FR-012

The system shall support Biomedical Engineering career opportunities.

### FR-013

The system shall support Biochemistry career opportunities.

### FR-014

The system shall support hybrid career paths.

---

## Application Assistance

### FR-015

The system shall tailor the user's CV for each selected job.

### FR-016

The system shall generate tailored cover letters.

### FR-017

The system shall preserve the user's final decision before submitting any application.

---

## AI Assistance

### FR-018

The system shall use AI to improve application quality.

### FR-019

The system shall explain why a job is recommended.

### FR-020

The system shall expose a programmatic API for core workflows.

---

# Non-Functional Requirements

### NFR-001

The system should prioritize open-source technologies whenever practical.

### NFR-002

The system should minimize operational costs.

### NFR-003

The architecture shall be modular.

### NFR-004

The system should be maintainable and easy to extend.

### NFR-005

The project should use clear documentation.

### NFR-006

The system should support adding new job sources with minimal code changes.

### NFR-007

The user shall retain final control over every application submission.

### NFR-008

The codebase shall use Python type hints for public interfaces.

### NFR-009

API data contracts shall use Pydantic models.

### NFR-010

Automated tests shall be implemented with pytest.
