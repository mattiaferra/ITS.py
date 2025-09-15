

n="092b6377ed4b49fc16bbd5240f5c8" + \
        "124575b04b0053b037da6fbb461941" + \
        "919152a210e8ea43a82eaff13dd295" + \
        "f63e493df331403f14288767e6356b" + \
        "c2f52138ac9015b7c16f27679da0de" + \
        "546ca61056806f595c7d4772b603a9" + \
        "a49c8c4f6d575eb188a4609817135c" + \
        "5d7d2b8fdacf0cf14983c1304ca63a" + \
        "888f262d694bee21935c448aa0d7f4" + \
        "a217f8f70b0fe2c5db8de1f1e49076" + \
        "00cd3422b02b7f2dddf80fa15b9a8f" + \
        "c0aef58d0fc936b74120249a47b399" + \
        "9d72f21998cf595d331c6ddf7e974d" + \
        "aa7d0a55155689eee0a7f7a45b6265" + \
        "be97bd5c6569d8657b2709eac6bf32" + \
        "c7bfe637d632ba14165689049446ff" + \
        "632cc577e41ecc49a4f41d2840b3c5" + \
        "23bf"

decimale= int(n,16)
M= "Ciao come va ?.." 
Mi=int(M.encode("utf-8").hex(), 16)
print(Mi)
e=3


d= "1873b3ea78c8c54ae74a386028f6ad" + \
   "b63e480c800df2b3f9bd49e1043598" + \
             "42e31b02d17c609c07c7fd8a4dc3a9" + \
             "0a618a5332e00a835c16915108e74b" + \
             "28dadec76d58f3f592869144f0250e" + \
             "121bad63c0128ee4bf8be873ab46f0" + \
             "c4c20d3ce3e51d96c61019592de4ba" + \
             "3f8742a477d77d8c40a032b77109c1" + \
             "6d3107918ca7b042f951ea9abcda26" + \
             "456a6ce6a91eed2e5901d165da2e6c" + \
             "b0456927d44c4eee328a1813d9da81" + \
             "5d1feae513021c1b98e0e79463cf61" + \
             "d8aaf330231c9ec54f68f065936368" + \
             "f1bd2b0b412e60527340745774a822" + \
             "8bd400a1803722a808e90ba3529643" + \
             "1018f8246311e0d74671517f0e8a65" + \
             "be9df4e7f0b83be7ab9079ce18084e" + \
             "77"


d= int(d,16)
decifrato= pow(n,d,decimale)
print(decifrato)