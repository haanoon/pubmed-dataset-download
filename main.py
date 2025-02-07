import re

from datasets import load_dataset

wiki_dataset = load_dataset('wikipedia', '20220301.en')
book_dataset = load_dataset('bookcorpus')

pubmed = load_dataset('pubmed')



print(wiki_dataset.head())
def clean_text(text):
    text = re.sub(r'\s+',' ',text)
    text = re.sub(r'[^a-zA-z0-9.,!?]',' ',text)
    return text.strip()

# wiki_clean = wiki_dataset.map()

def save_dataset_to_file(dataset, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for example in dataset['train']:  # Access the 'train' split
            cleaned_text = clean_text(example['text'])  # Assuming 'text' is the field name
            f.write(cleaned_text + '\n')

# Save PubMed dataset
save_dataset_to_file(pubmed, 'pubmed_cleaned.txt')