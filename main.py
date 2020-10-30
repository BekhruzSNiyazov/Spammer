import smtplib
import random
import time

message = """\
Subject: No subject here

"""

text = """
Founding Fathers of the United States, in order to safeguard Americans rights to Life, Liberty, and the Pursuit of Happiness and prevent the formation of tyranny, devised an intricate system consisting of constitutional checks and balances and competing branches of government. 
But the government is not the only entity that has the potential to become a threat to individual rights and liberties. As John Stuart Mill warned in his book On Liberty, there is another threat to freedom — tyranny of society over individual, and society’s “means of tyrannising are not restricted to the acts which it may do by the hands of its political functionaries”: “it leaves fewer means of escape, penetrating much more deeply into the details of life, and enslaving the soul itself.” 
Contemporary America is facing a triple threat to liberty: an intolerant and illiberal woke movement, Donald Trump, a national populist with authoritarian tendencies, and authoritarian China abroad. It seems that people are losing faith in foundational liberal values on all sides of the political spectrum.
President Trump has attacked the integrity of American democracy and undermined the rule of law, becoming the first president in the US history to refuse to commit to the peaceful transfer of power and to recognize the results of the election, while attempting to subvert and hijack it; assaulted the rule of law, using his power to commute sentence of former aides and pressure foreign countries to dig up dirt on his political opponent; shredded American federalism, threatening to cut off federal funding to states and cities that refuse to conform to his agenda. He made a mockery of America’s constitutional system, issuing executive orders at an unprecedented rate, turning the Justice Department into his personal law firm, waging war against his own government and using the CDC as “the fourth branch of government” to unilaterally create new regulations and laws — all bypassing Congress. He has embraced crony capitalism, profiting from his presidency and employing the power of the federal government to pick economic winners and losers. It should not come as a surprise that more than seventy former Republican national security officials, seven former GOP governors, twenty Republicans former attorneys, seven members of George W. Bush’s cabinet, four former GOP senators, and over twenty-four Republican members of Congress have endorsed Joe Biden for presidency.
"""

server = smtplib.SMTP("smtp.outlook.com", 587)
server.starttls()
server.login("email@example.com", "password")
for i in range(5):
    num = len(text.split())
    for i in range(num):
        message += text[random.randrange(num)]
    time.sleep(2)
    server.sendmail("email@example.com", "email2@example.com", message)
