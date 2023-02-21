from typing import Tuple,List


def find_maximum_and_minimum(file_name: str) -> List[Tuple[int, int]]:
    new=[]
    with open(file_name) as fi:
        for line in fi:
            if line=="\n": #
                continue
            line=line.split(",")
            for i in range(len(line)):
                line[i]=int(line[i]) #
            new.append((min(line),max(line)))



#find_maximum_and_minimum("file_task03.txt")
