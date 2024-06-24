#
# @lc app=leetcode id=831 lang=python3
#
# [831] Masking Personal Information
#


# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            email = s.split("@")

            email[0] = email[0].lower()
            email[1] = email[1].lower()

            email[0] = email[0][0] + "*****" + email[0][-1]

            email = "@".join(email)

            return email
        else:
            separationChars = ["+", "-", "(", ")", " "]
            phone = s

            for char in separationChars:
                phone = phone.replace(char, "")

            phone = (
                f"***-***-{phone[6:]}"
                if len(phone) == 10
                else f"+*-***-***-{phone[7:]}"
                if len(phone) == 11
                else f"+**-***-***-{phone[8:]}"
                if len(phone) == 12
                else f"+***-***-***-{phone[9:]}"
            )

            return phone


# @lc code=end
