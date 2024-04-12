from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justify_texts = []
        line = []
        len_line = 0
        for it in range(len(words)+1):
            if it < len(words) and len(words[it]) + len_line <= maxWidth:
                len_line += len(words[it]) + 1
                line.append(words[it])
            else:
                num_characters = len_line - len(line)
                num_spaces = maxWidth - num_characters
                if len(line) == 1:
                    justify_texts.append(line[0] + ' ' * num_spaces)
                    if it < len(words):
                        line = [words[it]]
                        len_line = len(words[it]) + 1
                    continue
                elif it >= len(words):
                    justify_texts.append(' '.join(line) + ' ' * (num_spaces - len(line) + 1))
                    continue
                num_spaces_per_word = num_spaces // (len(line) - 1)
                remains_spaces = num_spaces % (len(line) - 1)
                sapces_list = []
                for _ in range(len(line) - 1):
                    num_spaces_after = num_spaces_per_word + 1 if remains_spaces > 0 else num_spaces_per_word
                    remains_spaces -= 1
                    sapces_list.append(' ' * num_spaces_after)
                tmp_list = []
                for i, w in enumerate(line):
                    tmp_list.append(w)
                    if i < len(line) - 1:
                        tmp_list.append(sapces_list[i])
                justify_texts.append(''.join(tmp_list))
                if it < len(words):
                    line = [words[it]]
                    len_line = len(words[it]) + 1
        return justify_texts


solution = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
assert solution.fullJustify(words, maxWidth) == [
   "This    is    an",
   "example  of text",
   "justification.  "
]
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
assert solution.fullJustify(words, maxWidth) == [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
assert solution.fullJustify(words, maxWidth) == ["What   must   be","acknowledgment  ","shall be        "]
