%%writefile app.py
 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# Making predictions 
prediction = classifier.predict([[tau1,tau2,tau3,tau4,p1,p2,p3,p4,g1,g2,g3,g4]])
     
if prediction == 0:
  pred = 'unstable'
else:
  pred = 'stable'
  return pred
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    #tau1,tau2,tau3,tau4,p1,p2,p3,p4,g1,g2,g3,g4
    st.header("Machine Learning-Based Model for Prediction of Stability in Smart Grid")
    tau1 = st.number_input('Insert tau1 Value between (0.5 , 10)',min_value=0.500793	,max_value=9.999469) 
    tau2 = st.number_input('Insert tau2 Value between (0.5 , 10)',min_value=0.500141	,max_value=9.999837)
    tau3 = st.number_input('Insert tau3 Value between (0.5 , 10)',min_value=0.500141		,max_value=9.999837	)
    tau4 = st.number_input('Insert tau4 Value between (0.5 , 10)',min_value=0.500141	,max_value=9.999837	)
    p1 = st.number_input('Insert p1 Value between (1.5 , 6)',min_value=1.582590	,max_value=5.864418)
    p2 = st.number_input('Insert p2 Value between (-0.5 , -2)',min_value=-1.999945,max_value=-0.500025)
    p3 = st.number_input('Insert p3 Value between (-0.5 , -2)',min_value=-1.999945	,max_value=-0.500025)
    p4 = st.number_input('Insert p4 Value between (-0.5 , -2)',min_value=-1.999945	,max_value=-0.500025)
    g1 = st.number_input('Insert g1 Value between (0,1)',min_value=0.050009	,max_value=0.999937) 
    g2 = st.number_input('Insert g2 Value between (0,1)',min_value=0.050028	,max_value=0.999982	) 
    g3 = st.number_input('Insert g3 Value between (0,1)',min_value=0.050028	,max_value=0.999982	) 
    g4 = st.number_input('Insert g3 Value between (0,1)',min_value=0.050028	,max_value=0.999982	) 
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(tau1,tau2,tau3,tau4,p1,p2,p3,p4,g1,g2,g3,g4) 
        st.success('Smart Grid is {}'.format(result))
     
if __name__=='__main__': 
    main()
