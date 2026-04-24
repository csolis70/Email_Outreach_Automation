import pandas as pd
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_emails(df, sender, subject_tmpl, body_tmpl, api_key=None, dry_run=True):
    """
    Send personalized emails from a dataframe using SendGrid.

    df: pandas DataFrame with at least 'Email' column
    sender: str, e.i, email that you want to send batch emails from
    subject_tmpl : str, may contain {placeholders}
    body_tmpl : str, may contain {placeholders}
    api_key : SendGrid API key (required if dry_run=False)
    dry_run : if True, print previews only
    """

    if not dry_run and not api_key:
        raise ValueError("API key required when dry_run=False")

    sg = SendGridAPIClient(api_key) if not dry_run else None

    for _, row in df.iterrows():
        ctx = {k: ("" if pd.isna(v) else v) for k, v in row.items()} 

        subject = subject_tmpl.format(**ctx)
        body = body_tmpl.format(**ctx)
        to_email = ctx["Email"]

        if dry_run:
            print(f"--- DRY RUN to {to_email} ---")
            print("Subject:", subject)
            print("Body:", body[:200], "...\n")
        else:
            message = Mail(
                from_email=sender,
                to_emails=to_email,
                subject=subject,
                html_content=body
            )

            try:
                response = sg.send(message)
                print(f"Sent to {to_email}, status {response.status_code}")
            except Exception as e:
                print(f"Error sending to {to_email}: {e}")
