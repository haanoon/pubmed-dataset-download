from datasets import load_dataset, concatenate_datasets

# Load datasets
medical_data = load_dataset('pubmed')  # Your medical corpus
general_data = load_dataset('wikipedia', '20220301.en')  # General corpus

# Calculate oversampling ratio
oversample_factor = len(general_data['train']) // len(medical_data['train'])

# Create oversampled medical dataset
oversampled_medical = medical_data['train'].map(lambda x: x, batched=True).shuffle().repeat(oversample_factor)

# Combine datasets
combined_data = concatenate_datasets([
    general_data['train'].shuffle(),
    oversampled_medical
]).shuffle() 