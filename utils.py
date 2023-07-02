import yaml
import streamlit as st
from vncorenlp import VnCoreNLP
from transformers import AutoTokenizer, EncoderDecoderModel


with open('./config.yaml') as f:
    configs = yaml.load(f, Loader=yaml.SafeLoader)

tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)
encoder_max_length = configs['encoder_max_length']
decoder_max_length = configs['decoder_max_length']


# Get the checkpoints from gcp
model = EncoderDecoderModel.from_pretrained(configs['output_dir'])
rdrsegmenter = VnCoreNLP("./vncorenlp/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx2g')