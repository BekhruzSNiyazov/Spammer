import smtplib
import time

message = """\
Subject: No subject here
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at faucibus risus. Proin imperdiet sollicitudin sapien, eu mollis elit mattis vel. Curabitur mauris ex, venenatis et dapibus id, convallis vitae arcu. Phasellus vestibulum sed nulla eget dignissim. Etiam urna mi, commodo id enim vitae, hendrerit malesuada odio. Phasellus molestie urna lacinia faucibus suscipit. Vestibulum commodo sapien est, a vulputate nisi laoreet imperdiet. Cras mi magna, venenatis sit amet varius ut, vulputate ac ligula. Aliquam viverra diam in nunc mattis, id auctor massa dictum. Mauris sapien lacus, cursus eget posuere fringilla, lobortis ac urna.
"""

server = smtplib.SMTP("smtp.outlook.com", 587)
server.starttls()
server.login("email@example.com", "password")
for i in range(10):
    time.sleep(2)
    server.sendmail("email@example.com", "email2@example.com", message)
