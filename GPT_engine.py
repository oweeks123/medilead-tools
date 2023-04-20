import pandas as pd
import openai
from GPT_prompts import extract_point

note_input = "34 female, 3 days of dysuria, frequency, haematuria, fever, not responded to abx, ref urology"

notes = (f"{note_input}")

prompt = f"summarize paragraph in a letter format starting with Dear colleague: {notes}"

class NoteEngine:
    # Define OpenAI API key 
    openai.api_key = "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"
    # Set up the model and prompt
    model_engine = "text-curie-001"
    def __init__(self, note_input, task):
        self.note_input = note_input
        self.question = task
        self.prompt = f"{task}: {note_input}"
    def GPT_engine(self):
        # Generate a response
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=self.prompt,
            max_tokens=1500,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        return response


print(NoteEngine(notes, prompt).GPT_engine())