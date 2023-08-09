import transformers
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain.llms import HuggingFacePipeline
from peft import LoraConfig, PeftModel

class LLMPackage:
    def __init__(self, model_name, api_token):
        self.model_name = model_name
        self.api_token = api_token

    def getLLMResponse(self, input_statement, output_dir, max_new_tokens=2000, repetition_penalty=1.2, temperature=0.5):
        device_map = {"": 0}  # You may need to specify the appropriate device index if using a GPU

        # Reload model in FP16 and merge it with LoRA weights
        base_model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            low_cpu_mem_usage=True,
            return_dict=True,
            torch_dtype=torch.float16,
            device_map=device_map,
        )
        model = PeftModel.from_pretrained(base_model, output_dir)
        model = model.merge_and_unload()

        # Reload tokenizer to save it
        tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True)
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "right"

        # Create a pipeline for text generation using the loaded model and tokenizer
        generate_text = transformers.pipeline(
            model=model, tokenizer=tokenizer,
            return_full_text=True,
            task='text-generation',
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            repetition_penalty=repetition_penalty
        )

        # Initialize the LLM pipeline with the text generation pipeline
        return HuggingFacePipeline(pipeline=generate_text)
