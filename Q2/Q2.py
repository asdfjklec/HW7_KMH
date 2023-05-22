import numpy as np

def main():
    Docs = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    Query = np.array([1,1,0,0,1,0])
    
    doc = []
    for a in Docs:
        temp = np.dot(a, Query) / (np.linalg.norm(a)*np.linalg.norm(Query))
        doc.append(temp)

    for i in range(1,4):
        print("doc" + str(i) + " = %0.2f" %doc[i-1])
        
if __name__ == '__main__':
    main()
