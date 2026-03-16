def numUniqueEmails(emails):
    unique_emails = set()

    for email in emails:
        local, domain = email.split('@')
        
        # '+' ke baad ka part hata do
        if '+' in local:
            local = local[:local.index('+')]
        
        # '.' remove karo
        local = local.replace('.', '')
        
        # final email banao
        final_email = local + '@' + domain
        
        unique_emails.add(final_email)

    return len(unique_emails)


emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]

print(numUniqueEmails(emails))

emails = ["a@leetcode.com",
          "b@leetcode.com",
          "c@leetcode.com"]
print(numUniqueEmails(emails))


