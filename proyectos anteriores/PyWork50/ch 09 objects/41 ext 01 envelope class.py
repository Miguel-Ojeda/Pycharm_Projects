"""
Write an Envelope class, with two attributes, weight (a float, measuring grams)
and was_sent (a Boolean, defaulting to False).

There should be three methods:
(1) send, which sends the letter, and changes was_sent to True, but only
after the envelope has enough postage;
(2) add_postage, which adds postage equal to its argument; and
(3) postage_needed, which indicates how much postage the envelope needs total.

The postage needed will be the weight of the envelope times 10.

Now write a BigEnvelope class that works just like Envelope except
that the postage is 15 times the weight, rather than 10.
"""


class NotEnoughPostageError(Exception):
    pass


class Envelope:
    postage_multiplier = 10

    def __init__(self, weight):
        self.weight = weight
        self.was_sent = False
        self.postage = 0

    def add_postage(self, postage):
        self.postage += postage

    def postage_needed(self):
        return self.weight * self.postage_multiplier

    def send(self):
        if self.postage >= self.postage_needed():
            self.was_sent = True
        else:
            raise NotEnoughPostageError('El franqueo es insuficiente')


class BigEnvelope(Envelope):
    postage_multiplier = 15
