import pandas as pd
from GPT_engine import NoteEngine
import streamlit as st

dear_colleague = "summarize paragraph in a letter format, asking for an expert opinion, starting with Dear colleague thank you for seeing this, ending with yours sincerely:"
twimc = "summarize paragraph in a letter format starting with To whom it may concern, ending with yours faithfully"

# COMPLAINT RESPOMSE
extract_questions = " this document:"
answer_questions = "extract the questions that need answering from Paragraph-A and use information from Paragraph-B to formulate a compassionate letter answers to them: "

def main():
    menu = ['Letter Creator', 'Note Summarisor', 'Extract Features', 'Complaint Response']
    letter_format_choices = ['To colleague', 'To whom it may concern']

    side_menu = st.sidebar.selectbox('Menu', menu)

    # LETTER CREATOR
    if side_menu=='Letter Creator':
        st.title('Clinical Letter Creator')
        st.subheader('This tool uses the ChatGPT AI engine to create a referral letter from your clinic notes.')
        letter_format = st.selectbox('Letter format', letter_format_choices)
        note_input = st.text_area('Enter notes')

        if letter_format == 'To colleague':
            tasks = dear_colleague,
        elif letter_format == 'To whom it may concern':
            tasks = twimc,
        else: pass

        if st.button('Create'):
            output = NoteEngine(tasks, note_input).GPT_engine()
            st.write(output)
        else: pass
    else: pass

    # NOTE SUMMARISOR
    if side_menu=='Note Summarisor':

        note_method = ['Image', 'Text input', 'Text upload']

        st.title('Note Summarisor')
        st.subheader('This tool uses the ChatGPT AI engine to summarise clinical notes.')
        note_capture = st.selectbox('Note format', note_method)

        if note_capture == 'Text input':
            note_input = st.text_area('Enter notes')

            if st.button('Create'):
                output = NoteEngine(tasks, note_input).GPT_engine()
                st.write(output)

        if note_capture in ['Image','Text upload']:
            file_uploader = st.file_uploader('Select file')

            if st.button('Create'):
                output = NoteEngine(extract_questions, note_input).GPT_engine()
                st.write(output)
            else: pass
        else: pass

    if side_menu=='Complaint Response':
        st.title('Complaint Response Creator')
        st.subheader('This tool uses the ChatGPT AI engine to create a complaint response.')
        concern = st.text_area('Enter concern')
        case_summary = st.text_area('Enter case summary')

        if st.button('Formulate Response'):
            questions = NoteEngine(extract_questions, concern).GPT_engine()
            combined_prompt = f'{answer_questions} + " Paragraph-A: {concern}. Paragraph-B {case_summary}."'
            response = NoteEngine(extract_questions, combined_prompt).GPT_engine()
            st.write(response)
        else: pass
    else: pass        

if __name__ == '__main__':
    main()
