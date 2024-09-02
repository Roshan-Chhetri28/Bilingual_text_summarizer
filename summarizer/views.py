from django.shortcuts import render
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch


device = "cuda" if torch.cuda.is_available() else "cpu"
model_path = "model"  # The path where you saved the trained model
model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_path)

def summarize_text(request):
    if request.method == "POST":
        input_text = request.POST.get('input_text')
        inputs = tokenizer("summarize: " + input_text, return_tensors="pt", max_length=1024, truncation=True).to(device)
        summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return render(request, 'summarize.html', {'summary': summary, 'input_text': input_text})
    return render(request, 'summarize.html')
