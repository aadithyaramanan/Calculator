import streamlit as st 

def calculator(num1,num2,operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        if num2!=0:
            return num1/num2
        else:
            return "Division by zero is undefined error."
        
def main():
    st.title("Simple Calculator")
    num1=st.number_input("Enter the first number ",format="%f") 
    num2=st.number_input("Enter the second number ",format="%f") 
    operation=st.selectbox("Select Operation ",["+","-","*","/"])
    result=calculator(num1=num1,num2=num2,operation=operation)
    
    if st.button("Submit"):
        st.write(f"Result :{result}")
        st.balloons()
if __name__=="__main__":
    main()
            
           