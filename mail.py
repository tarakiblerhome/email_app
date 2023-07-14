def send_email(to,cc,bcc):
  if (len(to) + len(cc) + len(bcc)) > 99:
    return "Failed"
  for email in to:
    if '@' not in email:
      return "Failed"
  for email in cc:
    if '@' not in email:
      return "Failed"
  return "Success"