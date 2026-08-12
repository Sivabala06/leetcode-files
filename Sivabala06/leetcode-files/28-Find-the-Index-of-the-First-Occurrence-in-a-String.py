class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)

        if needle in haystack:
            for i in range(0, len(haystack)):
                flag = True

                for j in range(0, len(needle)):
                    if i + j >= len(haystack):
                        flag = False
                        break

                    if haystack[i + j] != needle[j]:
                        flag = False
                        break

                if flag:
                    return i

        return -1