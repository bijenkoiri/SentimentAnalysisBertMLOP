import tensorflow as tf
from transformers import TFBertModel




#model architecture
@tf.keras.utils.register_keras_serializable()
class SentimentAnalyzer(tf.keras.Model):
    def __init__(self, num_classes):
        super(SentimentAnalyzer,self).__init__()
        self.num_classes = num_classes
        self.transformer = TFBertModel.from_pretrained('bert-base-cased')  # 12-layers, 768-hidden, 12-heads, 112 M parameters
        
        self.dropout_layer = tf.keras.layers.Dropout(0.3)
        self.LH = tf.keras.layers.Dense(num_classes)
        self.prob_ = tf.keras.layers.Softmax()
        
    def call(self,X, attention_mask=None,training=True):
        context_embed = self.transformer(X, attention_mask = attention_mask).last_hidden_state
        context_embed = self.dropout_layer(context_embed)
        flatten_ctx_embd = tf.reshape(context_embed, shape=(context_embed.shape[0],context_embed.shape[1]*context_embed.shape[2]))
        
        lh_output = self.LH(flatten_ctx_embd)
        
        return  self.prob_(lh_output)
    