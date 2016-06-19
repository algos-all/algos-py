import string


class SearchKMP:
    def __init__(self, pattern, letters=string.ascii_letters):
        self.pattern = pattern
        self.letters = letters

        if not pattern: return

        self.automat = {
            letter : {
                i : 0 for i in range(len(pattern))
            } for letter in letters
        }

        i, self.automat[pattern[0]][0] = 0, 1

        for j, p in enumerate(pattern[1:], 1):
            for letter in letters:
                self.automat[letter][j] = self.automat[letter][i]

            self.automat[p][j] = j + 1
            i = self.automat[p][i]

    def search(self, txt):
        i, j = 0, 0
        n, m = len(txt), len(self.pattern)

        while i < n and j < m:
            j = self.automat[txt[i]][j]
            i += 1

        if j == m:
            return i - m
        return n


class SearchBM:
    def __init__(self, pattern, letters=string.ascii_letters):
        self.pattern = pattern
        self.letters = letters

        self.rshifts = {letter : -1 for letter in letters}

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
