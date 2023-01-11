class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for m in emails:
            l, d = m.split("@", 1)
            l2 = l.split("+", 1)[0].replace(".", "")
            s.add(l2 + "@" + d)
        return len(s)
