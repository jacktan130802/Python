import numpy as np

E=[60,90,35,85,70,50]
Mt=[70,50,55,75,60,40]
M=[90,85,70,85,70,75]
S=[80,75,60,95,55,65]

mean_E=np.mean(E)
std_E=np.std(E)
E_t_score=50+10*(E[0]-mean_E)/std_E
print("His English T-Score is: ",int(E_t_score))

mean_Mt=np.mean(Mt)
std_Mt=np.std(Mt)
Mt_t_score=50+10*(Mt[0]-mean_Mt)/std_Mt
print("His Mother Tongue T-Score is: ",int(Mt_t_score))

mean_M=np.mean(M)
std_M=np.std(M)
M_t_score=50+10*(M[0]-mean_M)/std_M
print("His Math T-Score is: ",int(M_t_score))

mean_S=np.mean(S)
std_S=np.std(S)
S_t_score=50+10*(S[0]-mean_S)/std_S
print("His Science T-Score is: ",int(S_t_score))

score=int(E_t_score)+int(Mt_t_score)+int(M_t_score)+int(S_t_score)
print("His PSLE score is: ",score)
