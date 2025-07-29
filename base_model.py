from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/Airavata")
model = AutoModelForCausalLM.from_pretrained(
    "ai4bharat/Airavata",
    device_map="auto",
    torch_dtype=torch.bfloat16
)

# Save base model
save_dir = "./Base_Airavata"
model.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)
