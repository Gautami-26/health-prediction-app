def health_prediction(
        glucose,
        haemoglobin,
        cholesterol
):

    if glucose > 140 and cholesterol > 220:

        return "High diabetes/cardiac risk"

    elif haemoglobin < 11:

        return "Possible anemia"

    else:

        return "Normal risk"