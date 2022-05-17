import time
start = time.time()

def end(Txt, C=False):
    end = time.time()
    if Txt:
        if C:
            return 'Current Time Taken: {}'.format(end-start)
        else:
            return 'Time Taken: {}'.format(end-start)
    else:
        return end-start