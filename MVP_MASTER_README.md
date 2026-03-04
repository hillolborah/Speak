# Speak — MVP Master README

## 1. Overview

Speak is a constrained semantic correction system designed to bridge impaired speech and voice/home assistants.

The MVP focuses on a single-user, mild speech impairment setting with a small closed command set (5–10 commands).

The system does not attempt to improve speech clarity.
Instead, it performs robust intent recognition under ASR noise.

**Core idea:**

$$x \rightarrow ASR(x) = y \rightarrow f(y) = c$$

Where:
- $x$ = impaired speech waveform
- $y$ = noisy ASR transcript
- $c$ = canonical command

The system maps noisy ASR output to a predefined command set and forwards the structured command to a voice assistant emulator.

For MVP, we emulate assistant behavior using Rasa.

## 2. Scope of MVP

**Included**
- Single user
- Mild impairment
- Stable speech patterns
- 5–10 predefined commands
- Static mapping (no learning)
- Whisper ASR integration
- Embedding-based semantic similarity mapping
- Rasa assistant emulation
- Basic logging

**Not Included**
- Fine-tuning ASR
- Online learning
- Multi-user support
- Open-domain conversation
- Production deployment
- UI polish

This is a research-grade prototype, not a product.

## 3. System Architecture

### Logical Pipeline
```
User Speech (x)
        ↓
Whisper ASR
        ↓
Noisy Text (y)
        ↓
Semantic Mapping Module
        ↓
Canonical JSON Command (c)
        ↓
Assistant Emulator (Rasa)
```

### Design Philosophy
- Closed-set command recognition
- Deterministic mapping
- No model training in MVP
- Robustness through semantic similarity, not adaptation

See: [docs/01_system_architecture.md](../01_system_architecture.md)

## 4. Core Modules

### 4.1 ASR Module
- **Model:** Whisper (pretrained)
- **Input:** raw waveform (.wav)
- **Output:** transcript (string)
- No fine-tuning in MVP.

See: [docs/modules/asr_module.md](../modules/asr_module.md)

### 4.2 Semantic Mapping Module

**Implements:**

$$c = \arg\max_{c_i \in C} \cos(e(y), e(c_i))$$

Where:
- $e(\cdot)$ is a sentence embedding model
- $C$ is the canonical command set

This is a non-parametric nearest neighbor classifier in embedding space.

No training required.

See: [docs/modules/mapping_module.md](../modules/mapping_module.md)

### 4.3 Command Ontology

**Defines:**
- Full canonical command list
- JSON schema for commands
- Allowed arguments (if any)

**Example:**
```json
{
  "intent": "call",
  "target": "mom"
}
```

See: [docs/03_command_ontology.md](../03_command_ontology.md)

### 4.4 Assistant Integration
- For MVP, assistant behavior is emulated using Rasa.
- Integration via REST endpoint.
- No direct integration with Amazon Alexa in MVP.

See: [docs/modules/assistant_integration.md](../modules/assistant_integration.md)

### 4.5 Logging

**Stores:**
- Audio path
- ASR output
- Predicted command
- Similarity score
- Timestamp

Used for analysis and research evaluation only.

See: [docs/05_logging_schema.md](../05_logging_schema.md)

## 5. Mathematical Formulation

**The system is modeled as:**
- $x \in X$ (audio space)
- $y = ASR(x)$
- $c \in C$ (finite command set)

**Mapping:**

$$f(y) = \arg\max_{c_i \in C} \cos(e(y), e(c_i))$$

**We study:**
- Word Error Rate (WER)
- Intent Error Rate (IER)

**Key research question:**

Can semantic similarity preserve intent accuracy under high ASR noise?

See: [docs/02_mathematical_formulation.md](../02_mathematical_formulation.md)

## 6. Evaluation Plan

**Metrics:**
- Intent Accuracy
- Confusion Matrix
- Similarity Score Distribution
- WER vs Intent Accuracy comparison
- Latency

**Experimental setup:**
- Controlled utterances per command
- Multiple recordings per command
- ASR transcript analysis

See: [docs/04_evaluation_protocol.md](../04_evaluation_protocol.md)

## 7. Repository Structure

```
Speak/
│
├── asr/
│   └── whisper_interface.py
│
├── mapping/
│   ├── embedder.py
│   ├── similarity.py
│   └── command_registry.json
│
├── assistant/
│   └── rasa_client.py
│
├── storage/
│   └── logger.py
│
├── evaluation/
│   └── metrics.py
│
├── docs/
│   ├── 01_system_architecture.md
│   ├── 02_mathematical_formulation.md
│   ├── 03_command_ontology.md
│   ├── 04_evaluation_protocol.md
│   ├── 05_logging_schema.md
│   └── modules/
│       ├── asr_module.md
│       ├── mapping_module.md
│       └── assistant_integration.md
│
├── main.py
├── config.yaml
└── MVP_MASTER_README.md
```
## 8. Failure Handling Policy

**If:**

$$\max \cos(e(y), e(c_i)) < \tau$$

**Then:**
- System rejects command
- Prompts user to repeat

**Threshold** $\tau$ is defined in: [docs/06_failure_handling.md](../06_failure_handling.md)
## 9. Research Positioning

**This MVP investigates:**

Robust Intent Recognition from Impaired Speech in Closed Command Domains.

**Key hypothesis:**

Even when ASR Word Error Rate is high, semantic similarity mapping can maintain high intent accuracy in constrained environments.

## 10. Roadmap Beyond MVP

**Phase 2:**
- Add logging-based analysis
- Add threshold tuning

**Phase 3:**
- Fine-tune Whisper
- Add adaptive mapping

**Phase 4:**
- Direct speech-to-intent model

See: [docs/roadmap.md](../roadmap.md)

## 11. Guiding Principles
- Keep domain small
- Keep architecture modular
- Avoid premature ML complexity
- Formalize before optimizing
- Make evaluation reproducible