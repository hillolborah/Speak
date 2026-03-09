from datasets import load_dataset
from collections import Counter

ds = load_dataset("changelinglab/easycall-dysarthria")

commands = [x["text"] for x in ds["train"]]

print("Total samples:", len(commands))
print("Unique commands:", len(set(commands)))

counter = Counter(commands)

print("\nTop commands:")
for cmd, count in counter.most_common(20):
    print(cmd, count)