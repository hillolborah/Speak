from datasets import load_dataset
import re


class EasyCallDataset:

    def __init__(
        self,
        split="train",
        severity="1",
        speaker=None,
        normalize=True
    ):
        """
        EasyCall dataset loader

        Args:
            split: dataset split (train/test/validation)
            severity: dysarthria severity filter
            speaker: optional speaker filter
            normalize: normalize transcript text
        """

        # Load dataset
        self.ds = load_dataset(
            "changelinglab/easycall-dysarthria"
        )[split]

        # Filter by severity
        self.ds = self.ds.filter(
            lambda x: x["dysarthria_severity"] == severity
        )

        # Filter by speaker (optional)
        if speaker is not None:
            self.ds = self.ds.filter(
                lambda x: x["speaker"] == speaker
            )

        self.normalize = normalize

    def __len__(self):
        return len(self.ds)

    def normalize_text(self, text):
        """Normalize transcript text"""

        text = text.lower().strip()

        # remove punctuation
        text = re.sub(r"[^\w\s]", "", text)

        # normalize whitespace
        text = re.sub(r"\s+", " ", text)

        return text

    def __getitem__(self, idx):

        sample = self.ds[idx]

        transcript = sample["text"]

        if self.normalize:
            transcript = self.normalize_text(transcript)

        return {
            "audio": sample["audio"]["array"],
            "sampling_rate": sample["audio"]["sampling_rate"],
            "transcript": transcript,
            "speaker": sample["speaker"],
            "filename": sample["filename"]
        }