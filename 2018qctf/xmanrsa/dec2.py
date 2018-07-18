import base64
import libnum
import binascii

def num_to_bytes(n):
	b = hex(n)[2:-1]
	b = '0' + b if len(b)%2 == 1 else b
	return b.decode('hex')

def bytes_to_num(b):
	b = b.encode('hex')
	return int(b,16)

n2_base64 = "PVNHb2BfGAnmxLrbKhgsYXRwWIL9eOj6K0s3I0slKHCTXTAUtZh3T0r+RoSlhpO3+77AY8P7WETYz2Jzuv5FV/mMODoFrM5fMyQsNt90VynR6J3Jv+fnPJPsm2hJ1Fqt7EKaVRwCbt6a4BdcRoHJsYN/+eh7k/X+FL5XM7viyvQxyFawQrhSV79FIoX6xfjtGW+uAeVF7DScRcl49dlwODhFD7SeLqzoYDJPIQS+VSb3YtvrDgdV+EhuS1bfWvkkXRijlJEpLrgWYmMdfsYX8u/+Ylf5xcBGn3hv1YhQrBCg77AHuUF2w/gJ/ADHFiMcH3ux3nqOsuwnbGSr7jA6Cw=="
n3_base64 = "TmNVbWUhCXR1od3gBpM+HGMKK/4ErfIKITxomQ/QmNCZlzmmsNyPXQBiMEeUB8udO7lWjQTYGjD6k21xjThHTNDG4z6C2cNNPz73VIaNTGz0hrh6CmqDowFbyrk+rv53QSkVKPa8EZnFKwGz9B3zXimm1D+01cov7V/ZDfrHrEjsDkgK4ZlrQxPpZAPl+yqGlRK8soBKhY/PF3/GjbquRYeYKbagpUmWOhLnF4/+DP33ve/EpaSAPirZXzf8hyatL4/5tAZ0uNq9W6T4GoMG+N7aS2GeyUA2sLJMHymW4cFK5l5kUvjslRdXOHTmz5eHxqIV6TmSBQRgovUijlNamQ=="
n2 = bytes_to_num(base64.b64decode(n2_base64))
print n2
n3 = bytes_to_num(base64.b64decode(n3_base64))

print n3


c1_1 = "2639c28e3609a4a8c953cca9c326e8e062756305ae8aee6efcd346458aade3ee8c2106ab9dfe5f470804f366af738aa493fd2dc26cb249a922e121287f3eddec0ed8dea89747dc57aed7cd2089d75c23a69bf601f490a64f73f6a583081ae3a7ed52238c13a95d3322065adba9053ee5b12f1de1873dbad9fbf4a50a2f58088df0fddfe2ed8ca1118c81268c8c0fd5572494276f4e48b5eb424f116e6f5e9d66da1b6b3a8f102539b690c1636e82906a46f3c5434d5b04ed7938861f8d453908970eccef07bf13f723d6fdd26a61be8b9462d0ddfbedc91886df194ea022e56c1780aa6c76b9f1c7d5ea743dc75cec3c805324e90ea577fa396a1effdafa3090"
c1_2 = "42ff1157363d9cd10da64eb4382b6457ebb740dbef40ade9b24a174d0145adaa0115d86aa2fc2a41257f2b62486eaebb655925dac78dd8d13ab405aef5b8b8f9830094c712193500db49fb801e1368c73f88f6d8533c99c8e7259f8b9d1c926c47215ed327114f235ba8c873af7a0052aa2d32c52880db55c5615e5a1793b690c37efdd5e503f717bb8de716303e4d6c4116f62d81be852c5d36ef282a958d8c82cf3b458dcc8191dcc7b490f227d1562b1d57fbcf7bf4b78a5d90cd385fd79c8ca4688e7d62b3204aeaf9692ba4d4e44875eaa63642775846434f9ce51d138ca702d907849823b1e86896e4ea6223f93fae68b026cfe5fa5a665569a9e3948a"
#n1_1 = 0x11574caaea9fd80017ee2986de85b4939d2e43bd5edf5f84e280198004628303fc0c46030926d701194fd8b6b61fdad9fb996291742dcc181d7a21af22f9834caf7650637e458c616ec725a1396ea1920e78ea1ed70d9a35a2390744943a134c8a8101383386e94db4ff4e809d226cffc84bfa2847a3f4fe08ee9df4bf7a40ebf16a347fe90f09016b8b9d2dfb281b536da1fc4442c7b47f84204b3eed6186f4deab1f71ead8edd8c42fe3d93972c220d8c4eb9aab52600ed168ce51064c49b152e34c6fb83de63a635d421c9664fc78f7388de3d1dde7cd3180951c876f20dcede08280ec6ac284b120615e9e141dac68399035bb71eac8cd2bb866b3a6e007
#n1_2 = 0x0230d7a40a416d8c056c314b7d641bffb1dd007917ba0b215f58f6b68f8285067136aa0f0ce37db354cf61d22af84c8be4160963fcbfb9814f31875b458bfea9cb8aa064e5692894f2cde421b16ee2fba30d0b5d5acd8270af65c5bfdd656733b7170b48583a909560c5811cae775499b813efeb9bbb6a8e9da35bd54c0c6d047d6c28a6442cf69522b02c1609774fd4c19e1841989526f70896227138d0fc8bf3ad4ff92466aafc79dbc2b0b68cde3a810d805fba9db05267b33a39f26ccc06c34de1a6a90a5521f01a1e8e0e1387f6ed51b3970409b7562896dfdbf487337d787e6629d474a73e86dbb934446628dad06a8bc6bded821b9a2361f2f1055d12
n1_1 = bytes_to_num(c1_1.decode('hex'))
n1_2 = bytes_to_num(c1_2.decode('hex'))
e1 = 0x1001
e2 = 0x101
print libnum.xgcd(e1,e2)
xgcd = libnum.xgcd(e1,e2)
n1_1_inv = libnum.invmod(n1_1,n3)
assert (n1_1_inv*n1_1)%n3==1
m = (pow(n1_1_inv,xgcd[0]*-1,n3)*pow(n1_2,xgcd[1],n3))%n3
print m
print libnum.gcd(e1,e2)
assert pow(m,e1,n3)==n1_1
assert pow(m,e2,n3)==n1_2
#print hex(pow(m,e2,n3))
n1 = m
print n1
#n1 = 820928650845870620723398641418430560681156001138735096925030451902417919194443533997091546977591994803076546864089678354698681762386374331300311255855681398660128703679421620966541327377041709407909422433258969486458918135644782166730266421648609176380494526721089557340533459290986717438829332517062112510441791255031169683629746300741131885337863789133958194148147076564652001394063636006538871538841709581230856211101448471200607015180491156127670595948207742541369333765734985482522833859182877386338753929062754028024947469226250613374092460434598257428472528861445143456766204473851110780586998315353287
p1 = libnum.gcd(n1,n2)
p2 = n1/p1
p3 = n2/p1
e = 0x1001
phi_1 = (p1-1)*(p2-1)
phi_2 = (p1-1)*(p3-1)
c1 = "1240198b148089290e375b999569f0d53c32d356b2e95f5acee070f016b3bef243d0b5e46d9ad7aa7dfe2f21bda920d0ac7ce7b1e48f22b2de410c6f391ce7c4347c65ffc9704ecb3068005e9f35cbbb7b27e0f7a18f4f42ae572d77aaa3ee189418d6a07bab7d93beaa365c98349d8599eb68d21313795f380f05f5b3dfdc6272635ede1f83d308c0fdb2baf444b9ee138132d0d532c3c7e60efb25b9bf9cb62dba9833aa3706344229bd6045f0877661a073b6deef2763452d0ad7ab3404ba494b93fd6dfdf4c28e4fe83a72884a99ddf15ca030ace978f2da87b79b4f504f1d15b5b96c654f6cd5179b72ed5f84d3a16a8f0d5bf6774e7fd98d27bf3c9839"
c2 = "129d5d4ab3f9e8017d4e6761702467bbeb1b884b6c4f8ff397d078a8c41186a3d52977fa2307d5b6a0ad01fedfc3ba7b70f776ba3790a43444fb954e5afd64b1a3abeb6507cf70a5eb44678a886adf81cb4848a35afb4db7cd7818f566c7e6e2911f5ababdbdd2d4ff9825827e58d48d5466e021a64599b3e867840c07e29582961f81643df07f678a61a9f9027ebd34094e272dfbdc4619fa0ac60f0189af785df77e7ec784e086cf692a7bf7113a7fb8446a65efa8b431c6f72c14bcfa49c9b491fb1d87f2570059e0f13166a85bb555b40549f45f04bc5dbd09d8b858a5382be6497d88197ffb86381085756365bd757ec3cdfa8a77ba1728ec2de596c5ab"
c1 = int(c1,16)
c2 = int(c2,16)
d1 = libnum.invmod(e,phi_1)
d2 = libnum.invmod(e,phi_2)
m1 = pow(c1,d1,n1)
m2 = pow(c2,d2,n2)
m1 = binascii.a2b_hex(hex(m1)[2:].strip("L"))
m2 = binascii.a2b_hex(hex(m2)[2:].strip("L"))
print m1,m2
def separate(n):
	p = n % 4
	t = (p*p) % 4
	return t == 1
flag = ""
j2 = 0
j1 = 0
for i in range(100):
	if j1 == len(m1) or j2==len(m2):
		print flag
		print j1,j2,len(m1),len(m2)
		print len(flag)
		print flag+m1[20]
		exit(0)
	if separate(i):
		print j2,len(m2)
		flag += m2[j2]
		j2 += 1
	else:
		flag += m1[j1]
		j1 += 1