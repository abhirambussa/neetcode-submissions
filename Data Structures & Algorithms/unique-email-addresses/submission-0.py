class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split('@')

            # ignore everything after '+'
            if '+' in local:
                local = local[:local.index('+')]

            # remove all '.'
            local = local.replace('.', '')

            unique.add(local + '@' + domain)

        return len(unique)
