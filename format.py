class Format:

    text = []

    def __init__(self, raw_data, set_width):
        self.raw = raw_data
        self.width = set_width

    def done(self):
        text = []
        string = ""
        for part in self.raw:
            words = part.split()
            for word in words:
                if len(string) + len(word) < self.width or len(string) == 0:
                    string = string + word + " "
                else:
                    text.append(string)
                    string = word
            text.append(string)
            string = ""
            text.append(string)
        return text
