import copy
import string


class SearchKMP:

    def __init__(self, pattern, letters=string.ascii_letters):
        self.pattern = pattern
        self.letters = letters

        if not pattern: return

        self.automat = {
            j: {letter: 0 for letter in letters}
            for j in range(len(pattern))
        }

        x, self.automat[0][pattern[0]] = 0, 1

        for j, p in enumerate(pattern[1:], 1):
            self.automat[j] = copy.copy(self.automat[x])

            self.automat[j][p] = j + 1

            x = self.automat[x][p]

    def search(self, txt):
        i, j = 0, 0
        n, m = len(txt), len(self.pattern)

        while i != n and j != m:
            j = self.automat[j][txt[i]]
            i += 1

        if j == m:
            return i - m
        return n


class SearchBM:

    def __init__(self, pattern, letters=string.ascii_letters):
        self.pattern = pattern
        self.letters = letters

        self.rshifts = {letter: -1 for letter in letters}

        for i, letter in enumerate(pattern):
            self.rshifts[letter] = i

    def search(self, txt):
        i, n, m = 0, len(txt), len(self.pattern)

        while i <= n - m:
            for j in range(m - 1, -1, -1):
                if txt[i + j] != self.pattern[j]:
                    i += max(1, j - self.rshifts[txt[i + j]])

                    break
            else:
                return i

        return n
