```
Full dataset → severity=1 → command analysis → top-5 commands → MVP dataset (265 samples)
```

* Dataset Reduction Rationale:\
The EasyCall dataset contains a large set of spoken commands produced by speakers with varying levels of dysarthria. Initial inspection revealed that automatic speech recognition (ASR) outputs exhibit significant variability and frequent transcription collapse, where multiple distinct commands are mapped to common conversational tokens such as “ciao” or “grazie”.

* Controlled MVP Subset:\
To enable controlled experimentation on semantic command recovery, we construct a minimal viable subset of the dataset. We restrict the dataset to:
    * dysarthria severity level 1
    * a set of commands whose ASR outputs exhibit both reasonable consistency and sufficient separability.

* Command Selection Methodology:\
Each command was evaluated using three metrics derived from ASR outputs:
    * Transcript Consistency – the frequency of the most common ASR transcription for a command.
    * Transcript Entropy – the diversity of transcripts produced by the ASR system.
    * Command Separability – the distance between transcript embeddings of different commands.

    Commands with high consistency, low entropy, and sufficient separability were selected for the MVP experiments.

* Final Dataset:\
Based on this analysis, five commands were selected for the MVP system:
no, stop, quattro, nove, cinque
The resulting dataset contains 265 utterances, each consisting of:
    * audio waveform
    * canonical command label

    This subset provides a controlled environment for studying semantic recovery of commands from noisy ASR transcripts.