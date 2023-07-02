import yaml
from transformers import AutoTokenizer, EncoderDecoderModel


with open('./config.yaml') as f:
    configs = yaml.load(f, Loader=yaml.SafeLoader)

tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)
# Get the checkpoints from save_model
model = EncoderDecoderModel.from_pretrained(configs['model_dir'])

def decode_summary(text):
    inputs = tokenizer(text, padding="max_length", truncation=True, max_length=256, return_tensors="pt")
    input_ids = inputs.input_ids.to("cpu")
    attention_mask = inputs.attention_mask.to("cpu")

    outputs = model.generate(input_ids, attention_mask=attention_mask)
    # all special tokens including will be removed
    output_str = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return output_str[0]
