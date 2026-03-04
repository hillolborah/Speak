# 04 — Evaluation Protocol

## 1. Purpose

This document defines the experimental setup for evaluating the Speak MVP system.

Evaluation focuses on:
- Intent recognition accuracy
- Robustness under ASR noise
- Comparison between ASR quality and intent accuracy

## 2. Research Objective

**Primary question:**  
Can semantic similarity mapping preserve intent accuracy even under high ASR word error rates?

## 3. Dataset Construction

### 3.1 Controlled Recording Setup

For each command $c_i$:
- Record 10–20 utterances
- Natural speaking style
- Single user (mild impairment)
- Quiet environment

Total dataset size:
$$N = k \times u$$
where $k$ = number of commands, $u$ = utterances per command.  
Example: 7 commands × 15 utterances = 105 samples.

### 3.2 Data Storage

For each sample, store a JSON object:
```json
{
  "audio_path": "...",
  "ground_truth_command": "...",
  "asr_transcript": "...",
  "predicted_command": "...",
  "similarity_score": ...
}
```

## 4. Metrics

### 4.1 Intent Accuracy
$$A_{\text{accuracy}} = \frac{\text{Correct Predictions}}{\text{Total Samples}}$$

### 4.2 Intent Error Rate (IER)
$$\mathrm{IER} = 1 - A_{\text{accuracy}}$$

### 4.3 Word Error Rate (WER)
For each sample:
$$\mathrm{WER} = \frac{S + D + I}{N}$$
Compare ASR transcript with reference phrase.

### 4.4 Confusion Matrix
Compute a confusion matrix across commands to:
- Identify which commands are frequently confused
- Detect semantic overlap issues

### 4.5 Similarity Score Distribution
Analyze:
- Distribution of similarity scores
- Correct vs incorrect predictions
- Optimal rejection threshold $\tau$

## 5. Threshold Analysis

Define rejection threshold $\tau$.

Experiment:
- Sweep $\tau \in [0.5, 0.95]$

Measure:
- Accuracy
- Rejection rate
- False accept rate

**Goal:** Find balance between safety and usability.

## 6. Baseline Comparison

Optional baseline:
- Fuzzy string matching
- Edit distance–based mapping

Compare:

| Method              | Intent Accuracy |
|---------------------|-----------------|
| Fuzzy Matching      | ?               |
| Embedding Similarity| ?               |

This strengthens research contribution.

## 7. Error Analysis

For misclassified samples, analyze:
- ASR transcript distortion
- Similarity scores
- Semantic confusion patterns

Categorize errors:
- Severe ASR distortion
- Semantic ambiguity
- Threshold miscalibration

## 8. Reporting Format (For Paper)

Include:
- Dataset size
- Command distribution
- ASR model used
- Embedding model used
- Intent Accuracy
- WER
- IER
- Confusion matrix
- Threshold curve

## 9. MVP Assumptions

- Single speaker
- Quiet environment
- No adversarial inputs
- No background noise stress testing

## 10. Future Evaluation Extensions

- Multi-session variability
- Noise robustness
- Cross-speaker generalization
- Fine-tuned ASR comparison
- Direct speech-to-intent modeling