class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line_words = []
        line_length = 0

        for word in words:
            # Check if adding this word exceeds line width
            if line_length + len(word) + len(line_words) > maxWidth:
                # Time to justify current line
                spaces = maxWidth - line_length
                gaps = len(line_words) - 1

                # If only one word → left justify
                if gaps == 0:
                    res.append(line_words[0] + ' ' * spaces)
                else:
                    # Divide spaces evenly
                    even = spaces // gaps
                    extra = spaces % gaps
                    line = ''
                    for i in range(gaps):
                        # extra spaces go to leftmost gaps
                        line += line_words[i] + ' ' * (even + (1 if i < extra else 0))
                    line += line_words[-1]
                    res.append(line)

                # Reset for new line
                line_words = []
                line_length = 0

            # Add word to current line
            line_words.append(word)
            line_length += len(word)

        # Handle the last line (left-justified)
        last_line = ' '.join(line_words)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)

        return res
