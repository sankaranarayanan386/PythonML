from numpy import *
import random
##################################################################################
def  h_theta_avg_error(theta_0,theta_1,data_set,m) :
    total_error=0
    for i in range(len(data_set)):
        x=float(data_set[i][0])
        y=float(data_set[i][1])
        h_theta_x=theta_0+(theta_1*x)
        error=(h_theta_x-y)
        total_error+=error
        #print("x={0}  predicted={1}   actual={2}   error={3}",x,h_theta_x,y,error)
    #print("average_error=",(total_error/(2*len(data_set))))
    return(abs(total_error/2))
################################################################################
if __name__=="__main__":
    data_set=genfromtxt("data.csv",delimiter=',')
    theta_0=random.uniform(0,5)
    theta_1=random.uniform(0,data_set[0][0])
    m=len(data_set)
    
    total_error=h_theta_avg_error(theta_0,theta_1,data_set,m)
    #print(total_error)
    #alpha=random.uniform(0,0.3)
   # print(alpha)
    #print(gradient_descent(total_error,alpha,data_set,theta_0,theta_1))
       
#########################################################################
##data_set=genfromtxt("data.csv",delimiter=',')
#theta_0=random.uniform(0,5)
#theta_1=random.uniform(0,data_set[0][0])
    alpha=0.0001
#m=len(data_set)
    previous_cost=total_error
    for i in range(1000):
        for j in range(m):
            theta_0_temp=theta_0-((alpha*total_error)*(1/m))
            theta_1_temp=theta_1-(((alpha*total_error)*(1/m))*data_set[j][0])
            theta_0=theta_0_temp
            theta1=theta_1_temp
            new_cost=h_theta_avg_error(theta_0,theta_1,data_set,m)
            print("new=",new_cost)
            print("old=",previous_cost)
            if [abs(abs(new_cost)-abs(previous_cost))<(120)]:
                print("#######################################################################################################################")
                print(theta_0,theta_1,new_cost)
                
                break
            previous_cost=new_cost
    