import ns
import csv
import streamlit as st
import pandas as pd
import os
import time
#import streamlit_authenticator as stauth  
#import database as db
import pyexcel as pe


st.set_page_config(page_title="PROFESSOR AI - SPLITTER", page_icon=":bar_chart:")

placeholder = st.empty()


authentication_status=True

if authentication_status:
    placeholder.empty()
    def save_input_file(input_file):
        with open(os.path.join("inputm.csv"), "wb") as f:
            f.write(input_file.getbuffer())
        return st.success("Source File Uploaded")

    st.title("PROFESSOR SATHISH- AI SPLITTER ")
    #authenticator.logout("Logout", "sidebar")

    col1, col2, col3 = st.columns(3)

    col4, col5 = st.columns([7,1])
    with col1:
        reg = st.selectbox(
            'Enter the regulation  13 | 17 | 21 : ',
            (13, 17, 21))

    with col2:  
        ass = st.selectbox(
            'Choose the assessment : ',
        ("IA1", "IA2", "MODEL", "Lab", "Project", "Custom"))
        

    if ass == "Custom":
        with col3:
            que_count = st.number_input('Enter the Question Count : ' , min_value=1, max_value=100, value=1, step=1)
            
   
    dep = None
    co_lister = []
    ms_lister = []
    if ass == "MODEL":
        dep = st.selectbox(
            'Choose the Department',
            ("S & H", "Other"))
    
    if dep == "S & H":
        dep = 1
    elif dep == "Other":
        dep = 2
    if ass == "Custom":
 
        st.markdown(f"""
                    <div style="margin-top:35px">
                    <div>
                    """, unsafe_allow_html=True)
        st.write("COPO NUMBERS")
        for i in range(que_count):
            # que = st.text_input(f"Enter the question {i+1} co number : ", placeholder="CO1")
            que = st.selectbox(f"Enter the question {i+1} co number : ",
            ("CO - 1", "CO - 2", "CO - 3", "CO - 4", "CO - 5", "CO - 6", "CO - 7", "CO - 8", "CO - 9", "CO - 10", "CO - 11", "CO - 12", "CO - 13", "CO - 14", "CO - 15", "CO - 16", "CO - 17", "CO - 18", "CO - 19", "CO - 20"))

            if que == "CO - 1":
                que = 1
            if que == "CO - 2":
                que = 2
            if que == "CO - 3":
                que = 3
            if que == "CO - 4":
                que = 4
            if que == "CO - 5":
                que = 5
            if que == "CO - 6":
                que = 6
            if que == "CO - 7":
                que = 7
            if que == "CO - 8":
                que = 8
            if que == "CO - 9":
                que = 9
            if que == "CO - 10":
                que = 10
            if que == "CO - 11":
                que = 11
            if que == "CO - 12":
                que = 12
            if que == "CO - 13":
                que = 13
            if que == "CO - 14":
                que = 14
            if que == "CO - 15":
                que = 15
            if que == "CO - 16":
                que = 16
            if que == "CO - 17":
                que = 17
            if que == "CO - 18":
                que = 18
            if que == "CO - 19":
                que = 19
            if que == "CO - 20":
                que = 20
            co_lister.append(que)
                
        st.markdown(f"""
                <div style="margin-top:35px">
                <div>
                """, unsafe_allow_html=True)
        st.write("COPO MARKS")
        for i in range(que_count):
            mque = st.selectbox(f"Enter the question {i+1} mark : ",
            (2, 8, 13, 15, 16, 20))
            ms_lister.append(mque)
        st.markdown(f"""
                <div style="margin-top:35px">
                    
                <div>
                """, unsafe_allow_html=True)
    with col4:
        file_name = st.text_input('Enter the Output File Name: ', placeholder="COPO_File")
    with col5:
        st.markdown(f"""
                    <div style="margin-top:35px">
                        
                    <div>
                    """, unsafe_allow_html=True)
        st.button("Submit")
        

    trunc_file = "inputm.csv"
    f = open(trunc_file, "w+")
    f.close()

    # if ass != "Custom":
    input_mark = st.text_area(f"Enter the marks of {ass}:  ")
    arr = [int(i) for i in input_mark.strip().split("\n") if i]
    
    with open("inputm.csv", 'a') as my_file:
        for i in arr:
            my_file.write(str(i) + "\n")
    
    
    
    
    if ass == "IA1":
        ass = 1
    elif ass == "IA2":
        ass = 2
    elif ass == "MODEL":
        ass = 3
    elif ass == "Lab":
        ass = 4
    elif ass == "Project":
        ass = 5
    elif ass == "Custom":
        ass = 6

    col7, col8, col9 = st.columns([1,4,1])

    def getbtn(btn_func):
        if btn_func:
            st.warning("Wait while Generating...")
            ns.ranCOS(reg, ass, file_name, dep, co_lister, ms_lister)
            df = pd.read_csv(f"{file_name}.csv",skiprows=2) 
            st.write(df) 
            time.sleep(3)
            if file_name is not None:
                pe.save_book_as(file_name=file_name+".csv", dest_file_name=f"{file_name}.xls")
                with open(file_name + ".xls", 'rb') as my_file:
                    with col9:
                        st.download_button(label = 'Download', data = my_file, file_name = file_name + '.xls', mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')   
            os.remove(file_name + ".csv")
            st.success("Generated Successfully!")
            
            time.sleep(2)
            try:
                os.remove(file_name + ".xls")
            except:
                print("File not found")
                
    with col8:
        st.empty()           
    with col7: 
        res_btn = st.button("Generate")      
    getbtn(res_btn)
