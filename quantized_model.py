from transformers import BitsAndBytesConfig, AutoTokenizer, AutoModelForCausalLM
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_compute_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/Airavata")
model = AutoModelForCausalLM.from_pretrained(
    "ai4bharat/Airavata",
    quantization_config=bnb_config,
    device_map="auto"
)

# Save quantized model
save_dir = "./Quantized_Airavata"
model.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)
