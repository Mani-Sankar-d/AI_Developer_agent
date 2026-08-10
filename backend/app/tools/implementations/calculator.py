from langchain_core.tools import tool

@tool
def calculator(expression:str):
    """Performs arithmetic calculations"""
    return eval(expression)