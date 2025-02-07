# from datasets import load_dataset

# datasets = load_dataset("pubmed",name = '2025')

# datasets.save_to_disk("pubmed_dataset_local")

# print(datasets)


from pubmed.pubmed import Pubmed
import datasets
from datasets import DownloadConfig

# Initialize the builder
builder = Pubmed()

# Create a download config FIRST
builder.download_config = DownloadConfig(
    cache_dir="./pubmed_cache",
    force_download=False
)

# Then proceed with download
builder.download_and_prepare()

# Load the dataset
dataset = datasets.load_from_disk(builder.cache_dir)

# Use the dataset
print(dataset["train"][0])  