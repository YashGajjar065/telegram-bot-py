from datetime import datetime
from telegram.ext import *


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "Hey! how's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I am your hackers_bots"

    if user_message in ("Choose your Subject type", "who are you?"):
        return "I am your hackers_bots"
# ----------------English_code_links--------------------------------
    if user_message in ("/1101"):
        return "Link : https://www.google.com"

    elif user_message in ("/1111"):
        return "Link : https://drive.google.com/drive/folders/1BAONmAA0sQmaL8PtUDkW7fxclZr1-2Qz?usp=sharing"

    elif user_message in ("/1102"):
        return "Link : https://www.google.com"

    elif user_message in ("/1103"):
        return "Link : https://www.youtube.com"

    elif user_message in ("/1113"):
        return "Link : https://www.youtube.com"

    elif user_message in ("/1104"):
        return "Link : https://www.youtube.com"
        
    elif user_message in ("/1114"):
        return "Link : https://www.docs.com"

    elif user_message in ("/1105"):
        return "Link : https://www.docs.com"

    elif user_message in ("/1106"):
        return "Link : https://www.docs.com"

    elif user_message in ("/1116"):
        return "Link : http://Codingwithyash.epizy.com"

    elif user_message in ("/1107"):
        return "Link : http://Codingwithyash.epizy.com"

    elif user_message in ("/1108"):
        return "Link : http://Codingwithyash.epizy.com"

    elif user_message in ("/1118"):
        return "Link : http://Codingwithyash.epizy.com"
#-------------------English_link_complete------------------------------------
    
# -------------------Psychological_link_complete--------------------------------
    elif user_message in ("/0112"):
        return "Link : https://docs.google.com/document/d/1ujOYSriTqQ4EGil-8IMByDJvFKg_2Bq3YUuOF532atU/edit?usp=sharing"

    elif user_message in ("/0212"):
        return "Link : https://drive.google.com/file/d/1fBmt1FFPwu9iX4tVweRIqR6hG5EgBi7v/view?usp=sharing"

    elif user_message in ("/0312"):
        return "Link : https://docs.google.com/document/d/1HtnxxMuE-qseOMcoiqxPGPC1kI-d9qyV8FbXGeM_fbo/edit?usp=sharing"

    elif user_message in ("/0412"):
        return "Link : https://docs.google.com/document/d/1PqrnIA8j129qrqZK1X9tqRQ-9aKqx7Cv/edit?usp=sharing&ouid=100546146135422748707&rtpof=true&sd=true"

    elif user_message in ("/0512"):
        return "Link : https://docs.google.com/document/d/1VG-O8p27Z5lrIuqelbuegdEEwi7KDdIjEHXdCzIf3f0/edit?usp=sharing"

    elif user_message in ("/0612"):
        return "Link : https://docs.google.com/document/d/1Q8HZm4Y7nmnwvcPdIlPqwca9p-_AfxpsW7UcQgRucxc/edit?usp=sharing"
        
    elif user_message in ("/0712"):
        return "Link : https://docs.google.com/document/d/1Ed-pwguc10hQyJ1CPAm73sxbAXhcJr4dTX60LXahmpY/edit?usp=sharing"

    elif user_message in ("/0812"):
        return "Link : https://docs.google.com/document/d/1WUfFayCjzUigL30Q4Me6Q9WnmifTgREonHz2_p6-GBQ/edit?usp=sharing"

    elif user_message in ("/0912"):
        return "Link : https://docs.google.com/document/d/1MZjdlqG5sfF4kDE_WPP6JWwI5inVAaFM2Ib1242pQs4/edit?usp=sharing"

# -------------------Psychological_link_complete--------------------------------
    
    if user_message in ("Choose your phishing type method", "who are you?"):
        return "I am your hackers_bots"

    if user_message in ("time", "time?",):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "I don't understand you."
