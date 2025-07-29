from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

model_path = "./Base_Airavata"  # or "./Quantized_Airavata"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    torch_dtype=torch.float16
)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.get("/")
def root():
    return {"message": "Airavata FastAPI server is running. Use /docs to test the API."}

class GenerateRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 100

@app.post("/generate")
async def generate(req: GenerateRequest):
    output = pipe(
        req.prompt,
        max_new_tokens=req.max_new_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    return {"generated_text": output[0]["generated_text"]}
