# 02 — Mathematical Formulation

## 1. Problem Definition

Let:
- $X$ = space of speech waveforms
- $Y$ = space of text transcripts
- $C$ = finite set of canonical commands

We define:
- $x \in X$

**ASR transformation:**
$$y = A(x),\qquad A: X \rightarrow Y$$

**Semantic mapping:**
$$c = f(y),\qquad f: Y \rightarrow C$$

Overall system:
$$c = f(A(x))$$

## 2. Closed-Set Intent Space

Command set:
$$C = \{c_1, c_2, \ldots, c_k\}$$
where $k \in [5,10]$.  
Each $c_i$ has structured JSON representation.  
Closed-set assumption simplifies classification.

## 3. Embedding-Based Mapping

Let
$$e: Y \rightarrow \mathbb{R}^d$$
be a pretrained sentence embedding function.

For each canonical command $c_i$, we define a representative natural language phrase and compute:
$$v_i = e(c_i).$$

For transcript $y$:
$$v_y = e(y).$$

**Similarity score:**
$$S(y,c_i) = \cos(v_y, v_i).$$

**Command selection:**
$$c^* = \arg\max_{c_i \in C} S(y,c_i).$$

## 4. Confidence Thresholding

Define threshold $\tau$.

If
$$\max_{c_i} S(y,c_i) < \tau,$$

then system rejects prediction.

## 5. Error Metrics

### 5.1 Word Error Rate (WER)

For transcript $y$ relative to ground-truth $y^*$:
$$\mathrm{WER} = \frac{S + D + I}{N}$$

Where:
- $S$ = substitutions
- $D$ = deletions
- $I$ = insertions
- $N$ = number of words in reference

### 5.2 Intent Error Rate (IER)

Let $c^*$ = predicted command and $c_{\text{true}}$ = true command.
$$\mathrm{IER} = \frac{\text{Number of incorrect intent predictions}}{\text{Total commands}} = 1 - \text{Accuracy}.$$ 

## 6. Research Hypothesis

**Hypothesis:**

High WER does not necessarily imply high IER.  
In constrained domains:
$$\mathrm{IER} \ll \mathrm{WER}.$$  

This suggests semantic similarity mapping compensates for ASR noise.

## 7. Error Propagation Analysis

The system has two stages:
- Acoustic-to-text error (ASR)
- Text-to-intent error (Mapping)

Total error:
$$P(c \neq c_{\text{true}}) = P(\text{Mapping error}\mid \text{ASR output}).$$

Goal: Minimize conditional mapping error despite noisy $y$.

## 8. MVP Assumptions

- $C$ is small
- Single user
- Speech variability is low
- No model fine-tuning
- Embedding model fixed

## 9. Future Formal Extensions

Potential expansions:
- Learnable classifier $f_\theta(y)$
- Direct model $g_\phi(x)\rightarrow c$
- Bayesian confidence modeling
- Reinforcement learning from feedback

(Not included in MVP.)