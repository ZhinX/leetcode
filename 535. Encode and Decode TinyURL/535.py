import random


class Codec:
    def __init__(self):
        self.url_map = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        char_set = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        while True:
            short_postfix = ""
            for i in range(6):
                short_postfix += random.choice(char_set)
            if short_postfix in self.url_map:
                continue
            else:
                self.url_map["http://tinyurl.com/" + short_postfix] = longUrl
                return "http://tinyurl.com/" + short_postfix

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.url_map[shortUrl]


codec = Codec()
print codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))

