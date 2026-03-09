def predict_anxiety(text):
    text = text.lower()

    high_words = ["panic", "fear", "can't sleep", "very stressed", "terrified"]
    moderate_words = ["nervous", "worried", "pressure", "tense"]
    
    for word in high_words:
        if word in text:
            return "High Anxiety"
    
    for word in moderate_words:
        if word in text:
            return "Moderate Anxiety"
    
    return "Low Anxiety"