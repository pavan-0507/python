import streamlit as st

def Gen_Eff(V, CL, IL, K, Rse, Ra):

    CUL = (K * IL) ** 2 * (Rse + Ra)
    Eff = (K * V * IL - CL - CUL) / (K * V * IL) * 100
    
    return Eff, CUL


st.title("2205A21011-PS11") 
st.write("calculate the efficiency of DC series motor in various loads")
col1,col2 = st.columns(2)  
with col1:
    with st.container(border=True):
     V = st.number_input("Voltage (V)", value=230.0)  
     CL = st.number_input("Core Loss (CL) in Watts", value=100.0)  
     IL = st.number_input("Full Load Current (IL) in Amps", value=15.0)  
     K = st.number_input("Loading on Motor (K)", value=1)  
     Rse = st.number_input("Series Field Resistance (Rse) in Ohms", value=0.20)  
     Ra = st.number_input("Armature Resistance (Ra) in Ohms", value=0.10)
     compute = st.button("compute") 
     

    with st.container(border=True):
      if compute:
          with col2:
           Eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)
           st.write(f"**Efficiency of a DC series motor(%)**: {Eff:.2f}%")
           st.write(f"**Core Loss (CUL) in Watts**: {CUL:.2f} W")
