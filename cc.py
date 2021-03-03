from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import utils
from constants import *
from sys import argv



tempFile = None

def ccPDFmake(frontFile, backFile, saveFile, text):
    canvas = Canvas(saveFile)

    front = utils.ImageReader(frontFile)
    back = utils.ImageReader(backFile)

    canvas.drawImage(front, FRONT_X, FRONT_Y, width= CC_WIDTH, height=CC_HEIGHT, mask='auto')
    canvas.drawImage(back, BACK_X, BACK_Y, width= CC_WIDTH, height=CC_HEIGHT, mask='auto')

    if text != "":
        canvas.saveState()

        canvas.rotate(55)
        canvas.setFillColorRGB(.6,.6,.6)
        canvas.setFont("Times-Roman", 30)
        canvas.drawString(10*CM, 0.2*CM, text)
        canvas.restoreState()

    canvas.save()
    return True


def sentenceArgBuilder(argv):
    sentence = argv[4]
    for i in range(4, len(argv)):
        sentence += " "
        sentence += argv[i]
    return sentence


if __name__ == '__main__':
    if len(argv) > 4:
        ccPDFmake(argv[1], argv[2], argv[3], sentenceArgBuilder(argv))
    elif len(argv) == 4:
        ccPDFmake(argv[1], argv[2], argv[3], '')
    else:
        print ("Use the correct syntax: python3 cc.py frontPicturePath backPicturePath generatedPDF_path optionalWatermark")