import smtplib

my_mail = "Gmail"
password = "password" # type generation key
subject_text = "test"
body_text = "test"
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail, 
        to_addrs="addres",
        msg="Subject: {subject_text}\n\n {body_text}"
    )