import pandas as pd
import openai
from GPT_prompts import extract_point

#note_input = "34 female, 3 days of dysuria, frequency, haematuria, fever, not responded to abx, ref urology"
#notes = (f"{note_input}")
#prompt = f"summarize paragraph in a letter format starting with Dear colleague: {notes}"

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

notes = """
Objectives: This review aims to: 1) evaluate the quality of model reporting, 2) provide an overview of methodology for developing and validating Early Warning Score Systems (EWSs) for adult patients in acute care settings, and 3) highlight the strengths and limitations of the methodologies, as well as identify future directions for EWS derivation and validation studies.
Methodology: A systematic search was conducted in PubMed, Cochrane Library, and CINAHL. Only peer reviewed articles and clinical guidelines regarding developing and validating EWSs for adult patients in acute care settings were included. 615 articles were extracted and reviewed by five of the authors. Selected studies were evaluated based on the Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis (TRIPOD) checklist. The studies were analyzed according to their study design, predictor selection, outcome measurement, methodology of modeling, and validation strategy.
Results: A total of 29 articles were included in the final analysis. Twenty-six articles reported on the development and validation of a new EWS, while three reported on validation and model modification. Only eight studies met more than 75% of the items in the TRIPOD checklist. Three major techniques were utilized among the studies to inform their predictive algorithms: 1) clinical-consensus models (n = 6), 2) regression models (n = 15), and 3) tree models (n = 5). The number of predictors included in the EWSs varied from 3 to 72 with a median of seven. Twenty-eight models included vital signs, while 11 included lab data. Pulse oximetry, mental status, and other variables extracted from electronic health records (EHRs) were among other frequently used predictors. In-hospital mortality, unplanned transfer to the intensive care unit (ICU), and cardiac arrest were commonly used clinical outcomes. Twenty-eight studies conducted a form of model validation either within the study or against other widely-used EWSs. Only three studies validated their model using an external database separate from the derived database.
Conclusion: This literature review demonstrates that the characteristics of the cohort, predictors, and outcome selection, as well as the metrics for model validation, vary greatly across EWS studies. There is no consensus on the optimal strategy for developing such algorithms since data-driven models with acceptable predictive accuracy are often site-specific. A standardized checklist for clinical prediction model reporting exists, but few studies have included reporting aligned with it in their publications. Data-driven models are subjected to biases in the use of EHR data, thus it is particularly important to provide detailed study protocols and acknowledge, leverage, or reduce potential biases of the data used for EWS development to improve transparency and generalizability
"""

prompt = 'summarize the article in bullet points'

print(NoteEngine(notes, prompt).GPT_engine())