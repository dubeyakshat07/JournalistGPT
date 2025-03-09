# JournalistGPT

JournalistGPT is designed to revolutionize the way news events in India are analyzed by leveraging advanced large language models (LLMs). It can efficiently query, summarize, and interconnect multiple news events, allowing users to track developments across different timeframes and sources. By identifying patterns, common themes, and underlying narratives, the system helps researchers gain a deeper understanding of the socio-political and economic factors influencing events. Furthermore, it provides contextual analysis by linking past incidents with present occurrences, offering a comprehensive timeline of interconnected events. This functionality is particularly valuable for researchers, policymakers, and analysts who seek to uncover the broader implications of news developments beyond isolated incidents.  

Beyond mere summarization and event connection, JournalistGPT extends its capabilities to detect flaws, misinformation, or systemic shortcomings that may have contributed to a particular event. By analyzing multiple reports, statements, and expert opinions, it can highlight inconsistencies, media biases, or governance lapses that led to the situation. Advanced sentiment and bias detection modules help assess the tone and framing of news coverage, ensuring a more objective and holistic understanding of events. Additionally, JournalistGPT can generate structured reports, visualizing event interconnections through graphs and charts, making complex event relationships easier to comprehend. As a tool strictly meant for research purposes, it aims to advance the application of LLMs in media analysis while ensuring ethical and responsible use in studying Indian news narratives.
## GPT-Trained on Inshorts News Dataset (2023)  

## Overview  
This repository contains a GPT model trained on a news dataset from **Inshorts**, spanning from **2005 to December 2023**. The model has been fine-tuned to generate news summaries, headlines, and insights based on extensive real-world data.  

Access to the trained models is available upon request. You can contact me via [LinkedIn](https://www.linkedin.com/in/akshat0007/).  

## About Inshorts  
[Inshorts](https://www.inshorts.com) is a news aggregation platform that provides concise summaries of news articles, typically within 60 words. The dataset used in this project was sourced from **Kaggle (Inshorts Dataset - English)** and includes comprehensive news details over nearly two decades.  

### **Disclaimer**  
I do not hold any rights to the dataset. The dataset was provided on **Kaggle** as **open-source** and is used solely for research and educational purposes.  

## Setup and Execution  

To use this project, follow these steps:  

1. **Download the dataset:** Obtain the CSV file from [Kaggle](https://www.kaggle.com/datasets/shivamtaneja2304/inshorts-dataset-english) (search for *Inshorts Dataset - English*).  
2. **Convert to input format:** Open the Jupyter Notebook within the `data/` folder and use it to transform the CSV into `input.txt`.  
3. **Prepare data:** Move `input.txt` into the `data/` directory.  
4. **Set up the environment:**  
   ```bash
   conda create --name journalist python=3.9  
   conda activate journalist  
   pip install -r requirements.txt  
   ```  
5. **Prepare dataset for training:**  
   ```bash
   python data/news_char/prepare.py  
   ```  
6. **Train the model:**  
   ```bash
   python config/train_news_base_gpt.py  
   ```  
7. **Adjust training parameters (Optional):**  
   You can modify `config/train_news_base_gpt.py` for better performance:  
   ```python
   gradient_accumulation_steps = 1  
   batch_size = 64  
   block_size = 256  # Context of up to 256 previous characters  

   n_layer = 6  
   n_head = 6  
   n_embd = 384  
   dropout = 0.2  
   ```  
8. **Trained Model Output:**  
   The trained model will be available at:  
   ```
   out_news_char/  
   ```  

## **Apple MacBook MPS & CUDA Compatibility**  
- The code is **automatically optimized** to run on **Mac MPS (Apple M1/M2/M3 chips)** for faster training.  
- If you wish to use **CUDA** (NVIDIA GPUs), update the `device` setting in `config/train_news_base_gpt.py`:  
   ```python
   device = "cuda"  # Change from "mps" to "cuda" for NVIDIA GPU support
   ```  

## Future Updates  
More models will be added to fine-tune open-source models from **Hugging Face** for enhanced performance and improved news summarization capabilities. Stay tuned for updates!  

## Credits  
This project is inspired by the work of **[Andrej Karpathy](https://github.com/karpathy)**, particularly his advancements in training GPT models on character-level datasets.  

For any inquiries or access requests, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/akshat0007/).  

---
