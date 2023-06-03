


def arithmetic_arranger(Elements,anwswer=False):

    numbers1 = []
    numbers2 = []
    numbers3 = []
    numbers4 = []
    numbers5 = []
    
    count = 0

    # if(type(Elements)) != List :
    #     print("Not Enought Items")
    # else: 
    if(len(Elements) > 5):
        print("Error: Too many problems.")
        return "Error: Too many problems."
    for operation in Elements:
        count +=1        
        numbers = operation.split()
        # print(numbers)
        if(len(max(numbers, key=len))>4):
            print("Error: Numbers cannot be more than four digits.")
            return "Error: Numbers cannot be more than four digits."
            
        if(numbers[1] !="-" and numbers[1]!= "+"):
             print("Error: Operator must be '+' or '-'.")   
             return "Error: Operator must be '+' or '-'."
             
        if(not str(numbers[0]).isnumeric() or not str(numbers[2]).isnumeric()):         
            print("Error: Numbers must only contain digits.")
            return "Error: Numbers must only contain digits."
            
        else:
            padding =  len(max(numbers, key=len)) + 2
                        
            if(numbers[1] == "+"):
                result = int(numbers[0]) + int(numbers[2])
                numbers.append(str(result))
            if(numbers[1] == "-"):
                result = int(numbers[0]) - int(numbers[2])
                numbers.append(str(result))
         
            print(padding)
            numbers.append(padding)
            # print(numbers)               
            match count:
                case 1:                    
                    numbers1 = numbers  
                case 2:                    
                    numbers2 = numbers  
                case 3:                    
                    numbers3 = numbers  
                case 4:                    
                    numbers4 = numbers  
                case 5:                    
                    numbers5 = numbers  

    # print("1")               
    # print(numbers1)  
    # print("2")               
    # print(numbers2)        
    # print("3")                 
    # print(numbers3)    
    # print("4")                
    # print(numbers4)        
      
    match count:
        case 1: 
            if(anwswer==True):
                return(str(numbers1[0]).rjust(numbers1[4], ' ') + "\n" + str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "\n" + "".rjust(numbers1[4],"-") + "\n" + str(numbers1[3]).rjust(numbers1[4], ' ') )
            
            return(str(numbers1[0]).rjust(numbers1[4], ' ') + "\n" + str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "\n" + "".rjust(numbers1[4],"-") )
                
    
        case 2:           
            if(anwswer==True):
                return(str(numbers1[0]).rjust(numbers1[4], ' ') + "    " + str(numbers2[0]).rjust(numbers2[4], ' ') + "\n" + 
                    str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "    " + str(numbers2[1])+ " " +  str(numbers2[2]).rjust(numbers2[4]-2, ' ') + "\n" +
                "".rjust(numbers1[4],"-") + "    " +  "".rjust(numbers2[4],"-")  + "\n" + str(numbers1[3]).rjust(numbers1[4], ' ') + "    " + str(numbers2[3]).rjust(numbers2[4], ' ') )
            return(str(numbers1[0]).rjust(numbers1[4], ' ') + "    " + str(numbers2[0]).rjust(numbers2[4], ' ') + "\n" + 
                    str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "    " + str(numbers2[1])+ " " +  str(numbers2[2]).rjust(numbers2[4]-2, ' ') + "\n" +
                "".rjust(numbers1[4],"-") + "    " +  "".rjust(numbers2[4],"-"))
        case 3: 
            if(anwswer==True):
                return(str(numbers1[0]).rjust(numbers1[4], ' ') + "    " + str(numbers2[0]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[0]).rjust(numbers3[4], ' ') + "    " + str(numbers4[0]).rjust(numbers4[4], ' ') + "\n" + 
                    str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "    " + str(numbers2[1])+ " " +  str(numbers2[2]).rjust(numbers2[4]-2, ' ') + "    " +  str(numbers3[1])+ " " +  str(numbers3[2]).rjust(numbers3[4]-2, ' ') + "    " + str(numbers4[1])+ " " +  str(numbers4[2]).rjust(numbers4[4]-2, ' ') + "\n" +
                "".rjust(numbers1[4],"-") + "    " +  "".rjust(numbers2[4],"-") + "    " + "".rjust(numbers3[4],"-") + "    " + "".rjust(numbers4[4],"-") + "    " + "\n" + str(numbers1[3]).rjust(numbers1[4], ' ') + "    " + str(numbers2[3]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[3]).rjust(numbers3[4], ' ') + "    " + str(numbers4[3]).rjust(numbers4[4], ' '))
            return(str(numbers1[0]).rjust(numbers1[4], ' ') + "    " + str(numbers2[0]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[0]).rjust(numbers3[4], ' ')  + "\n" + 
                    str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "    " + str(numbers2[1])+ " " +  str(numbers2[2]).rjust(numbers2[4]-2, ' ') + "    " +  str(numbers3[1])+ " " +  str(numbers3[2]).rjust(numbers3[4]-2, ' ') + "\n" +
                "".rjust(numbers1[4],"-") + "    " +  "".rjust(numbers2[4],"-") + "    " + "".rjust(numbers3[4],"-"))
 
        case 4: 
            if(anwswer==True):
                return(str(numbers1[0]).rjust(numbers1[4], ' ') + "    " + str(numbers2[0]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[0]).rjust(numbers3[4], ' ') + "    " + str(numbers4[0]).rjust(numbers4[4], ' ') + "\n" + 
                    str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "    " + str(numbers2[1])+ " " +  str(numbers2[2]).rjust(numbers2[4]-2, ' ') + "    " +  str(numbers3[1])+ " " +  str(numbers3[2]).rjust(numbers3[4]-2, ' ') + "    " + str(numbers4[1])+ " " +  str(numbers4[2]).rjust(numbers4[4]-2, ' ') + "\n" +
                "".rjust(numbers1[4],"-") + "    " +  "".rjust(numbers2[4],"-") + "    " + "".rjust(numbers3[4],"-") + "    " + "".rjust(numbers4[4],"-") + "    " + "\n" + str(numbers1[3]).rjust(numbers1[4], ' ') + "    " + str(numbers2[3]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[3]).rjust(numbers3[4], ' ') + "    " + str(numbers4[3]).rjust(numbers4[4], ' '))
            return(str(numbers1[0]).rjust(numbers1[4], ' ') + "    " + str(numbers2[0]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[0]).rjust(numbers3[4], ' ') + "    " + str(numbers4[0]).rjust(numbers4[4], ' ') + "\n" + 
                    str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "    " + str(numbers2[1])+ " " +  str(numbers2[2]).rjust(numbers2[4]-2, ' ') + "    " +  str(numbers3[1])+ " " +  str(numbers3[2]).rjust(numbers3[4]-2, ' ') + "    " + str(numbers4[1])+ " " +  str(numbers4[2]).rjust(numbers4[4]-2, ' ') + "\n" +
                "".rjust(numbers1[4],"-") + "    " +  "".rjust(numbers2[4],"-") + "    " + "".rjust(numbers3[4],"-") + "    " + "".rjust(numbers4[4],"-"))
        case 5: 
            if(anwswer==True):
                return(str(numbers1[0]).rjust(numbers1[4], ' ') + "    " + str(numbers2[0]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[0]).rjust(numbers3[4], ' ') + "    " + str(numbers4[0]).rjust(numbers4[4], ' ') + "    " + str(numbers5[0]).rjust(numbers5[4], ' ') + "\n" + 
                    str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "    " + str(numbers2[1])+ " " +  str(numbers2[2]).rjust(numbers2[4]-2, ' ') + "    " +  str(numbers3[1])+ " " +  str(numbers3[2]).rjust(numbers3[4]-2, ' ') + "    " + str(numbers4[1])+ " " +  str(numbers4[2]).rjust(numbers4[4]-2, ' ') + "    " + str(numbers5[1])+ " " +  str(numbers5[2]).rjust(numbers5[4]-2, ' ')  + "\n" +
                "".rjust(numbers1[4],"-") + "    " +  "".rjust(numbers2[4],"-") + "    " + "".rjust(numbers3[4],"-") + "    " + "".rjust(numbers4[4],"-") + "    " + "".rjust(numbers5[4],"-")  + "\n" + str(numbers1[3]).rjust(numbers1[4], ' ') + "    " + str(numbers2[3]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[3]).rjust(numbers3[4], ' ') + "    " + str(numbers4[3]).rjust(numbers4[4], ' ')  + "    " + str(numbers5[3]).rjust(numbers5[4], ' '))
            return(str(numbers1[0]).rjust(numbers1[4], ' ') + "    " + str(numbers2[0]).rjust(numbers2[4], ' ') + "    " +  str(numbers3[0]).rjust(numbers3[4], ' ') + "    " + str(numbers4[0]).rjust(numbers4[4], ' ') + "    " + str(numbers5[0]).rjust(numbers5[4], ' ') + "\n" + 
                    str(numbers1[1])+ " " +  str(numbers1[2]).rjust(numbers1[4]-2, ' ') + "    " + str(numbers2[1])+ " " +  str(numbers2[2]).rjust(numbers2[4]-2, ' ') + "    " +  str(numbers3[1])+ " " +  str(numbers3[2]).rjust(numbers3[4]-2, ' ') + "    " + str(numbers4[1])+ " " +  str(numbers4[2]).rjust(numbers4[4]-2, ' ')  + "    " + str(numbers5[1])+ " " +  str(numbers5[2]).rjust(numbers5[4]-2, ' ')+ "\n" +
                "".rjust(numbers1[4],"-") + "    " +  "".rjust(numbers2[4],"-") + "    " + "".rjust(numbers3[4],"-") + "    " + "".rjust(numbers4[4],"-") + "    " + "".rjust(numbers5[4],"-"))




