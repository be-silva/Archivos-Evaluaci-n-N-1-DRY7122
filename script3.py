acl = int(input("Ingrese el número de ACL IPv4: "))

# Standard 1-99, 1300-1999
# Extended 100-199, 2000-2699
print("Su ACL es:", acl)

if 1 <= acl <=99 or 1300<= acl <=1999:
    print("Su ACL es una ACL Estándar")
elif 100 <= acl <=199 or 2000<= acl <=2699:
    print ("Su ACL es una ACL Extendida")
else:
    print ("Su ACL no es Estandar ni Extendida")