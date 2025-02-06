import imaplib
import email

class EmailFetcher:
    def fetch(self, email_account, password, imap_url='imap.gmail.com'):
        results = []
        try:
            mail = imaplib.IMAP4_SSL(imap_url)
            mail.login(email_account, password)
            mail.select('inbox')

            _, data = mail.search(None, 'ALL')
            for num in data[0].split():
                _, msg_data = mail.fetch(num, '(RFC822)')
                msg = email.message_from_bytes(msg_data[0][1])
                text = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                results.append({"email": email_account, "text": text})
        except Exception as e:
            print(f"Error fetching emails: {e}")
        return results
