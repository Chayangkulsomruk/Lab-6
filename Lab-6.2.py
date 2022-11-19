class Creategraph:
    def __init__(Self):
        Self.Time = [[" "," "],[" "," "]]
    def Createedge(Self,Nodename):
        temp = Self.Time[0]
        if Self.Time[0][-1] != " ":
            Self.Time[0].append(" ")
            Selfime = False
        else:
            Selfime = True
        check = 0
        if Self.Time[0][0] == " ":
            Self.Time[0][0] = "-"
        for i in range (len(Self.Time[0])):
            if i == len(Self.Time[0])- 1 and not Selfime:
                Self.Time.append([])
            while len(Self.Time[i]) < len(Self.Time[i-1]):
                Self.Time[i].append("0")
                if Self.Time[i][0] == "0":
                    Self.Time[i][0] = " "
        for i in range (len(Self.Time)):
            if Self.Time[0][i] == " " and check == 0:
                Self.Time[0][i] = Nodename
                check = 1
        for j in range (len(Self.Time[0])):
            if Self.Time[j][0] == " " and check == 1:
                Self.Time[j][0] = Nodename
                Self.Time[j][1] = "0"
                check = 0
    def AdjacencyMatriTime(Self):
        print(len(Self.Time) * "****")
        for i in range(len(Self.Time)):
            print(Self.Time[i])
    def connect(Self,X,Y):
        if X in Self.Time[0] and Y in Self.Time[0] :
            XInTime,YinTime = 0,0
            for i in range(len(Self.Time)):
                if X == Self.Time[0][i]:
                    XInTime = i
                elif Y == Self.Time[0][i]:
                    YinTime = i
            Self.Time[XInTime][YinTime] = "1"
            Self.Time[YinTime][XInTime] = "1"
        else:
            print ("Not")
    def AdjacencyList(Self):
        tempList = [ ]
        for i in range(1,len(Self.Time)):
            tempList.append(str(Self.Time[i][0]) + ":")
            for j in range(1,len(Self.Time)):
                if Self.Time[i][j] == "1":
                    tempList.append(Self.Time[0][j])
            print(tempList)
            tempList=[]
    def Edge_List(Self):
        tempList = [ ]
        List = [ ]
        output = [[ ],[ ]]
        for i in range(1,len(Self.Time)):
            tempList.append(str(Self.Time[i][0]) + ":")
            List.append(Self.Time[i][0])
            for j in range(1,len(Self.Time)):
                if Self.Time[i][j] == "1":
                    tempList.append(Self.Time[0][j])
                    memCheck = len(List)
                    List[memCheck-1] += Self.Time[0][j]
                    if j != (len(Self.Time) - 1):
                        List.append(Self.Time[i][0])
                elif (j == (len(Self.Time) - 1) and Self.Time[i][j] == "0"):
                    List.pop()
            tempList=[ ]
        Count = 0
        for i in range(len(List)):
            Get = List.pop(0)
            if Get[::-1] not in output[1]:
                output[0].append(str(Count) + ":")
                output[1].append(Get)
                Count += 1
        for i in range (len(output[0])):
            print(str(output[0][i]) + " " + str(output[1][i]))
Call = Creategraph()
Call.Createedge("A")
Call.Createedge("B")
Call.Createedge("C")
Call.Createedge("D")
Call.Createedge("E")
Call.Createedge("F")
Call.connect("A","B")
Call.connect("A","C")
Call.connect("A","F")
Call.connect("C","D")
Call.connect("D","E")
Call.connect("E","F")
Call.AdjacencyMatriTime()
print("****************************")
Call.AdjacencyList()
print("****************************")
Call.Edge_List()
