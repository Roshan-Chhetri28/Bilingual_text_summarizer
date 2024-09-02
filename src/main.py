from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch


device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_path = 'model'
model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_path)

input_text = input("Enter your string(English Only): ")
input = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True).to(device)
input_id = model.generate(input["input_ids"], max_length = 50, min_length= 20, length_penalty = 2.0, early_stopping = True, num_beams = 4)

summary = tokenizer.decode(input_id[0], skip_special_tokens=True)
print("Summarizing be patient: ", end="\n")
print(summary)  

