import svgwrite
import tempfile
import time
from constants import *
import webbrowser as wb
from os import remove as rm


def generatePreview():
    global tempFile
    delTempFile()
    tempFile = tempfile.NamedTemporaryFile(mode='w+b', suffix=".svg", delete=False)
    dw = svgwrite.Drawing('{0}'.format(str(tempFile.name)), size=(str(A4_WIDTH + 10),str(A4_HEIGHT + 10)))
    dw.add(dw.rect(
        insert=(5, 5), 
        size=(A4_WIDTH, A4_HEIGHT), 
        stroke=svgwrite.rgb(0,0,0), 
        stroke_width=4,
        fill='white'))

    dw.add(dw.rect(
        insert=(FRONT_X, FRONT_Y),
        size=(CC_WIDTH, CC_HEIGHT),
        stroke=svgwrite.rgb(0,0,0), 
        stroke_width=1,
        fill='red'
    ))

    dw.add(dw.text(
    'Costas',
    insert=(FRONT_X + (CC_WIDTH/2), FRONT_Y + (CC_HEIGHT/2)),
    stroke='none',
    fill=svgwrite.rgb(15, 15, 15, '%'),
    font_size='15px',
    font_weight="bold"
    ))

    dw.add(dw.rect(
        insert=(BACK_X, BACK_Y),
        size=(CC_WIDTH, CC_HEIGHT),
        stroke=svgwrite.rgb(0,0,0), 
        stroke_width=1,
        fill='red'
    ))

    dw.add(dw.text(
    'Frente',
    insert=(BACK_X + (CC_WIDTH/2), BACK_Y + (CC_HEIGHT/2)),
    stroke='none',
    fill=svgwrite.rgb(15, 15, 15, '%'),
    font_size='15px',
    font_weight="bold"
    ))

    dw.add(dw.text(
    'Não quero não é adasadad',
    insert=(10*CM, 22.5*CM),
    stroke='none',
    fill=svgwrite.rgb(139, 136, 136),
    transform=str('rotate(310,%s, %s)' % (3.5*CM, 22.5*CM)),
    font_size='30px',
    font_weight="bold"
    ))
    
    
    
    dw.save()
    wb.open('{0}'.format(str(tempFile.name)), new=1, autoraise=True)
    time.sleep(1)

def delTempFile():
    if tempFile:
        rm(tempFile.name)