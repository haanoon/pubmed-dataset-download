import os
import random
from datasets import load_dataset

# Load general corpus (Wikipedia)
def load_general_corpus():
    dataset = load_dataset("wikipedia", "20220301.en", split="train")
    return dataset["text"]

# Load domain-specific corpus (PubMed abstracts)
def load_medical_corpus():
    # Example: Filter PubMed abstracts by MeSH IDs for human diseases
    pubmed_dataset = load_dataset("pubmed", split="train")
    filtered_abstracts = [
        example["abstract"] for example in pubmed_dataset
        if "Diseases [C]" in example["mesh_ids"]  # Replace with actual filtering logic
    ]
    return filtered_abstracts

# Save corpora to text files
def save_corpus(corpus, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(corpus))

general_corpus = load_general_corpus()
medical_corpus = load_medical_corpus()

save_corpus(general_corpus, "general_corpus.txt")
save_corpus(medical_corpus, "medical_corpus.txt")