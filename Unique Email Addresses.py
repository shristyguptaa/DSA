# Unique Email Addresses
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

# Solution 1
# O(n*m) n is number of elements and m is max(len) of email address
domain = set()
for email in emails:    # n times
    j = email.index('@')
    test = email[:j]
    email = test.replace(".",'')+email[j:]
    j = email.index('@')
    # temp = test + email
    if '+' in email:
        i = email.index('+')
        email = email[0:i]+email[j:]
    if email not in domain:
        domain.add(email)
return len(domain)
    
# Solution 2
ans = set()
for email in emails:
    local,domain = email.split('@')
    local = local.replace('.','')
    try:
        i = local.index('+')
    except:
        i = len(local)
    email = local[:i]+'@'+domain
    if email not in ans:
        ans.add(email)
return len(ans)
