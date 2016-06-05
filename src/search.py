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


class SearchBM:
    def __init__(self, pattern, letters=string.ascii_letters):
        self.pattern = pattern
        self.letters = letters
        self.rshifts = {letter : -1 for letter in letters}

        for i, p in enumerate(pattern):
            self.rshifts[p] = i

    def search(self, txt):
        N, M = len(txt), len(self.pattern)

        i = 0
        while i <= N - M:
            skip = 0

            for j in range(M - 1, -1, -1):
                if txt[i + j] != self.pattern[j]:
                    skip = max(1, j - self.rshifts[txt[i + j]])

                    break
            else:
                return i

            i += skip

        return N
