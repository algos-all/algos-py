import string


class SearchKMP:
    def __init__(self, pattern, letters=string.ascii_letters):
        self.pattern = pattern
        self.letters = letters

        if not pattern: return

        self.automat = {
            l : {i : 0 for i in range(len(pattern))} for l in letters
        }
        self.automat[pattern[0]][0] = 1

        i = 0

        for j, p in enumerate(pattern[1:], 1):
            for l in letters:
                self.automat[l][j] = self.automat[l][i]

            self.automat[p][j] = j + 1
            i = self.automat[p][i]

    def search(self, txt):
        i, j = 0, 0
        N, M = len(txt), len(self.pattern)

        while i < N and j < M:
            j = self.automat[txt[i]][j]
            i += 1

        if j == M:
            return i - M
        else:
            return N
