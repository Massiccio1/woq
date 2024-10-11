import gen

#chamged in run
dim = 10
k = 5

def find_optimal_cost(fullcost,k):
    #   [ fixed_woq, [list of calculated wages]  ]
    total_cost=[]
    for i in range(len(fullcost)):
        wage= sorted(fullcost[i][1])
        tmp_cost=0
        for tmp_wage in wage[:k]:
            tmp_cost+=tmp_wage
        total_cost.append(tmp_cost)
        # print(text)
    m = min(total_cost)

    return m

def calc_full_cost(w:list,q:list,woq:list):
    fullcost = []
    for i in range(len(woq)-k+1):
        wage_fixed_woq=[]
        for j in range(i,len(woq)):
            wage = woq[i]*q[j]
            wage_fixed_woq.append(wage)
        fullcost.append([woq[i],wage_fixed_woq])
    return fullcost

def calc_woq(w,q):
    woq=[]
    for i in range(len(w)):
        val = (w[i])/(q[i])
        woq.append(val)
    return woq

def run(dim_par = 5, k_par= 2):

    dim = int(dim_par)
    k=int(k_par)
    w,q , _, _= gen.gen_lists(dim)
    woq=calc_woq(w,q)
    woq, q, w = (list(t) for t in zip(*sorted(zip(woq,q,w), reverse=True)))
    fullcost = calc_full_cost(w,q,woq)
    opt = find_optimal_cost(fullcost,k)
    return opt

if __name__ == "__main__":
    opt = run()
    print("minumum cost: ", opt)
    # fullcost = calc_full_cost(fullmap)