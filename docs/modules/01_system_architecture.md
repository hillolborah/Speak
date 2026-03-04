# 01 — System Architecture

## 1. Purpose

This document defines the architectural design of the Speak MVP system.

The system is designed to bridge impaired speech and voice/home assistants by performing robust intent recognition in a constrained command domain.

This document specifies:
- System boundaries
- Module responsibilities
- Data flow
- Interfaces
- Design constraints

The MVP focuses on clarity, modularity, and research reproducibility.

## 2. Problem Context

Users with mild speech impairments often produce speech that general-purpose ASR systems transcribe with errors.

Instead of attempting to correct speech acoustically, the system performs semantic correction at the intent level.

The system transforms:

$$x \rightarrow y \rightarrow c$$

Where:
- $x$ = impaired speech waveform
- $y$ = ASR transcript (possibly noisy)
- $c$ = canonical structured command

## 3. Architectural Principles

### Closed Command Set
- 5–10 predefined commands
- No open-domain speech

### Static Mapping
- No training or fine-tuning in MVP
- Deterministic similarity-based mapping

### Modular Design
- ASR independent of mapping
- Mapping independent of assistant
- Easy to extend later

### Research-Oriented
- Logging for evaluation
- Clear metrics separation
- Reproducibility‑first design

## 4. High-Level System Diagram

```
User Speech (x)
        ↓
ASR Module (Whisper)
        ↓
Transcript (y)
        ↓
Semantic Mapping Module
        ↓
Canonical JSON Command (c)
        ↓
Assistant Integration Layer (Rasa)
```

For assistant emulation, we use Rasa.  
Future integration with Amazon Alexa is possible but not part of MVP.

## 5. Module Specifications

### 5.1 ASR Module

**Responsibility:** Convert raw speech waveform into text transcript.

- **Input:** `.wav` audio file  
- **Output:** String transcript  
- **Implementation:** Pretrained Whisper model (no fine‑tuning in MVP)  
- **Boundary:** ASR module does not perform intent inference.

### 5.2 Semantic Mapping Module

**Responsibility:** Map ASR transcript to one canonical command.

- **Input:** Transcript string $y$  
- **Output:** 
  - Canonical JSON command $c$  
  - Similarity score  
- **Mechanism:**
  - Sentence embedding of transcript
  - Cosine similarity with canonical command embeddings
  - Argmax selection  

This module is a non‑parametric nearest‑neighbor classifier in embedding space.

### 5.3 Command Ontology

Defines:
- Canonical commands
- JSON schema
- Allowed arguments

This ensures:
- No ambiguity in evaluation
- Clean integration
- Controlled domain scope

### 5.4 Assistant Integration Module

**Responsibility:** Forward canonical command to assistant emulator.

- **Integration method:** REST API call to local Rasa server  
- Assistant emulation is handled via Rasa.

### 5.5 Logging Module

**Stores:**
- Timestamp  
- Audio file path  
- ASR transcript  
- Predicted command  
- Similarity score  

**Purpose:**
- Evaluation
- Research analysis
- Error inspection

## 6. Data Flow

- User records speech  
- Audio saved locally  
- Audio passed to ASR  
- Transcript passed to mapping module  
- Canonical JSON command produced  
- Command sent to assistant emulator  
- Interaction logged

## 7. Failure Handling

If similarity score < threshold $\tau$:
- System rejects command
- Prompts user to repeat

Threshold policy defined separately.

## 8. Non-Goals (MVP)

- No multi-user support
- No personalization
- No online learning
- No cloud deployment
- No ASR retraining
- No generative models

## 9. Extensibility Points

Future expansion may include:
- Adaptive threshold tuning
- Fine‑tuned ASR
- Direct speech-to-intent modeling
- Multi-user support
- Edge deployment

Architecture supports extension without refactoring core pipeline.