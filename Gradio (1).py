#!/usr/bin/env python
# coding: utf-8

# In[2]:


import gradio as gr
from caption import predict_step
with gr.Blocks() as demo:
    image = gr.Image(type='pil', label='Image')
    label = gr.Text(label='Generated Caption')
    image.upload(predict_step,[image],[label])
if __name__ == '__main__':
    demo.launch()


# In[ ]:




