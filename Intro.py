import sys
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip

from statics.helpers import DrawHelpers

FRAME_COLOR_1 = '#EE1D52'
FRAME_COLOR_2 = '#69C9D0'

FONT_COLOR = '#ffffff'
BACKGROUND = '#010101'

FONT_PATH = './statics/fonts/montserrat.ttf'
IMAGE_SIZE = (WIDTH, HEIGHT) = (1080, 1920)


def get_powered_by():
    return Image.open('./statics/logos/powered.png').convert('RGBA')
    
def get_logo_tech(tech):
    return Image.open(f'./statics/logos/{tech}.png').convert('RGBA')

largura = WIDTH
altura = HEIGHT
fps = 30
tempo_total = 6

quadros = []

# Declarando a fonte
font = ImageFont.truetype(FONT_PATH, 80)

texto = sys.argv[1]
tech_arg = sys.argv[2]

texto = texto.upper()
lether_list = []
for l in texto:
    lether_list.append(l)
lether_list = lether_list[::-1]
lether_time = ((fps*tempo_total) // (len(texto)+6))
animation_text = []
count = 0

logo = get_powered_by()
width_logo, height_logo = logo.size

logo_tech = get_logo_tech(tech_arg)
width_logo_tech, height_logo_tech = logo_tech.size

for tempo in range(tempo_total * fps):
    if count>lether_time:
        count=0
        try:
            animation_text.append(lether_list.pop()) 
        except:
            pass
        print(animation_text)

    image = Image.new('RGBA', IMAGE_SIZE, BACKGROUND)

    draw = ImageDraw.Draw(image)

    frame_1_start = ((HEIGHT//2)-100)-100
    frame_1_end = ((HEIGHT//2)-100)

    draw.rectangle((frame_1_start-550,frame_1_start,frame_1_end-550,frame_1_end), FRAME_COLOR_1)    
    draw.rectangle((frame_1_start-500,frame_1_start+50,frame_1_end-450,frame_1_end+100), BACKGROUND)

    draw.rectangle((frame_1_start,frame_1_start,frame_1_end,frame_1_end), FRAME_COLOR_2)
    draw.rectangle((frame_1_start-50,frame_1_start+50,frame_1_end-50,frame_1_end+50), BACKGROUND)

    draw.rectangle((frame_1_start, frame_1_start+350, frame_1_end, frame_1_end+350), FRAME_COLOR_1)    
    draw.rectangle((frame_1_start-50,frame_1_start+300,frame_1_end-50,frame_1_end+300), BACKGROUND)

    draw.rectangle((frame_1_start-550,frame_1_start+350,frame_1_end-550,frame_1_end+350), FRAME_COLOR_2)
    draw.rectangle((frame_1_start-500,frame_1_start+300,frame_1_end-500,frame_1_end+300), BACKGROUND)

    # total arguments
    if (animation_text):
        text_width, text_height = DrawHelpers.get_text_dimensions(''.join(animation_text), font)
        POSITION = (((WIDTH//2)-(text_width//2)), ((HEIGHT//2)-(text_height//2)))
        draw.text(
                POSITION, 
                ''.join(animation_text), 
                font=font, 
                fill=FONT_COLOR
        )
    # Adicione o quadro à lista
    count += 1
    image.save(f"./build/{''.join(animation_text)}_{count}.png")
    quadros.append(f"./build/{''.join(animation_text)}_{count}.png")

print(f'Total de quadros: {len(quadros)}')
print(f'Termpo por letra: {lether_time}')
print(f'texto: {lether_list}')
print(f'len_texto: {len(lether_list)}')

video = ImageSequenceClip(quadros, fps=fps)

video.write_videofile(f'intro{texto}.mp4', fps=fps)