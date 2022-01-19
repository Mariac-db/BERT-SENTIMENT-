# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:37:41 2022

@author: User
"""

import transformers

MAX_LEN=64
TRAIN_BATCH_SIZE=8
VALID_BATCH_SIZE=4
EPOCHS=10

BERT_PATH="C:/Users/User/OneDrive - Instituto Tecnológico Metropolitano/CODIGOS/Transformers/BERT-NER/Sentiment BERT/Input"
MODEL_PATH = "model.bin"
TRAINING_FILE="C:/Users/User/OneDrive - Instituto Tecnológico Metropolitano/CODIGOS/Transformers/BERT-NER/Sentiment BERT/data.csv"
TOKENIZER=transformers.BertTokenizer.from_pretrained(
    BERT_PATH,
    do_lower_case=True) 

