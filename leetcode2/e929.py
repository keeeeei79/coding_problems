class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()
        for email in emails:
            s = ""
            i = 0
            while i < len(email):
                if email[i] == ".":
                    pass
                elif email[i] == "+":
                    while email[i] != "@":
                        i += 1
                    s += email[i:]
                    break
                elif email[i] == "@":
                    s += email[i:]
                    break
                else:
                    s += email[i]
                i += 1
            uniq.add(s)
        return len(uniq)
