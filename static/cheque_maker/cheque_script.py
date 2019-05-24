from PIL import Image,ImageDraw,ImageFont
from num2words import num2words

"""

This function generate_cheque creates a id.jpg image which is a dummy cheque made using the given parameters.
amount_in_figure represents the numeric value of the amount.
date_of_issue is a string and contains a date to be printed.
reciever_name is a string which takes the reciever name as input

Returns path of the saved image
"""





def generate_cheque(id,amount_in_figure,date_of_issue,reciever_name):

    date_of_issue=str(date_of_issue)
    amount_words=num2words(amount_in_figure, to = 'currency',lang='en_IN')
    amount_words=amount_words.capitalize()
    amount_words=amount_words.replace("euro","rupees").replace("cents","paise")

    im=Image.open("static/cheque_maker/dummyCheque.jpg")
    draw = ImageDraw.Draw(im)


    if (len(amount_words) > 64):
        temp=amount_words[55:].split(" ")
        amount_in_words=amount_words[0:55]+temp[0]
        del temp[0]
        amount_in_words_2=" ".join(temp)

    else :
        amount_in_words=amount_words
        amount_in_words_2=""



    fill_color="rgb(0,0,0)" # black


    font=ImageFont.truetype("static/cheque_maker/Roboto-Bold.ttf",size=20)


    draw.text((80,65),reciever_name,font=font,fill=fill_color,)

    draw.text((110,100),amount_in_words,font=font,fill=fill_color)
    draw.text((20,135),amount_in_words_2,font=font,fill=fill_color)

    draw.text((670,12),date_of_issue,font=font,fill=fill_color)


    font_2=ImageFont.truetype("static/cheque_maker/Roboto-Bold.ttf",size=25)

    draw.text((600,135),str(amount_in_figure),font=font_2,fill=fill_color)


    
    # im.show() #USE FOR DEBUGGING
    im.save(f"static/cheque_maker/outputs/{id}.jpg")
    return f"static/cheque_maker/outputs/{id}.jpg"
