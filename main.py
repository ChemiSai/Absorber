import streamlit as st
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("McCabe–Thiele Method for finding number of trays needed for an Absorber")
st.sidebar.markdown("# **Define the Absorption system**")
y_in=st.sidebar.slider("Absorbate inlet Mole fraction (Yn+1)",min_value=0.1,max_value=0.999,value = 0.5,step = 0.01)
y_out=st.sidebar.slider("Absorbate outlet Mole fraction (Y1)",min_value=0.001,max_value=y_in,value = 0.1,step = 0.001)
x_out = st.sidebar.slider("Absorbent outlet Mole fraction (Xn)",min_value=0.1,max_value=y_in,value = 0.28,step = 0.01)
x_in = st.sidebar.slider("Absorbent inlet Mole fraction (Xo)",min_value=0.0,max_value=x_out,value = 0.0,step = 0.01)
st.sidebar.write("Equillibrium Relation used:")
st.sidebar.latex(r'''y=\ \frac{Kx}{1+Kx}''')
K = st.sidebar.slider("Equillibrium Constant (K)",min_value=0.0,max_value=10.0,value = 2.0,step = 0.001)
x = []
y = []
x_o = [x_in,x_out]
y_o = [y_out,y_in]
i = 0.0
while i<y_in:
    x.append(i)
    c = (K*i)/(1+(K*i))
    y.append(c)
    i = i + 0.1
st.markdown('## Generated Equillibrium Data')
data = {'Mole fraction of Absorbate stream':x,'Mole fraction in Solvent':y}
st.dataframe(data,width=1000,height=1000)
m = (y_out-y_in)/(x_in-x_out)
c = y_in-(m*x_out)
x_stairs = [x_out]
y_stairs = [y_in]
def opline(y):
	x = (y-c)/m
	return x
def eql(x):
	y = K*x/(1+K*x)
	return y
x_new = x_out
x_plot = [x_out]
y_plot = [y_in]
stages = 0
while x_new > x_in:
	y_new = eql(x_new)
	x_plot.append(x_new)
	y_plot.append(y_new)
	x_new = opline(y_new)
	x_plot.append(x_new)
	y_plot.append(y_new)
	stages =stages + 1
plt.plot(x,y,x_o,y_o,x_plot,y_plot)
plt.xlabel("Mole ratio of Absorbate in Solvent")
plt.ylabel("Mole ration of Absorbate in Absorbate rich stream")
plt.title("No. of trays required")
st.pyplot()
st.write('Number of Stages required =',stages)
if st.button('Author'):
    st.balloons()
    st.write("""By:
    **_Sai Swaroop_  :sunglasses:""")
