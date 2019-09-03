
# coding: utf-8

# In[1]:


from numpy import *
import matplotlib


# In[2]:


def h_theta_avg_error(theta_0,theta_1,data_set,m) :
    total_error=0
    for i in range(len(data_set)):
        x=float(data_set[i][0])
        y=float(data_set[i][1])
        h_theta_x=theta_0+(theta_1*x)
        error=(h_theta_x-y)**2
        total_error+=error
        #print("x={0}  predicted={1}   actual={2}   error={3}",x,h_theta_x,y,error)
    #print("average_error=",(total_error/(2*len(data_set))))
    return((total_error/(2*m)))


# In[3]:


def gradient_descent(total_error,alpha,data_set,theta_0,theta_1,iterations):
    m=len(data_set)
    print("running gradient Descent....")
    #count=0
    #countif=0
    i=0
    for i in range(0,iterations):
        theta_0,theta_1,new_error=descent_step(theta_0,theta_1,data_set,alpha,total_error)
       # count+=1
       # print(theta_0,theta_1,new_error)
        #print(count,countif)
        if abs(new_error-total_error)<=10 :
            total_error=new_error
           # countif+=1
            break
    total_error=new_error
    plot(theta_0,theta_1,data_set)
    return (theta_0,theta_1,total_error,alpha)     
        


# In[4]:


def descent_step(theta_0,theta_1,data_set,alpha,total_error):
    theta_0_temp=0
    theta_1_temp=0
    m=len(data_set)
    for i in range(m):
        theta_0_temp+=-(2/m)*(data_set[i][1] - ((theta_1 * data_set[i][0]) + theta_0))
        theta_1_temp+=-(2/m)*data_set[i][0]*(data_set[i][1]-((theta_1*data_set[i][0]+theta_0)))
    theta_0_new = theta_0 - (alpha * theta_0_temp)
    theta_1_new = theta_1 - (alpha * theta_1_temp)
    new_error=h_theta_avg_error(theta_0_new,theta_1_new,data_set,m)
    return(theta_0_new,theta_1_new,new_error)




import matplotlib.pyplot as plt
def plot(theta_0,theta_1,data_set):
    get_ipython().magic('matplotlib inline')
    x=[0]*len(data_set)
    y=[0]*len(data_set)
    y_predict=[]
    for i in range(len(data_set)):
        x[i]=data_set[i][0]
        y[i]=data_set[i][1]
        y_predict.append((theta_0 + theta_1*x[i]))
    plt.plot(x,y,'o')
    plt.plot(x,y_predict,'r-')
    #plt.show()
    

# In[7]:


if __name__=="__main__":
    data_set=genfromtxt("data.csv",delimiter=',')
    theta_0=0
    theta_1=0
    m=len(data_set)
    total_error=h_theta_avg_error(theta_0,theta_1,data_set,m)
    print(total_error)
    alpha=0.0001
    #print(alpha)n
    iterations=100000
    print(gradient_descent(total_error,alpha,data_set,theta_0,theta_1,iterations))
    plt.show()
    print ("Done!")
    #anim.save(r"C:\Users\668376\Desktop\LR\linear_regression.mp4",writer=animation.FFMpegWriter())
    


# In[5]:



