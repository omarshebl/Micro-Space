import variables
import random
import pygame

pygame.font.init()
clock = pygame.time.Clock()
FPS = variables.FPS

simplequestions = [["What interrupt do we use for outputting text ?", "21h"],
             ["What interrupt do we use for inputting text ?", "16h"],
             ["What value for AH in INT10 to change video mode ?", "0"],
             ["What value for AX to get mouse position in INT33 ?","3"]] #TODO add more questions

hardquestions = [["MOV BX,25h\nMOV AX,36h\nADD AX,BX\nAX=?","5Bh"]
                 ]

def makequestion(typeqeus):
    if typeqeus == 1:
        num = random.randint(0, len(simplequestions)-1)
        return simplequestions[num],num
    else:
        num = random.randint(0, len(hardquestions)-1)
        return hardquestions[num],num


def drawpwrp(WIN, multiplier, pwrup):
    if pwrup == "nuke":
        WIN.blit(variables.nuke128, (variables.Xq/2 - variables.nuke128.get_width() / 2, 50))
    if pwrup == "revive":
        WIN.blit(variables.revive128, (variables.Xq/2 - variables.revive128.get_width() / 2, 50))
    if pwrup == "armor":
        WIN.blit(variables.armor128, (variables.Xq/2 - variables.armor128.get_width() / 2, 50))
    if pwrup == "health":
        WIN.blit(variables.health128, (variables.Xq/2 - variables.health128.get_width() / 2, 50))
    if pwrup == "auto":
        WIN.blit(variables.auto128, (variables.Xq/2 - variables.auto128.get_width() / 2, 50))
    if pwrup == "smrtmissile":
        WIN.blit(variables.smrtmissile128, (variables.Xq/2 - variables.smrtmissile128.get_width() / 2, 50))
    if pwrup == "multiplier":
        multiplier_label = variables.mainfont.render(f"For Multiplier: {multiplier}x", 1, variables.RED)
        WIN.blit(variables.multiplier128, (variables.Xq/2 - variables.multiplier128.get_width() / 2, 70))
        WIN.blit(multiplier_label, (variables.Xq / 2 - multiplier_label.get_width() / 2, 20))

def drawquestion(WIN, multiplier, pwrup, ques, typeques):
    variables.blackbackground.set_alpha(255)
    WIN.blit(variables.blackbackground, (0, 0))
    if typeques == 1:
        question_label = variables.questionfont.render(ques, 1, variables.WHITE)
        WIN.blit(question_label, (variables.Xq / 2 - question_label.get_width() / 2, 300))
    else:
        lines = ques.split("\n")
        i = 0
        for line in lines:
            line_label = variables.questionfont.render(line, 1, variables.WHITE)
            WIN.blit(line_label, (100, 200 + i*30))
            i += 1

    drawpwrp(WIN, multiplier, pwrup)

def askquestion(WIN, typeques, multiplier, auto, pwrup=None):
    timer = pygame.time.get_ticks()
    usertext = ""
    question,num = makequestion(typeques)
    if auto:
        usertext = str(question[1])
    while True:
        clock.tick(FPS)
        seconds = (pygame.time.get_ticks() - timer) / 1000
        questiontime = variables.simpleqtime
        if typeques != 1:
            questiontime = variables.hardqtime
        if seconds > questiontime:
            return False
        drawquestion(WIN,multiplier, pwrup, str(question[0]), typeques)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if not len(usertext) <= 0:
                        usertext = usertext[:-1]
                elif event.key == pygame.K_RETURN:
                    if usertext.lower() == str(question[1]).lower():
                        return True
                    else:
                        return False
                else:
                    usertext += event.unicode
        answer_label = variables.questionfont.render(usertext, 1, variables.WHITE)
        WIN.blit(answer_label, (variables.Xq / 2 - answer_label.get_width() / 2, 400))
        pygame.display.update()


