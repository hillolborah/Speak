from datasets import load_dataset, Audio
from huggingface_hub import login
login(token="hg_access_token")

ds = load_dataset("changelinglab/easycall-dysarthria")
ds = ds.cast_column("audio", Audio(sampling_rate=16000))

# print(ds)

sample = ds["train"][0]

print(sample.keys())
print(sample)