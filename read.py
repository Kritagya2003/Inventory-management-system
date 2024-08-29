
def store():
    #Display all items
    with open("store.txt", "r") as outfile:
        print()
        header = ['S.N', 'Name', 'Brand', 'Price', 'Quantity', 'Processor', 'Graphic Card']
        border = '+-------------------'*len(header)

        output = outfile.readlines()


        print(border)
        for item in header:
            print(item.ljust(len(item)+15), end=" ")
        print()
        print(border)


        total_index = 0
        for index, item in enumerate(output):
            total_index +=1
            li = item.split(",")
            li.insert(0,index+1)
            # print(li)
            for info in li:
                print(str(info).ljust(20),end='')
            print()
        print(border)
        return total_index