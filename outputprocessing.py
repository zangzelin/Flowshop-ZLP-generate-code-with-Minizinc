import os
import numpy as np
import main

def ProcessingOutputFile(text,ap):
    
    ap = open(ap,'a')
    f=open("answeritem/data"+str(text)+".txt")
    
    text = f.read()
    finalpart = text.split("----------\n")
    finalpart = finalpart[-2]

    lines = finalpart.split("\n")
    order = lines[0].split('[')[1].split(']')[0]
    obj = int(lines[0].split('[')[1].split(']')[1])
    order = [int(orde) for orde in order.split(', ')]

    n = len(order)

    protime = []

    i = 0
    for line in lines[2:-1]:
        i+=1
        items = line.split(':')
        tl = []
        for item in items:
            a,b,c = item.split('-')
            tl.append([int(a),int(b)])
            
        protime.append(tl)

    problem = {}
    problem['time'] = protime
    problem['order'] = order
    problem['n'] = n
    problem['m'] = i
    problem['obj'] = obj

    ap.write(str(problem))
    ap.write("\n")

    f.close()
    ap.close()

    return problem

def main2():
    question_path = open('dataset/dataset-question1.txt','w')
    problem =  ProcessingOutputFile(0,question_path)
    print(problem)

if __name__ == '__main__':
    main2()
