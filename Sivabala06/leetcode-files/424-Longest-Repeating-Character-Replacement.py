class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        answer = 0

        for right in range(len(s)):

            if s[right] not in freq:
                freq[s[right]] = 0

            freq[s[right]] += 1

            ws = right - left + 1
            mf = max(freq.values())

            while ws - mf > k:
                freq[s[left]] -= 1
                left += 1

                ws = right - left + 1
                mf = max(freq.values())

            answer = max(answer, ws)

        return answer