from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Buttons:
    replayBtn = 520, 670
    standBtn = 480, 665
    doubleBtn = 396, 671
    splitBtn = 339, 669
    splitNoBtn = 443, 669
    HitBtn = 320, 671
    noInsurance = 470, 670


class UserHands:
    none = 3337
    Twenty = 7759
    Nineteen = 7008
    Eighteen = 7604
    Seventeen = 5981
    Sixteen = 7179
    Fifteen = 6351
    Fourteen = 7169
    Thirteen = 6494
    Twelve = 6374
    Eleven = 5783
    Ten = 8318
    Nine = 6715
    Eight = 6961
    Seven = 4744
    Six = 6613
    Four = 6194


class DealerHands:
    Eleven = 6025
    Ten = 7492
    Nine = 8276
    Eight = 8243
    Seven = 5665
    Six = 7748
    Five = 6319
    Four = 7166
    Three = 6080
    Two = 5805
    none = 1485


class SplitHandsRight:
    Twenty = 8806
    Nineteen = 8043
    Eighteen = 8008
    Seventeen = 7186
    Sixteen = 8056
    Fifteen = 7576
    Fourteen = 8228
    Thirteen = 7290
    Twelve = 7651
    Eleven = 6912
    Ten = 8952
    Nine = 7421


class SplitHandsLeft:
    Twenty = 4606
    Nineteen = 3749
    Eighteen = 4467
    Seventeen = 3737
    Sixteen = 4329
    Fifteen = 3994
    Fourteen = 3983
    Thirteen = 3836
    Twelve = 3844
    #Eleven = never found
    Ten = 5979
    #Nine = never found


class Aces:
    RedAceLeft = 6184
    RedAceRight = 6266
    BlackAceLeft = 5860
    BlackAceRight = 5835


def restartgame():
    pyautogui.click(Buttons.replayBtn)
    pyautogui.click(Buttons.replayBtn)


def stand():
    pyautogui.click(Buttons.standBtn)

def hit():
    pyautogui.click(Buttons.HitBtn)


def double():
    pyautogui.click(Buttons.doubleBtn)


def split():
        print("split")
        pyautogui.click(Buttons.splitBtn)
        time.sleep(2)


def splitno():
        print("no split")
        pyautogui.click(Buttons.splitNoBtn)
        time.sleep(2)


def noinsurance():
    pyautogui.click(Buttons.noInsurance)
    pyautogui.click(Buttons.noInsurance)
    time.sleep(2)


def dealer():
    box = (396, 406, 407, 413)
    image2 = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image2)
    b = array(grayimage.getcolors())
    return b.sum()


def splits2():
    box = (326, 660, 355, 675)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    h = array(grayimage.getcolors())
    return h.sum()


def splitleft():
    box = (360, 528, 374, 536)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    d = array(grayimage.getcolors())
    return d.sum()


def splitright():
    box = (422, 522, 436, 536)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    x = array(grayimage.getcolors())
    return x.sum()


def hand():
    box = (391, 522, 405, 530)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    return a.sum()


def aceidentifier1():
    box = (366, 473, 373, 486)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    j = array(grayimage.getcolors())
    return j.sum()


def aceidentifier2():
    box = (390, 472, 396, 484)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    z = array(grayimage.getcolors())
    return z.sum()


def deal():
    while True:
        if hand() == UserHands.none:
            print("deal")
            restartgame()
            time.sleep(1.5)
        if hand() != UserHands.none:
            break


def dealerace():
    if dealer() == 6025:
        print("no insurance")
        noinsurance()


def twenty():
        if hand() == UserHands.Twenty:
            print("20")
            if splits2() == 15863:
                splitno()
            stand()


def twentyleft():
        if splitleft() == SplitHandsLeft.Twenty:
            print("20")
            if splits2() == 15863:
                splitno()
            stand()


def twentyright():
        if splitright() == SplitHandsRight.Twenty:
            print("20")
            if splits2() == 15863:
                splitno()
            stand()


def nineteen():
    while True:
        if hand() == UserHands.Nineteen:
            print("19")
            stand()
        else:
            break


def nineteenleft():
    while True:
        if splitleft() == SplitHandsLeft.Nineteen:
            print("19")
            stand()
        else:
            break


def nineteenright():
    while True:
        if splitright() == SplitHandsRight.Nineteen:
            print("19")
            stand()
        else:
            break


def eighteen():
    while True:
        if hand() == UserHands.Eighteen:
            print("18")
            if splits2() == 15863:
                eighteensplit0()
            elif aceidentifier1() == Aces.RedAceLeft:
                print("soft")
                dealereighteena()
            elif aceidentifier1() == Aces.BlackAceLeft:
                print("soft")
                dealereighteena()
            elif aceidentifier2() == Aces.RedAceRight:
                print("soft")
                dealereighteena()
            elif aceidentifier2() == Aces.BlackAceRight:
                print("soft")
                dealereighteena()
            else:
                stand()
        else:
            break


def dealereighteena():
    if dealer() == DealerHands.Three:
        double()
    elif dealer() == DealerHands.Four:
        double()
    elif dealer() == DealerHands.Five:
        double()
    elif dealer() == DealerHands.Six:
        double()
    elif dealer() == DealerHands.Nine:
        hit()
    elif dealer() == DealerHands.Ten:
        hit()
    elif dealer() == DealerHands.Eleven:
        hit()
    else:
        stand()


def eighteensplit0():
    if dealer() == DealerHands.Eleven:
        splitno()
        time.sleep(2)
        stand()
    if dealer() == DealerHands.Ten:
        splitno()
        time.sleep(2)
        stand()
    if dealer() == DealerHands.Seven:
        splitno()
        time.sleep(2)
        stand()
    if dealer() == DealerHands.Nine:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Eight:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Six:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Five:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Four:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Three:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Two:
        split()
        time.sleep(2)
        splitmain()


def eighteenleft():
    while True:
        if splitleft() == SplitHandsLeft.Eighteen:
            print("18")
            if splits2() == 15863:
                splitno()
            stand()
        else:
            break


def eighteenright():
    while True:
        if splitright() == SplitHandsRight.Eighteen:
            print("18")
            if splits2() == 15863:
                splitno()
            stand()
        else:
            break


def seventeen():
    while True:
        if hand() == UserHands.Seventeen:
            print("17")
            if aceidentifier1() == Aces.RedAceLeft:
                print("soft")
                dealerseventeena()
            elif aceidentifier1() == Aces.BlackAceLeft:
                print("soft")
                dealerseventeena()
            elif aceidentifier2() == Aces.RedAceRight:
                print("soft")
                dealerseventeena()
            elif aceidentifier2() == Aces.BlackAceRight:
                print("soft")
                dealerseventeena()
            else:
                stand()
        if hand() != UserHands.Seventeen:
            break


def dealerseventeena():
    if dealer() == DealerHands.Three:
        double()
    elif dealer() == DealerHands.Four:
        double()
    elif dealer() == DealerHands.Five:
        double()
    elif dealer() == DealerHands.Six:
        double()
    else:
        hit()


def seventeenleft():
    while True:
        if splitleft() == SplitHandsLeft.Seventeen:
            print("17")
            stand()
        if hand() != SplitHandsLeft.Seventeen:
            break


def seventeenright():
    while True:
        if splitright() == SplitHandsRight.Seventeen:
            print("17")
            stand()
        if hand() != SplitHandsRight.Seventeen:
            break


def sixteen():
    if hand() == UserHands.Sixteen:
        print("16")
        if splits2() == 15863:
            split()
            time.sleep(2)
            splitmain()
        elif aceidentifier1() == Aces.RedAceLeft:
            print("soft")
            dealersixteena()
        elif aceidentifier1() == Aces.BlackAceLeft:
            print("soft")
            dealersixteena()
        elif aceidentifier2() == Aces.RedAceRight:
            print("soft")
            dealersixteena()
        elif aceidentifier2() == Aces.BlackAceRight:
            print("soft")
            dealersixteena()
        else:
            dealer16()


def dealersixteena():
    if dealer() == DealerHands.Four:
        double()
    elif dealer() == DealerHands.Five:
        double()
    elif dealer() == DealerHands.Six:
        double()
    else:
        hit()


def sixteenleft():
    if splitleft() == SplitHandsLeft.Sixteen:
        if splits2() == 15863:
            splitno()
        dealer16()


def sixteenright():
    if splitright() == SplitHandsRight.Sixteen:
        if splits2() == 15863:
            splitno()
        dealer16()


def dealer16():
    if dealer() == 6025:
        print("dealer high")
        hit()
    elif dealer() == 7492:
        print("dealer high")
        hit()
    elif dealer() == 8276:
        print("dealer high")
        hit()
    elif dealer() == 8243:
        print("dealer high")
        hit()
    elif dealer() == 5665:
        print("dealer high")
        hit()
    else:
        print("dealer low")
        stand()


def fifteen():
    if hand() == UserHands.Fifteen:
        print("15")
        if aceidentifier1() == Aces.RedAceLeft:
            print("soft")
            dealersixteena()
        elif aceidentifier1() == Aces.BlackAceLeft:
            print("soft")
            dealersixteena()
        elif aceidentifier2() == Aces.RedAceRight:
            print("soft")
            dealersixteena()
        elif aceidentifier2() == Aces.BlackAceRight:
            print("soft")
            dealersixteena()
        else:
            dealer16()


def fifteenleft():
    if splitleft() == SplitHandsLeft.Fifteen:
        print("15")
        dealer16()


def fifteenright():
    if splitright() == SplitHandsRight.Fifteen:
        print("15")
        dealer16()


def fourteen():
    if hand() == UserHands.Fourteen:
        print("14")
        if splits2() == 15863:
            fourteensplit0()
        elif aceidentifier1() == Aces.RedAceLeft:
            print("soft")
            dealerfourteena()
        elif aceidentifier1() == Aces.BlackAceLeft:
            print("soft")
            dealerfourteena()
        elif aceidentifier2() == Aces.RedAceRight:
            print("soft")
            dealerfourteena()
        elif aceidentifier2() == Aces.BlackAceRight:
            print("soft")
            dealerfourteena()
        else:
            dealer16()


def dealerfourteena():
    if dealer() == DealerHands.Five:
        double()
    elif dealer() == DealerHands.Six:
        double()
    else:
        hit()


def fourteensplit0():
    if dealer() == DealerHands.Eleven:
        splitno()
        time.sleep(2)
        hit()
    if dealer() == DealerHands.Ten:
        splitno()
        time.sleep(2)
        hit()
    if dealer() == DealerHands.Seven:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Nine:
        splitno()
        time.sleep(2)
        hit()
    if dealer() == DealerHands.Eight:
        splitno()
        time.sleep(2)
        hit()
    if dealer() == DealerHands.Six:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Five:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Four:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Three:
        split()
        time.sleep(2)
        splitmain()
    if dealer() == DealerHands.Two:
        split()
        time.sleep(2)
        splitmain()


def fourteenleft():
    if splitleft() == SplitHandsLeft.Fourteen:
        print("14")
        dealer16()


def fourteenright():
    if splitright() == SplitHandsRight.Fourteen:
        print("14")
        dealer16()


def thirteen():
    if hand() == UserHands.Thirteen:
        print("13")
        if aceidentifier1() == Aces.RedAceLeft:
            print("soft")
            dealerfourteena()
        elif aceidentifier1() == Aces.BlackAceLeft:
            print("soft")
            dealerfourteena()
        elif aceidentifier2() == Aces.RedAceRight:
            print("soft")
            dealerfourteena()
        elif aceidentifier2() == Aces.BlackAceRight:
            print("soft")
            dealerfourteena()
        else:
            dealer16()


def thirteenleft():
    if splitleft() == SplitHandsLeft.Thirteen:
        print("13")
        dealer16()


def thirteenright():
    if splitright() == SplitHandsRight.Thirteen:
        print("13")
        dealer16()


def twelve():
    if hand() == UserHands.Twelve:
        print("12")
        if aceidentifier1() == Aces.RedAceLeft:
            print("soft")
            split()
            time.sleep(2)
            splitmain()
        elif aceidentifier1() == Aces.BlackAceLeft:
            print("soft")
            split()
            time.sleep(2)
            splitmain()
        elif aceidentifier2() == Aces.RedAceRight:
            print("soft")
            split()
            time.sleep(2)
            splitmain()
        elif aceidentifier2() == Aces.BlackAceRight:
            print("soft")
            split()
            time.sleep(2)
            splitmain()
        elif splits2() == 15863:
            twelvesplits0()
        else:
            dealer12()


def twelvesplits0():
    if dealer() == DealerHands.Three:
        split()
        time.sleep(2)
        splitmain()
    elif dealer() == DealerHands.Four:
        split()
        time.sleep(2)
        splitmain()
    elif dealer() == DealerHands.Five:
        split()
        time.sleep(2)
        splitmain()
    elif dealer() == DealerHands.Six:
        split()
        time.sleep(2)
        splitmain()
    else:
        splitno()
        hit()


def twelveleft():
    if splitleft() == SplitHandsLeft.Twelve:
        print("12")
        dealer12()


def twelveright():
    if splitright() == SplitHandsRight.Twelve:
        print("12")
        dealer12()


def dealer12():
    if dealer() == 7748:
        print("stand")
        stand()
    if dealer() == 6319:
        print("stand")
        stand()
    if dealer() == 7166:
        print("stand")
        stand()
    if dealer() == 6025:
        print("hit")
        hit()
    if dealer() == 7492:
        print("hit")
        hit()
    if dealer() == 8276:
        print("hit")
        hit()
    if dealer() == 8243:
        print("hit")
        hit()
    if dealer() == 5665:
        print("hit")
        hit()
    if dealer() == 6080:
        print("hit")
        hit()
    if dealer() == 5805:
        print("hit")
        hit()


def eleven():
    if hand() == UserHands.Eleven:
        print("11")
        dealer11()


#def elevenleft():
    #if splitleft() == SplitHandsRight.Eleven:
        #print("11")
        #dealer11()


def elevenright():
    if splitright() == SplitHandsRight.Eleven:
        print("11")
        dealer11()


def dealer11():
    if dealer() == 6025:
        print("hit")
        hit()
    else:
        print("double")
        double()


def ten():
    if hand() == UserHands.Ten:
        print("10")
        if splits2() == 15863:
            splitno()
            dealer10()
        else:
            dealer10()


def tenleft():
    if splitleft() == SplitHandsLeft.Ten:
        print("10")
        dealer10()


def tenright():
    if splitright() == SplitHandsRight.Ten:
        print("10")
        dealer10()


def dealer10():
    if dealer() == 6025:
        hit()
    elif dealer() == 7492:
        hit()
    else:
        double()


def nine():
    if hand() == UserHands.Nine:
        print("9")
        dealer9()


def dealer9():
    if dealer() == 6080:
        double()
    elif dealer() == 7166:
        double()
    elif dealer() == 6319:
        double()
    else:
        hit()


#def nineleft():
    #if splitleft() == SplitHandsLeft.Nine:
        #print("nine")
        #dealer9()


def nineright():
    if splitright() == SplitHandsRight.Nine:
        print("nine")
        dealer9()


def eight():
    if hand() == UserHands.Eight:
        print("8")
        splitno()
        hit()


def seven():
    if hand() == UserHands.Seven:
        print("7")
        hit()


def six():
    if hand() == UserHands.Six:
        print("6")
        if splits2() == 15863:
            if dealer() == DealerHands.Four:
                split()
            elif dealer() == DealerHands.Five:
                split()
            elif dealer() == DealerHands.Six:
                split()
            elif dealer() == DealerHands.Seven:
                split()
            else:
                splitno()
                hit()
        else:
             hit()


def four():
    if hand() == 6194:
        print("4")
        if splits2() == 15863:
            if dealer() == DealerHands.Eight:
                splitno()
            elif dealer() == DealerHands.Nine:
                splitno()
            elif dealer() == DealerHands.Ten:
                splitno()
            elif dealer() == DealerHands.Eleven:
                splitno()
            else:
                split()
                splitmain()
        else:
            hit()


def main():
    while True:
        cycle = 0
        deal()
        time.sleep(3.5)
        dealerace()
        while True:
            twenty()
            nineteen()
            eighteen()
            seventeen()
            sixteen()
            fifteen()
            fourteen()
            thirteen()
            twelve()
            eleven()
            ten()
            nine()
            eight()
            seven()
            six()
            cycle = cycle + 1
            if cycle == 5:
                hit()
                cycle = 0
            time.sleep(.1)
            if hand() == UserHands.none:
                break


def splitmain():
    splitcycle = 0
    while True:
        twentyleft()
        twentyright()
        nineteenleft()
        nineteenright()
        eighteenleft()
        eighteenright()
        seventeenleft()
        seventeenright()
        sixteenleft()
        sixteenright()
        fifteenleft()
        fifteenright()
        fourteenleft()
        fourteenright()
        thirteenleft()
        thirteenright()
        twelveleft()
        twelveright()
        #elevenleft()
        elevenright()
        tenleft()
        tenright()
        #nineleft()
        nineright()
        splitcycle = splitcycle + 1
        if splitcycle == 5:
            hit()
            splitcycle = 0
        if hand() == UserHands.none:
            break


main()
