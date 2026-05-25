import numpy as np
import os 
from dotenv import load_dotenv 
load_dotenv()
choch = os.getenv("CHOCH")

n1 = 14
n2 = 5
n3 = np.add(n1,n2)


def main():
    print("Hello from pp!")
    print("Resultado = ",n3)
    print("Rorrogay owo :D")
    print("Chocho: ",choch)



if __name__ == "__main__":
    main()
