# given a set of policies, generate possible password variants in order to crack hashes

import re, random, string

def extract_words(text):
        return re.findall(r'\b[a-zA-Z]{2,}\b', text)

def generate(text, count):
        words = extract_words(text)
        for _ in range(count):
                chosen = random.sample(words, 1)[0]
                chosen = random.choice([chosen.replace("a", "@", random.randint(1, 2)), chosen])
                chosen = random.choice([chosen.replace("o", "0"), chosen])
                chosen = random.choice([chosen.replace("i", "1"), chosen])
                chosen += random.choice(["05", "1998", "08"])
                chosen += random.choice('#!@$%^&*"')

                if len(chosen) >= 12:
                        print(chosen)

def main():

        text = ""

        generate(text, 10000000)
main()
