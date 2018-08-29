import os
import time
import createdataset
import outputprocessing



def work():


    question_path = 'dataset/dataset-question1.txt'
    answer_path = 'dataset/dataset-answer1.txt'
    abovenumber = 1000    


    for i in range(abovenumber):

        createdataset.Create(5, 15, i, question_path)

        input1 = 'problemitem/data'+str(i)+'.dzn'
        output = 'answeritem/data'+str(i)+'.txt'
        os.system('timeout 300 minizinc flowshop.mzn ' + input1 + ' -a -o '+output) 

        outputprocessing.ProcessingOutputFile(i, answer_path)
        print(i,"/",abovenumber)

def main():
    work()

if __name__ == '__main__':
    main()