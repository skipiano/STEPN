from PIL import Image, ImageGrab, ImageShow
import pytesseract as pt
from pynput import keyboard, mouse
import time


def scrapeSneaker():
    im = ImageGrab.grab(bbox=None)
    im_serial = im.crop((168, 348, 225, 362))
    serial = pt.image_to_string(im_serial)
    print("serial: " + serial)
    im_class = im.crop((60, 400, 120, 411))
    _class = pt.image_to_string(im_class)
    print("class: " + _class)
    im_level = im.crop((60, 430, 100, 440))
    level = pt.image_to_string(im_level)
    print("level: " + level)
    rarity = ""
    im_mint = im.crop((145, 456, 233, 468))
    mint = pt.image_to_string(im_mint)
    print("mint: " + mint)
    im_eff_tot = im.crop((300, 522, 332, 540))
    eff_tot = pt.image_to_string(im_eff_tot)
    print("eff_tot: " + eff_tot)
    im_luck_tot = im.crop((300, 550, 332, 570))
    luck_tot = pt.image_to_string(im_luck_tot)
    print("luck_tot: " + luck_tot)
    im_comf_tot = im.crop((300, 580, 332, 600))
    comf_tot = pt.image_to_string(im_comf_tot)
    print("comf_tot: " + comf_tot)
    im_res_tot = im.crop((300, 608, 332, 626))
    res_tot = pt.image_to_string(im_res_tot)
    print("res_tot: " + res_tot)
    im_sock_1 = im.getpixel((57, 154, 57, 154))
    sock_1 = pt.image_to_string(im_sock_1)
    print("sock 1: " + sock_1)
    im_sock_2 = im.getpixel((306, 154, 306, 154))
    sock_2 = pt.image_to_string(im_sock_2)
    print("sock 2: " + sock_2)
    im_sock_3 = im.getpixel((57, 295, 57, 295))
    sock_3 = pt.image_to_string(im_sock_3)
    print("sock 3: " + sock_3)
    im_sock_4 = im.getpixel((306, 295, 306, 295))
    sock_4 = pt.image_to_string(im_sock_4)
    print("sock 4: " + sock_4)
    im_price = im.crop((40, 666, 200, 694))
    price = pt.image_to_string(im_price)
    print("price: " + price)


def scrapeShoeBox():
    im_rarity = im.crop((50, 280, 320, 312))
    rarity = pt.image_to_string(im_rarity)
    print("rarity: " + rarity)
    im_serial = im.crop((168, 322, 221, 336))
    serial = pt.image_to_string(im_serial)
    print("serial: " + serial)
    im_price = im.crop((96, 355, 315, 378))
    price = pt.image_to_string(im_price)
    print("price: " + price)
    im_parent_1 = im.crop((100, 452, 150, 468))
    parent_1 = pt.image_to_string(im_parent_1)
    print("parent 1: " + parent_1)
    im_parent_2 = im.crop((252, 452, 302, 468))
    parent_2 = pt.image_to_string(im_parent_2)
    print("parent 2: " + parent_2)


def scrapeGem():
    im_type_class = im.crop((55, 335, 325, 364))
    _class = pt.image_to_string(im_type_class)
    print("class: " + _class)
    im_serial = im.crop((160, 380, 228, 393))
    serial = pt.image_to_string(im_serial)
    print("serial: " + serial)
    im_price = im.crop((100, 498, 316, 522))
    price = pt.image_to_string(im_price)
    print("price: " + price)


if __name__ == "__main__":
    time.sleep(2)
    scrapeSneaker()
