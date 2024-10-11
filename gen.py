import random


def gen_lists(dim =3 , avg = 10, ds=0.5):
    c = 65
    w = []
    q=[]
    woqa = []
    names = []
    for i in range(dim):
        woq  = random.randint(int(avg-ds*avg), int(avg+ds*avg))
        qual = random.randint(1,10)
        w.append(woq*qual)
        q.append(qual)
        woqa.append(woq)
        names.append(chr(c+i))

    return w,q, woqa, names


if __name__ == "__main__":
    print("in main gen")
    print(gen_lists())