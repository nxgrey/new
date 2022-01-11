from PIL import Image
from utils.certificate_no import CertificateNo

from utils.draw import Draw
from utils.print import Print
from utils.save_img import SaveImage
from utils.src import Source
from utils.clear_entry import ClearEntry
from utils.insert_default_value import InsertDefault

'''
    default background image
    background_front: [default front background]
    background_back: [default back background]
'''
background_front = Image.open(Source().default_gold_front)
background_back = Image.open(Source().default_gold_back)

'''
    Fonts
'''
font_title = Source().font_title
font_text = Source().font_text

'''
    Color
'''
color_title = Source().COLOR_TITLE
color_text = Source().COLOR_TEXT

class Gold:
    def __init__(self, obj):
        self.obj = obj

    def set_value(self):
        '''
            '''''''''''''''''''''''''''''''''''''''''''''''''FRONT CARD STYLE'''''''''''''''''''''''''''''''''''''''''''''''''
        '''

        # product image
        product_image = Draw(self.obj.entry_product_img, background_front, 2300, 600)
        product_image.adding_image(1800, 1400)

        # jewellery name on front of the card
        jewellery_front_name = Draw(self.obj.entry_jewellery_name, background_front, background_front.width, 100, color_title, font_title, 190)
        jewellery_front_name.title_text("u")

        # Customer name
        customer_name = Draw(self.obj.entry_customer_name, background_front, 1038, 755, color_text, font_text, 90)
        customer_name.adding_text()

        # date
        date_in = Draw(self.obj.entry_date, background_front, 1038, 1055, color_text,  font_text, 90)
        date_in.adding_text()

        # product name
        product_name = Draw(self.obj.entry_product_name, background_front, 1038, 1205, color_text,  font_text, 90)
        product_name.adding_text()

        # product weight
        product_weight = Draw(self.obj.entry_product_weight, background_front, 1038, 1355, color_text,  font_text, 90)
        product_weight.adding_text_with_unit("Gm")

        # product karate
        product_karate = Draw(self.obj.entry_product_karate, background_front, 1038, 1505, color_text,  font_text, 90)
        product_karate.adding_text_with_unit("Ct")

        # gold value
        gold_value = Draw(self.obj.entry_gold_value, background_front, 600, 2000, color_text,  font_text, 90)
        gold_value.adding_text_with_unit("%")

        # silver value
        silver_value = Draw(self.obj.entry_silver_value, background_front, 600, 2170, color_text,  font_text, 90)
        silver_value.adding_text_with_unit("%")

        # copper value
        copper_value = Draw(self.obj.entry_coper_value, background_front, 1670, 2000, color_text,  font_text, 90)
        copper_value.adding_text_with_unit("%")

        # other value
        other_value = Draw(self.obj.entry_other_value, background_front, 1670, 2170, color_text,  font_text, 90)
        other_value.adding_text_with_unit("%")

        # certificate_no
        number = CertificateNo().get_no()

        print(number)

        certificate_no = Draw(number, background_front, 1038, 905, color_text,  font_text, 90)
        certificate_no.adding_certificate_number()

        '''
            '''''''''''''''''''''''''''''''''''''''''''''''''BACK CARD STYLE'''''''''''''''''''''''''''''''''''''''''''''''''
        '''

        # QR code
        qr_img = Draw(self.obj.entry_qr_img, background_back, 3790, 200)
        qr_img.adding_qr_img(450, 450)

        # jewellery name on back of the card
        jewellery_back_name = Draw(self.obj.entry_jewellery_name, background_back, background_back.width, 350, color_text,  font_title, 125)
        jewellery_back_name.title_text("u")

        # adress
        jewellery_back_adress = Draw(self.obj.entry_adress, background_back, background_back.width, 500, color_text,  font_text, 90)
        jewellery_back_adress.title_text("l")

    def print_card(self):
        front_card = SaveImage(background_front, "saved/gold_front_format", "saved/gold_front_print_format")
        front_card.save()
        gold_card_front_print = Print("gold_front_print_format")
        gold_card_front_print.print_hard_copy()

        back_card = SaveImage(background_back, "saved/gold_back_format", "saved/gold_back_print_format")
        back_card.save()
        gold_card_back_print = Print("gold_back_print_format")
        gold_card_back_print.print_hard_copy()

        ClearEntry(self.obj).clear()
        InsertDefault(self.obj).insert_default_value_to_entry()