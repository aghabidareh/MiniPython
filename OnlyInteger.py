def onlyInteger(List):
    List = [x for x in List if isinstance(x , int) and x >= 0]
    return List

List = ['aghabidareh' , '465' , 456 , 798 , '17 years' , 65]
print(onlyInteger(List))