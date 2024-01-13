from lorem_text import lorem
import nltk
import random
from nltk.corpus import words, brown

# Hard Sentence
class SentenceGenerator:
    def __init__(self):
        self.words = set(words.words())
        self.brown_words = set(brown.words())

    def generate_sentence(self, length=30):
        sentence = []
        for _ in range(length):
            word = random.choice(list(self.words.union(self.brown_words)))
            sentence.append(word)
        return ' '.join(sentence)


def hardSentence():
    generator = SentenceGenerator()
    random_sentence = generator.generate_sentence()
    print(random_sentence)

    
# Medium Sentence
def mediumSentence():
        return lorem.words(30)
    



# Easy Sentence
def get_common_words_list():
    common_words = [
        "apple", "banana", "carrot", "dog", "elephant", "forest", "guitar", "happy", "island", "jazz",
        "kangaroo", "lemon", "mountain", "notebook", "orange", "penguin", "quilt", "rainbow", "sunflower", "tiger",
        "umbrella", "violin", "waterfall", "xylophone", "yoga", "zebra", "book", "chair", "desk", "door",
        "flower", "hat", "key", "lamp", "moon", "ocean", "piano", "quasar", "rocket", "star", "train",
        "umbrella", "vase", "waffle", "xylograph", "yard", "zipper", "cookie", "candle", "balloon", "basket",
        "cloud", "diamond", "echo", "feather", "globe", "hammer", "iguana", "jacket", "kite", "lighthouse",
        "maple", "noodle", "opal", "puzzle", "quilt", "raccoon", "sailboat", "toothbrush", "unicorn", "volcano",
        "whistle", "xylophone", "yogurt", "zeppelin", "atom", "bracelet", "chandelier", "dragonfly", "fireworks", "glacier",
        "hedgehog", "illusion", "jackal", "kaleidoscope", "lightning", "mango", "nougat", "octopus", "parachute", "quasar",
        "rattlesnake", "sculpture", "telescope", "umbilical", "vortex", "wombat", "xenon", "yak", "zephyr"
    ]
    
    return common_words

def generate_random_sentence(word_list, sentence_length=30):
    sentence = random.sample(word_list, min(sentence_length, len(word_list)))
    return ' '.join(sentence)


def easySentence():
    common_words_list = get_common_words_list()
    random_sentence = generate_random_sentence(common_words_list, sentence_length=30)
    return random_sentence

