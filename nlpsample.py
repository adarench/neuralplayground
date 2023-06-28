
import nltk
nltk.download('punkt')
nltk.download('stopwords')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class SymptomCheckerBot:

    def __init__(self):
        self.symptom_map = {
            'headache': 'You might have a migraine or tension headache. Please consult a doctor.',
            'cough': 'You might have a common cold. If the cough persists, please consult a doctor.',
            'fever': 'You might have a flu or another type of infection. Please consult a doctor immediately.',
        }
        self.stop_words = set(stopwords.words('english'))

    def chat(self):
        print("Hello, I'm your symptom checker bot. Please describe your symptom.")
        while True:
            user_input = input()
            if user_input == 'quit':
                break

            response = self.respond_to(user_input)
            print(response)

    def extract_keywords(self, user_input):
        tokenized = word_tokenize(user_input)
        keywords = [word for word in tokenized if not word in self.stop_words]
        return keywords

    def respond_to(self, user_input):
        keywords = self.extract_keywords(user_input)
        for keyword in keywords:
            if keyword in self.symptom_map:
                return self.symptom_map[keyword]
        return "I'm sorry, I don't recognize that symptom. Please consult with a healthcare professional."

if __name__ == '__main__':
    bot = SymptomCheckerBot()
    bot.chat()
