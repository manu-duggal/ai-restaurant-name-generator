from langchain_classic.chains import LLMChain
from langchain_classic.chains import SequentialChain
from langchain_classic.prompts import PromptTemplate
from langchain_groq import ChatGroq
import streamlit as st
import os

groq_api_key = st.secrets.get("GROQ_API_KEY") 


llm = ChatGroq(
    model = 'llama-3.3-70b-versatile',
    temperature = 0.9,
    groq_api_key = groq_api_key,
    max_tokens = 400,
    max_retries = 2
)

def generate_restaurant_name_and_menu(cuisine):
    
    # Prompt for generating restaurant name
    prompt_name = PromptTemplate(input_variable = ['cuisine'],
                                 template = 'I want to open a restaurant for {cuisine} cuisine. Suggest me one good name for it and nothing else')

    # Restaurant name generation llm
    name_chain = LLMChain(llm= llm, prompt= prompt_name, output_key= 'restaurant_name')

    # Prompt for generating menu
    prompt_menu = PromptTemplate(input_variable= ['restaurant_name'],
                                 template = 'Suggest me a list of dishes for {restaurant_name} restaurant. Return it as a comma sepearated list of atmost 10 dishes and nothing else')

    # Menu generation llm 
    menu_chain = LLMChain(llm= llm, prompt= prompt_menu, output_key= 'menu_items')
    
    # Chaining both API calls
    chain = SequentialChain(chains= [name_chain, menu_chain],
                        input_variables= ['cuisine'],
                        output_variables= ['restaurant_name', 'menu_items'])

    response = chain.invoke({'cuisine': cuisine})
    
    return response

