import streamlit as st

st.title("Streamlit app of VGU")
st.text("Welcome to streamlit app")
st.header("i am a header")
st.write("You acn write",10+5)
name = st.text_input("Enter your name:")
age = st.text_input("Enter  your age:")
st.write("Your name is:" ,name)
st.write("Your name is:" ,age)
st.selectbox("Enter your course :",["BCA","BTECH","MCA"])
if st.button("Clicked Button"):
    st.success("Clicked Button")
file = st.file_uploader("Upload your file")
if file:
    content = file.read
    st.write("File uploaded successfully !!!")


data = {"Name": ["TOM","JACK","POP","HARRAY", "Marks": [10,20,30,20]}
df = pd.DataFrame(date)


st.dataframe(df)

data = pd.dataframe({
    "Marks" : [10,20,30,20] })

st.line_chart(data)
st.bar_chart(data)

subject = ["Python", "C++","Java"]]
marks = [20,10,5]

fig, ax = plt.subplot()
ax.pies(marks, labels=Marks,autopct='%1.1f%')
st.pyplot(fig)c
             
             
