from random import *
kommide_arv=randint(10 ,100)
print(f"laual on {kommide_arv} kommi")
võetud_kommide_arv=int(input("mittu kommi sa soovid laualt ära võtta? "))
if võetud_kommide_arv>kommide_arv:
    print("laual pole nii palju komme")
else:
    kommide_arv-=võetud_kommide_arv
    print(f"nüüd on laual {kommide_arv} kommi")