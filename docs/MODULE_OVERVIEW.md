# 📦 legal-core Module Overview

---

## 🧩 1. Core Legal Processing Functions

| Module | Description |
|--------|-------------|
| `metadata_extractor.py` | Extracts tenant name, date, case ID, and metadata from PDF/DOCX |
| `contracts.py` | Analyzes contract terms like parties, duration, breach, clauses |
| `law_parser.py` | Converts legal text (Acts/Statutes) into machine-readable format |
| `doc_classifier.py` | Classifies documents (notice, appeal, order, etc) |

---

## 🇦🇺 2. Australia/Victoria-Specific Modules

| Module | Description |
|--------|-------------|
| `vcat_rules.py` | Loads VCAT rules by form (Form A, B, C…) |
| `form_mapper.py` | Maps extracted info to form-specific fields |
| `tenancy_notice_parser.py` | Parses eviction/breach notices per RTA Victoria |

---

## 🔧 3. Tools (Reusable, Extendable)

| Module | Description |
|--------|-------------|
| `pdf_utils.py` | Converts PDF → text, locates metadata, extracts page ranges |
| `docx_utils.py` | Parses .docx block-by-block |
| `tokenizer.py` | Chunks legal text for LLMs (Claude/GPT) using token-aware slicing |

---

## 🌐 4. API Interfaces (AI & Government)

| Module | Description |
|--------|-------------|
| `gov_data.py` | Calls VIC Gov APIs (e.g. DataVic, Consumer Affairs) |
| `austlii_client.py` | Queries AustLII for statutes and precedent |
| `openai_interface.py` | Uses GPT/Claude for summarization, reasoning, extraction |

---

## 🧪 5. Testing & Simulation

| Module | Description |
|--------|-------------|
| `test_contracts.py` | Tests for clause/term detection in contracts |
| `test_pdf_utils.py` | Verifies PDF extraction integrity |
| `test_vcat_rules.py` | Ensures correct VCAT form–rule mapping logic |

---

## 📁 6. Templates & Legal Docs

| File | Description |
|------|-------------|
| `vcat_template.pdf` | Ready-to-use VCAT form with fillable fields |
| `universal_contract_template.docx` | Global contract template for automation |
| `API_REFERENCE.md` | API usage & structure documentation |
| `LEGAL_DOMAINS.md` | Jurisdiction & domain mapping for current modules |
| `ROADMAP.md` | Legal-core version roadmap & expansion plan |

---

## 🧠 7. Psychological/Machiavellian Analysis

| Module | Description |
|--------|-------------|
| `machiavellian_analyzer.py` | Detects manipulative patterns in language using dark triad traits |
| `motive_detector.py` | Attempts to infer likely motives from contract or statement structure |
| `persona_mapper.py` | Maps tone/language to psychological profile (assertive, avoidant, dominant) |
