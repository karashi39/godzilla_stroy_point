import base64

EMAIL_FILE = "./secrets/jira-email"
TOKEN_FILE = "./secrets/jira-token"
AUTH_FILE = "./secrets/jira_token.py"

# get email
try:
    with open(EMAIL_FILE, "r") as f:
        line = f.read()
        email = line.strip()
except FileNotFoundError:
    print(f"require Jira user email in {EMAIL_FILE}")
    exit()

# get token
try:
    with open(TOKEN_FILE, "r") as f:
        line = f.read()
        token = line.strip()
except FileNotFoundError:
    print(f"require Jira token in {TOKEN_FILE}")
    print("https://id.atlassian.com/manage-profile/security/api-tokens")
    exit()

# encode base64
b = f"{email}:{token}".encode()
b64 = base64.b64encode(b)
s64 = b64.decode()

# output authorization file
with open(AUTH_FILE, "w") as f:
    f.write(f'jira_token = "{s64}"')
