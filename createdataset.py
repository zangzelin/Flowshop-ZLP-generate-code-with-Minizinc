# import main
import numpy as np


def Create(m, n, id, question_path):
    
    question_path = open(question_path,'a')
    
    M = np.random.randint(10, 99, size=(m, n))
    Mlist = M.tolist()
    # print(Mlist)

    f = open('problemitem/data'+str(id)+'.dzn', 'w')
    f.write('m = '+str(m)+';\n')
    f.write('n = '+str(n)+';\n')

    f.write('M = [')
    for i in range(n):
        if i == 0:
            f.write('|'+'')
        else:
            f.write('\n |'+'')
        for j in range(m):
            if j == m-1:
                f.write(str(M[j, i])+'\t')
            else:
                f.write(str(M[j, i])+',\t')
    f.write('|];')
    # print('|];', end='', file=f)

    problem = {}
    problem['id'] = id
    problem['m'] = m
    problem['n'] = n
    problem['M'] = Mlist

    question_path.write(str(problem))
    question_path.write('\n')

    question_path.close()


def main():
    question_path = open('dataset/dataset-question1.txt', 'w')

    Create(5, 15, 100, question_path)


if __name__ == '__main__':
    main()
