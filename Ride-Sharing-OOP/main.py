from ride_sharing import Ride_Sharing
from users import Rider,Driver

def main():
    niye_jao = Ride_Sharing("Niye Jao")
    sakib = Rider("Sakib khan","sakib@email.com",1234,'tongi',12000)
    niye_jao.add_rider(sakib)
    sk = Driver("sk","sk@gmail.com",523,"Gulashan-1")
    niye_jao.add_driver(sk)
    print(niye_jao)
    sakib.request_ride(niye_jao,"Uttara")



main()