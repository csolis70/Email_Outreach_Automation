import pandas as pd
import re
import dns.resolver


def is_valid_syntax(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


def has_mx_record(domain):
    try:
        dns.resolver.resolve(domain, "MX")
        return True
    except Exception:
        return False


def validate_email(email):
    if not isinstance(email, str):
        return False

    email = email.strip().lower()

    if not is_valid_syntax(email):
        return False

    domain = email.split("@")[1]
    return has_mx_record(domain)


def validate_email_dataframe(df, email_column="Email"):
    df = df.copy()
    df["valid"] = df[email_column].apply(validate_email)

    valid_emails = df[df["valid"]]
    invalid_emails = df[~df["valid"]]

    print("Valid emails:", len(valid_emails))
    print("Invalid emails:", len(invalid_emails))

    return valid_emails, invalid_emails
