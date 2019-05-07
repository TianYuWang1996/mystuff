class lexicon(object):

    def __init__(self):
        self.lexicon = {"north": "direction",
                        "south": "direction",
                        "east": "direction",
                        "west": "direction",
                        "down": "direction",
                        "up": "direction",
                        "left": "direction",
                        "right": "direction",
                        "back": "direction",
                        "go": "verb",
                        "stop": "verb",
                        "kill": "verb",
                        "eat": "verb",
                        "the": "stop",
                        "in": "stop",
                        "of": "stop",
                        "from": "stop",
                        "at": "stop",
                        "it": "stop",
                        "door": "noun",
                        "bear": "noun",
                        "princess": "noun",
                        "cabinet": "noun"}

    def scan(self, input_text):
        words = input_text.split()
        words.reverse()
        word_tuples = []
        for i in range(len(words)):
            word = words.pop()
            if convert_number(word):
                word_tuples.append(("number", int(word)))
            else:
                if self.lexicon.get(word):
                    word_tuples.append((self.lexicon.get(word), word))
                else:
                    word_tuples.append(("error", word))
        return word_tuples

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

# 类的实例化
lexicon = lexicon()