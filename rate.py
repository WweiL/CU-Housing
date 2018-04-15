import numpy as np
#home_dict[[housename,housescore,gymscore,marketscore,libraryscore,north,out]]
#north==1,south==0,out==1,in==0
home_dict=[['house1',1.0,2.0,12.0,4.0,0.0,1.0],['house2',2.0,3.0,4.0,5.0,0.0,1.0],['house3',3.0,4.0,5.0,6.0,0.0,1.0]]
home_dict=np.array(home_dict)
def score(home_dict,year,location,gym,eat,car,study):
    #rscore=list[0]
    #rscore=srestaurantrate*srscore+orestaurantrate*orscore
    restaurantrate=0.3
    gymrate=0.1
    marketrate=0.3
    libraryrate=0.2
    nsrate=1.0
    """if ('year' == 'fresh'):
        srestaurantrate = 0.8
        orestaurantrate = 0.2
    else:
        srestaurantrate = 0.1
        orestaurantrate = 0.9"""

    ###For location,question2:
    # north==1,south==0
    """if (location == 1) and (house == 0):
        ###This means if the house is in the north, house is equal to zero
        nsrate = 0.66666666
    elif (location == 0) and (house == 1):
        ###This means if the house is in the south house is equal to one
        nsrate = 0.66666666"""


    ###For gym, question3:
    if (gym == 1.0):
        gymrate = 0.1
    elif (gym == 2.0):
        gymrate = 0.15
    elif (gym == 3.0):
        gymrate = 0.25
    else:
        gymrate = 0.3

    ###For question4:
    # cook==1
    if (eat == 1.0):
        restaurantrate = 0.25
        marketrate = 0.7

    ###For question5##  :
    # car==1

    if (car == 0.0):
        newhome_dict=[]
        for i in range(home_dict.shape[0]):
            if (home_dict[i][6].astype(float) == 0):  ##This means that the house is not on campus:
                newhome_dict.append(term)
        home_dict = np.array(newhome_dict)

    ###For question6
    #library=0
    if (study == 0.0):
        libraryrate = 0.3
    #rscore=srestaurantrate*srscore+orestaurantrate*orscore
    result=[]
    for i in range(home_dict.shape[0]):
        if (location == 1) and (home_dict[i][5].astype(float) == 0):
            ###This means if the house is in the north, house is equal to zero
            nsrate = 0.66666666
        elif (location == 0) and (home_dict[i][5].astype(float) == 1):
            ###This means if the house is in the south house is equal to one
            nsrate = 0.66666666
        restaurantscore=home_dict[i][1].astype(float)
        gymscore=home_dict[i][2].astype(float)
        marketscore=home_dict[i][3].astype(float)
        libraryscore=home_dict[i][4].astype(float)
        finalscore=(nsrate*(restaurantrate*restaurantscore+gymrate*gymscore+marketrate*marketscore+libraryrate*libraryscore))/(restaurantrate+gymrate+marketrate+libraryrate)
        result.append([home_dict[i][0],finalscore])
    result=np.array(result)
    result = result[result[:,-1].argsort()]
