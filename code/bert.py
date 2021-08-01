from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained("bert-base-uncased")

tokenizer.save_pretrained('./test/saved_model/')
model.save_pretrained('./test/saved_model/')

print('done')