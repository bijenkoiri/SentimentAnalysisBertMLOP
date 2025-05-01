from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager


import tensorflow as tf
from transformers import TFBertModel
from transformers import BertTokenizer, TFBertModel
import os

from model.architecture import SentimentAnalyzer
from model.preprocessing import process_text

#global model
model =None
tokenizer =None


ckpt_dir = os.path.join('.','checkpoints2')


#same mapping used wilhe training
Class_Integer_mapped_dict={0:'Negative',
                           1:'Irrelevant',
                           2:'Neutral',
                           3:'Positive'
                           }

@asynccontextmanager
async def lifespan(app: FastAPI):

    global model
    model = SentimentAnalyzer(num_classes=4)

    #model checkpoints
    ckpt = tf.train.Checkpoint(model = model)
    ckpt.restore(tf.train.latest_checkpoint(ckpt_dir))

    global tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
    
    # Yield allows the app to continue running
    yield

    # Clean up resources (e.g., close database connections)
    model = None  # Clear the model to free up memory
    tokenizer=None


###########################

app =FastAPI(lifespan=lifespan)

@app.get("/predict/")
def Predict():
    return {'pprediction':1}



@app.post("/cntx")
def Context(context:str):
    cleaned_txt =process_text(context)

    encoding = tokenizer.encode_plus(cleaned_txt, max_length =164,
                                           padding='max_length',
                                           truncation=True,
                                            return_tensors='tf',
                                            return_attention_mask=True
                                           )
    x,mask = encoding['input_ids'],encoding['attention_mask']

    y_hat = model(x,mask)
    y_pred = tf.argmax(y_hat,axis=1)
    y_pred =int(y_pred.numpy()[0])

        
    return {
        'predicted':Class_Integer_mapped_dict.get(y_pred)
    }
