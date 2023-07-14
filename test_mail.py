import pytest
from mail import *

VALID_EMAIL="JohnDoe@gmail.com"
INVALID_EMAIL="John"
SUCCESS_MSG="Success"
FAIL_MSG="Failed"

def test_valid_to():
    value = send_email([VALID_EMAIL],[],[])
    assert value == SUCCESS_MSG, f"Valid email {VALID_EMAIL} in To did not return {SUCCESS_MSG}"

def test_valid_cc():
    value = send_email([],[VALID_EMAIL],[])
    assert value == f"{SUCCESS_MSG}", f"Valid email {VALID_EMAIL} in CC did not return {SUCCESS_MSG}"

def test_valid_bcc():
    value = send_email([],[],[VALID_EMAIL])
    assert value == f"{SUCCESS_MSG}", f"Valid email {VALID_EMAIL} in BCC did not return {SUCCESS_MSG}"

def test_invalid_to():
    value = send_email([INVALID_EMAIL],[],[])
    assert value == f"{FAIL_MSG}", f"Invalid email {INVALID_EMAIL} in To did not return {FAIL_MSG}"

def test_invalid_cc():
    value = send_email([],[INVALID_EMAIL],[])
    assert value == f"{FAIL_MSG}", f"Invalid email {INVALID_EMAIL} in CC did not return {FAIL_MSG}"

def test_invalid_bcc():
    value = send_email([],[],[INVALID_EMAIL])
    assert value == f"{FAIL_MSG}", f"Invalid email {INVALID_EMAIL} in BCC did not return {FAIL_MSG}"

def test_one_invalid_email():
    value = send_email([VALID_EMAIL],[INVALID_EMAIL],[VALID_EMAIL])
    assert value == f"{FAIL_MSG}", f"Invalid email {INVALID_EMAIL} in one field did not return {FAIL_MSG}"

def test_one_invalid_email():
    list_of_emails = ""
    for x in range(0,99):
      list_of_emails = list_of_emails + VALID_EMAIL + str(x)
    value = send_email([list_of_emails],[],[])
    assert value == f"{SUCCESS_MSG}", f"99 emails in To field did not return {SUCCESS_MSG}"
