# 03 — Command Ontology Specification

## 1. Purpose

This document defines the canonical command space $C$ used in the Speak MVP.

Because the system operates in a closed-set domain, this ontology strictly defines:
- All valid commands
- Their structured representation
- Their natural language forms
- Their semantic intent

This document is the authoritative reference for command mapping and evaluation.

## 2. Design Principles

- **Small Closed Set**  
  5–10 commands only; no open-ended commands.
- **Unambiguous Semantics**  
  Each command maps to exactly one intent.
- **Minimal JSON Structure**  
  No unnecessary nesting; flat schema where possible.
- **Extendable**  
  Future arguments can be added without breaking schema.

## 3. Canonical Command Set (MVP v1)

Example command set (modifiable as needed):

1️⃣ **Call Mom**

```json
{
  "intent": "call",
  "target": "mom"
}
```

Representative phrases:
- "call mom"
- "phone mom"
- "dial mom"

2️⃣ **Call Dad**

```json
{
  "intent": "call",
  "target": "dad"
}
```

Representative phrases:
- "call dad"
- "phone dad"

3️⃣ **Play Music**

```json
{
  "intent": "play_music"
}
```

Representative phrases:
- "play music"
- "start music"
- "music on"

4️⃣ **Stop Music**

```json
{
  "intent": "stop_music"
}
```

Representative phrases:
- "stop music"
- "music off"

5️⃣ **Turn On Light**

```json
{
  "intent": "light_control",
  "action": "on"
}
```

Representative phrases:
- "turn on light"
- "light on"
- "switch light on"

6️⃣ **Turn Off Light**

```json
{
  "intent": "light_control",
  "action": "off"
}
```

Representative phrases:
- "turn off light"
- "light off"
- "switch light off"

7️⃣ **Emergency Call**

```json
{
  "intent": "emergency_call"
}
```

Representative phrases:
- "help"
- "emergency"
- "call for help"

## 4. Formal Definition

Let:
$$C = \{c_1, c_2, \ldots, c_k\},$$
where $k \le 10$.  
Each $c_i$ is uniquely defined by its JSON schema.  
The mapping module selects exactly one $c_i \in C$.

## 5. Canonical Phrase Registry

For embedding comparison, each command has one canonical representative phrase.

**Example registry:**
```json
{
  "call_mom": "call mom",
  "call_dad": "call dad",
  "play_music": "play music",
  "stop_music": "stop music",
  "light_on": "turn on light",
  "light_off": "turn off light",
  "emergency_call": "emergency call"
}
```

These phrases are embedded and stored at system initialization.

## 6. Command Identifier Convention

Each command should have:
- **Human-readable name**
- **Unique internal ID**

Example:

| ID         | JSON Intent                                  |
|------------|-----------------------------------------------|
| call_mom   | `{"intent": "call", "target": "mom"}` |
| play_music | `{"intent": "play_music"}`                |

Mapping layer outputs the ID, which maps to JSON.

## 7. High-Risk Commands

The following commands may require stricter confidence thresholds:
- `emergency_call`
- `call_mom`
- `call_dad`

These should be flagged in evaluation.

## 8. Ontology Constraints

- No overlapping semantic meanings
- No ambiguous synonyms across commands
- No hierarchical intent structure in MVP

## 9. Future Extensions

Possible additions:
- Room-specific light control
- Volume control
- Temperature control
- Multi-argument commands

(Not included in MVP.)