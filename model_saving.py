# saving the model 
import pickle 
pickle_out = open("classifier.pkl", mode = "wb") 
pickle.dump(rfn, pickle_out) 
pickle_out.close()
