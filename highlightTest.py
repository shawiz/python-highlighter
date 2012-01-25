#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import highlight


class HighlightTestCase(unittest.TestCase):
    
    def testInSnippet(self):
        """
        inSnippet should give current result with known inputs
        """
        known_values = ((['case', 'for', 'iPhone', 'is', 'made'], 'iphone case', True),
                        (['I', 'love', 'the', 'deep', 'dish'], 'pizza dish', False),
                        (['game', 'starts', 'with', 'the', 'screen'], 'games screen', False),
                        (['game', 'starts', 'with', 'the', 'screen'], 'screen game', True))
        
        for sequence, query, value in known_values:
            result = highlight.inSnippet(sequence, query)
            self.assertEqual(value, result)
    
    def testFindSentence(self):
        """
        findSentence should give current result with known inputs
        """
        doc = "I like fish. Little star's deep dish pizza sure is fantastic! Are there cats \
and other animals? Dogs are funny."

        known_values = ((doc, (0, 2), "I like fish."),
                        (doc, (2, 5), "I like fish. Little star's deep dish pizza sure is \
fantastic!"),
                        (doc, (11, 16), "Are there cats and other animals?"),
                        (doc, (11, 19), "Are there cats and other animals? Dogs are funny."),
                        (doc, (17, 19), "Dogs are funny."))
        for doc, snippet, sentence in known_values:
            result = highlight.findSentence(doc, snippet)
            self.assertEqual(sentence, result)

    def testHighlightSentence(self):
        """
        highlightSentence should give current result with known inputs
        """
        sentence = "In the 360-degree background is the Death Star and an earth-like planet, \
which come into view depending on which way you turn."
        known_values = ((sentence, "death star", "In the 360-degree background is the \
[[HIGHLIGHT]]Death Star[[ENDHIGHLIGHT]] and an earth-like planet, which come into view depending \
on which way you turn."),
                        (sentence, "death planet star", "In the 360-degree background is the \
[[HIGHLIGHT]]Death Star[[ENDHIGHLIGHT]] and an earth-like [[HIGHLIGHT]]planet[[ENDHIGHLIGHT]], \
which come into view depending on which way you turn."),
                        (sentence, "death Planet", "In the 360-degree background is the \
[[HIGHLIGHT]]Death[[ENDHIGHLIGHT]] Star and an earth-like [[HIGHLIGHT]]planet[[ENDHIGHLIGHT]], \
which come into view depending on which way you turn."))
        for sentence, query, highlighted in known_values:
            result = highlight.highlightSentence(sentence, query)
            self.assertEqual(highlighted, result)
    
    def testHighlightDoc(self):
        """
        highlightDoc should give current result with known inputs
        """
        doc = "The game starts with the scene from the original Star Wars inside the Millennium \
Falcon after they escape the Death Star and the TIE Fighters attack. You are Luke Skywalker in the \
gunner’s turret below, and you turn the iPhone to rotate around and shoot the attacking TIE Fighters \
while Han Solo and Princess Leah either encourage or heckle you depending on your skills. Let me \
guess, you are trying not to hit anyone. In the 360-degree background is the Death Star and an earth-like \
planet, which come into view depending on which way you turn. The game is completely immersive, and works \
especially well while sitting in a swivel office chair."
        
        known_values = ((doc, "death star", "The game starts with the scene from the original \
[[HIGHLIGHT]]Star[[ENDHIGHLIGHT]] Wars inside the Millennium Falcon after they escape the \
[[HIGHLIGHT]]Death Star[[ENDHIGHLIGHT]] and the TIE Fighters attack."),
                        (doc, "death star planet", "In the 360-degree background is the \
[[HIGHLIGHT]]Death Star[[ENDHIGHLIGHT]] and an earth-like [[HIGHLIGHT]]planet[[ENDHIGHLIGHT]], \
which come into view depending on which way you turn."),
                        (doc, "the star", "[[HIGHLIGHT]]The[[ENDHIGHLIGHT]] game starts with \
[[HIGHLIGHT]]the[[ENDHIGHLIGHT]] scene from [[HIGHLIGHT]]the[[ENDHIGHLIGHT]] original \
[[HIGHLIGHT]]Star[[ENDHIGHLIGHT]] Wars inside [[HIGHLIGHT]]the[[ENDHIGHLIGHT]] Millennium \
Falcon after they escape [[HIGHLIGHT]]the[[ENDHIGHLIGHT]] Death [[HIGHLIGHT]]Star[[ENDHIGHLIGHT]] \
and [[HIGHLIGHT]]the[[ENDHIGHLIGHT]] TIE Fighters attack."))
        for doc, query, highlighted in known_values:
            result = highlight.highlightDoc(doc, query)
            self.assertEqual(highlighted, result)
        
if __name__ == "__main__":
    unittest.main()