#!/usr/bin/env python
# coding: utf-8

# In[3]:


from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained('nlpconnect/vit-gpt2-image-captioning')
feature_extractor = ViTImageProcessor.from_pretrained(
    'nlpconnect/vit-gpt2-image-captioning')
tokenizer = AutoTokenizer.from_pretrained('nlpconnect/vit-gpt2-image-captioning')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

gen_kwargs = {'max_length': 16, 'num_beams': 4}

def predict_step(image):
    pixel_values = feature_extractor(
        images=[image], return_tensors='pt').pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds[0]


# In[4]:


image = Image.open(R'C:\Users\Sri_Harshitha\Downloads\jpg_44-2.jpg')
print(predict_step(image=image))

