import numpy as np
import pprint

filename = "data.csv"
pp = pprint.PrettyPrinter(indent=4)


def read_csv(filename):
    f = open(filename)
    lines = f.readlines()
    x = list() # Input list
    y = list() # Output list
    for line in lines:
        temp = line.strip().split(",")
        x.append([float(temp[0].replace('"', ''))])
        y.append([float(temp[1].replace('"', ''))])
    return np.array(x), np.array(y)


def regression():
    iterations = 10**6
    degree = 3
    lr = 1e-11
    train_test = 0.8
    weights = np.zeros((degree + 1, 1))
    inp, out = read_csv(filename)

    s = np.arange(inp.shape[0])
    np.random.shuffle(s)

    inp = inp[s]
    out = out[s]

    train_inp = inp[:int(train_test*inp.shape[0])]
    train_out = out[:int(train_test*out.shape[0])]

    # train_inp = np.array([[1], [2], [3]])
    # train_out = np.array([[1], [2], [3]])
    # print "train_inp"
    # pp.pprint(train_inp)
    # print "train_out"
    # pp.pprint(train_out)
    hx = np.array([[train_inp[i][0] ** j for j in range(degree + 1)] for i in
         range(train_inp.shape[0])])
    # print "Hx"
    # pp.pprint(hx)
    for iteration in range(iterations):
        y = np.dot(hx, weights)
        # print "y"
        # pp.pprint(y)
        err = train_out - y
        # print "err"
        # pp.pprint(err)
        # print "hxt"
        # pp.pprint(np.transpose(hx))
        # print "1/m", float(1) / train_inp.shape[0]
        # print err * (float(1) / train_inp.shape[0])
        # print "Temp"
        temp = np.dot(np.transpose(hx), err * (float(1) / train_inp.shape[0]))
        # pp.pprint(temp)
        weights = weights + lr * temp
        # print "###"
        # print weights
        s = np.sum(err)
        print "sum of errors", s
        if np.abs(s) < 1e-4:
            print "inja"
            break
        # raw_input()
    print weights
if __name__ == "__main__":
    regression()
