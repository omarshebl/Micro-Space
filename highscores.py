


def readscores():
    scores = []
    with open("highscores.txt", 'r') as filehandle:
        for line in filehandle:
            currentline = line[:-1]
            name, score = currentline.split("\t")
            scores.append((name, int(score)))
    return scores




def writescore(score):
    scores = readscores()
    scores.append(score)
    scores.sort(key=lambda x: x[1])
    scores.reverse()
    if len(scores)>10:
        scores = scores[:-1]
    with open("highscores.txt", 'w') as filehandle:
        for name, score in scores:
            filehandle.write("%s\t%d\n" % (name, score))





