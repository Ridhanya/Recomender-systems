import pickle
import scipy.sparse as sparse
from Recommendation import recommendation
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
import requests



app = FastAPI(debug=True)
model_var = pickle.load(open('model.pickle', 'rb'))

class Data(BaseModel):
	person_id:int






@app.put('/predict')
def predict(data:Data):
	data_dict=data.dict()
	person_vecs = sparse.csr_matrix(model_var.user_factors)
	content_vecs = sparse.csr_matrix(model_var.item_factors)
	mat=recommendation.sparse_person_content
	recommendations = recommendation.recommend(data.person_id, mat, person_vecs, content_vecs)
	return recommendations['title']
	
	



if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
