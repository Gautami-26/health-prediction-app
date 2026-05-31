import google.generativeai as genai

genai.configure(

    api_key="AQ.Ab8RN6Kk_ez9478pHjCVvqv3NzW-r3mJ0C6nrEordSe_gY9xhQ"

)

model = genai.GenerativeModel(

    "gemini-1.5-flash"

)


def health_prediction(

    glucose,

    haemoglobin,

    cholesterol

):

    prompt = f"""

    Predict possible health risk.

    Glucose: {glucose}

    Haemoglobin: {haemoglobin}

    Cholesterol: {cholesterol}

    Give short remarks.

    """

    response = model.generate_content(

        prompt

    )

    return response.text
