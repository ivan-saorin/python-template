from fastapi import APIRouter
import streamlit as st

router = APIRouter()

@router.get("/")
async def read_root():
return {"message": "Welcome to Py Project API"}

@router.get("/gui")
async def gui():
st.title("Your Project GUI")
st.write("Welcome to the Streamlit GUI for Py Project!")
