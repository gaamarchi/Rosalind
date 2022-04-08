def fibonnaci_numbers(months,offspring):
    parrent,child =1,1
    for itr in range(months-1):
        child, parrent = parrent, parrent+(child*offspring)
    return child   
    