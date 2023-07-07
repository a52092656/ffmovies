BB=b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
BA='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
B9='getEpisodes'
B8='Links are not available.'
B7=' - [I][COLOR khaki]'
B6='03AGdBq25eDJkrezDo2y'
B5='https://fmovies.to/ajax/episode/list/'
B4='duration'
B3='country'
B2='itemprop'
B1='quality'
B0='span>(\\d+)\\s*min<'
A_='Country\\:(.+?)<\\/div>'
Az='Genre\\:(.+?)<\\/div>'
Ay='<[^>]*>'
Ax='section'
Aw='getseasons'
Av='menutvs'
Au='menumov'
At='DefaultAddonService.png'
As='[I][COLOR violet][B]Reset all filters[/COLOR][/I][/B]'
Ar='-\t  [COLOR lightblue]rating:[/COLOR] [B]'
Aq='-\t  [COLOR lightblue]quality:[/COLOR] [B]'
Ap='-\t  [COLOR lightblue]year:[/COLOR] [B]'
Ao='-\t  [COLOR lightblue]genre:[/COLOR] [B]'
An='-\t  [COLOR lightblue]country:[/COLOR] [B]'
Am='-\t  [COLOR lightblue]sort:[/COLOR] [B]'
Al='skrajV'
Ak='ssortV'
Aj='sratyV'
Ai='fratyV'
Ah='fkrajV'
Ag='fsortV'
Af='profile'
AS='result'
AR='[B]Error[/B]'
AQ='playlink'
AP='Referer'
AO='Latin_1'
AN='https://fmovies.to'
AM='https:'
AL='videos'
AK='getLinks'
AJ='data'
AI='resetfil'
AH='DefaultAddonsSearch.png'
AG='[COLOR lightblue]Search[/COLOR]'
AF='url'
A9='\\"'
A8='vrf'
A7='span'
A6='>([^<]+)<\\/a>'
A5='data\\-id\\s*=\\s*"([^"]+)"'
A4='genre'
A3='src'
A2='div'
A1='&sort=default'
A0='search'
z='listmovies'
y='DefaultMovies.png'
x='1'
w=bytes
v=quit
s='&'
r='-'
q=', '
p='year'
o='/'
n='default'
g=str
f='strict'
e='plot'
d='href'
c='"'
b='|'
a='class'
Z=range
Y=int
X='img'
W='DefaultRecentlyAddedMovies.png'
V='[/B]'
U=chr
T=ord
S=len
O='title'
N='utf-8'
J=None
I=True
F='all'
D=False
A=''
import sys as G,os,re as C,json as AA,base64 as t
if G.version_info>=(3,0,0):AT=g;from resources.lib.cmf3 import parseDOM as H,replaceHTMLCodes;from urllib.parse import unquote,parse_qs,parse_qsl as AB,quote,urlencode,quote_plus
else:AT=unicode;from resources.lib.cmf2 import parseDOM as H,replaceHTMLCodes;from urllib import unquote,quote,urlencode,quote_plus;from urlparse import parse_qsl as AB,parse_qs
import io
from resources.lib import recaptcha_v2 as BC
import xbmc as AC,xbmcvfs,requests as BD,xbmcgui as R,xbmcplugin as L,xbmcaddon as BE,resolveurl as BF
BG=G.argv[0]
P=Y(G.argv[1])
u=dict(AB(G.argv[2][1:]))
B=BE.Addon(id='plugin.video.fmoviesto')
BH=B.getAddonInfo('path')
try:i=xbmcvfs.translatePath(B.getAddonInfo(Af))
except:i=AC.translatePath(B.getAddonInfo(Af)).decode(N)
if not os.path.exists(i):os.makedirs(i)
AU=os.path.join(i,'jfilename')
AV=os.path.join(i,'napisy')
BI=BH+'/resources/'
AW=BI+'fanart.jpg'
K=u.get(AF,J)
h=u.get(O,J)
AX=u.get('image',J)
BJ=u.get('page',[1])[0]
BK=B.getSetting(Ag)
BL=B.getSetting('fsortN')if BK else n
BM=B.getSetting('fkatV')
BN=B.getSetting('fkatN')if BM else F
BO=B.getSetting(Ah)
BP=B.getSetting('fkrajN')if BO else F
BQ=B.getSetting('frokV')
BR=B.getSetting('frokN')if BQ else F
BS=B.getSetting('fwerV')
BT=B.getSetting('fwerN')if BS else F
AY=B.getSetting('fnapV')
C4=B.getSetting('fnapN')if AY else F
BU=B.getSetting(Ai)
BV=B.getSetting('fratyN')if BU else F
BW=B.getSetting(Aj)
BX=B.getSetting('sratyN')if BW else F
AZ=B.getSetting('snapV')
C5=B.getSetting('snapN')if AZ else F
BY=B.getSetting(Ak)
BZ=B.getSetting('ssortN')if BY else n
Ba=B.getSetting('skatV')
Bb=B.getSetting('skatN')if Ba else F
Bc=B.getSetting(Al)
Bd=B.getSetting('skrajN')if Bc else F
Be=B.getSetting('srokV')
Bf=B.getSetting('srokN')if Be else F
Bg=B.getSetting('swerV')
Bh=B.getSetting('swerN')if Bg else F
Bi=B.getSetting('fdata')
Bj=B.getSetting('sdata')
Bk=I
AD='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
M={'User-Agent':AD,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'pl,en-US;q=0.7,en;q=0.3','Connection':'keep-alive','Upgrade-Insecure-Requests':x,'TE':'Trailers'}
Q=BD.Session()
def Bl(query):return BG+'?'+urlencode(query)
def E(url,name,image,mode,folder=D,IsPlayable=D,infoLabels=D,movie=I,itemcount=1,page=1,fanart=AW,moviescount=0):
	D=infoLabels;B=name;A=image;C=R.ListItem(label=B)
	if IsPlayable:C.setProperty('IsPlayable','True')
	if not D:D={O:B,e:B}
	C.setInfo(type='video',infoLabels=D);C.setArt({'thumb':A,'poster':A,'banner':A,'icon':A,'fanart':AW});E=L.addDirectoryItem(handle=P,url=Bl({'mode':mode,AF:url,'page':page,'moviescount':moviescount,'movie':movie,O:B,'image':A}),listitem=C,isFolder=folder);L.addSortMethod(P,sortMethod=L.SORT_METHOD_NONE,label2Mask='%R, %Y, %P');return E
def Bm():E('https://fmovies.to/filter?keyword=&type[]=movie','List movies',y,z,I);E(A,Am+BL+V,W,'filtr:fsort',folder=D,fanart=A);E(A,An+BP+V,W,'filtr:fkraj',folder=D,fanart=A);E(A,Ao+BN+V,W,'filtr:fkat',folder=D,fanart=A);E(A,Ap+BR+V,W,'filtr:frok',folder=D,fanart=A);E(A,Aq+BT+V,W,'filtr:fwer',folder=D,fanart=A);E(A,Ar+BV+V,W,'filtr:fraty',folder=D,fanart=A);E(A,AG,AH,A0,I);E('f',As,At,AI,folder=D);L.endOfDirectory(P)
def Bn():E('https://fmovies.to/filter?keyword=&type[]=tv','List tv-series',y,z,I);E(A,Am+BZ+V,W,'filtr:ssort',folder=D,fanart=A);E(A,An+Bd+V,W,'filtr:skraj',folder=D,fanart=A);E(A,Ao+Bb+V,W,'filtr:skat',folder=D,fanart=A);E(A,Ap+Bf+V,W,'filtr:srok',folder=D,fanart=A);E(A,Aq+Bh+V,W,'filtr:swer',folder=D,fanart=A);E(A,Ar+BX+V,W,'filtr:sraty',folder=D,fanart=A);E('s',As,At,AI,folder=D);E(A,AG,AH,A0,I);L.endOfDirectory(P)
def Bo():
	C='https://fmovies.to/movies'
	try:
		if B.getSetting('pic')!=x:Bp()
	except:pass
	E(C,'Movies',y,Au,I);E(C,'TV-Series',y,Av,I);E(A,AG,AH,A0,I);L.endOfDirectory(P)
def Bp():
	for C in['f','s']:B.setSetting(C+'sortN',n);B.setSetting(C+'sortV',A1);B.setSetting(C+'katN',F);B.setSetting(C+'katV',A);B.setSetting(C+'krajN',F);B.setSetting(C+'krajV',A);B.setSetting(C+'rokN',F);B.setSetting(C+'rokV',A);B.setSetting(C+'napN',F);B.setSetting(C+'napV',A);B.setSetting(C+'ratyN',F);B.setSetting(C+'ratyV',A);B.setSetting(C+AJ,A1);B.setSetting('pic',x);return
def Aa(exlink,page):
	K=exlink;C,F,M=Bq(K,page);N=C;G=S(C);H=AK;J=I
	for B in N:E(name=B.get(O),url=B.get(d),mode=H,image=B.get(X),folder=J,infoLabels={e:B.get(O),O:B.get(O)},itemcount=G,IsPlayable=D)
	Q=F;G=S(F);H=Aw;J=I
	for B in Q:E(name=B.get(O),url=B.get(d),mode=H,image=B.get(X),folder=J,infoLabels={e:B.get(O),O:B.get(O)},itemcount=G)
	if M:E(name='[COLOR blue]>> Next page [/COLOR]',url=K,mode=z,image=A,folder=I,page=M)
	if C or F:L.setContent(P,AL);L.endOfDirectory(P)
def Bq(url,page=1):
	t='code';s='\\&page=\\d+';r='&page=';R='&page=%d';I=page;B=url
	if'?keyword=&'in B:
		u=Bj if'=tv'in B else Bi
		if r in B:B=C.sub(s,R%Y(I),B)
		else:B=B+u+R%Y(I)
	elif r in B:B=C.sub(s,R%Y(I),B)
	else:B=B+R%Y(I)
	v='&amp;page=%d"'%(Y(I)+1);w=Q.get(B,verify=D,headers=M);J=w.content
	if G.version_info>=(3,0,0):J=J.decode(encoding=N,errors=f)
	T=[];U=[];W=D;c=H(J,'ul',attrs={a:'pagination'})
	if c:W=g(Y(I)+1)if v in c[0]else D
	h=H(J,A2,attrs={a:'movies\\s+.*?'})[0];L=[(A.start(),A.end())for A in C.finditer('<div class="item"',h)];L.append((-1,-1));T=[];U=[]
	for i in Z(S(L[:-1])):
		K=h[L[i][1]:L[i+1][0]]
		try:F=H(K,X,ret=A3)[0]
		except:F=H(K,X,ret='data-src')[0]
		F=AM+F if F.startswith('//')else F;P=H(K,'a')[-1];E=H(K,'a',ret=d)[-1];id=C.findall('([^\\-]+$)',E)[0];E=AN+E if E.startswith(o)else E;V=H(J,'i',attrs={a:'type'});V=V[0].strip()if V else A;j=A;k=C.findall('data\\-tip\\s*=\\s*"(.+?)"',K)[0];k='https://fmovies.to/ajax/film/tooltip/'+k;l=A;n=A;q=A
		if'to/tv/'in E:P=P+' [COLOR gold](serie)[/COLOR]';U.append({O:m(P),d:E+b+id,X:F,e:m(j),A4:l,p:q,t:n})
		else:T.append({O:m(P),d:E+b+id,X:F,e:m(j),A4:l,p:q,t:n})
	return T,U,W
def j(id):
	F='DZmuZuXqa9O0z3b7';F='MPPBJLgFwShfqIBx';I=id;D=Ae(F,I)
	if G.version_info>=(3,0,0):D=D.encode(AO)
	E=Ad(D)
	if G.version_info>=(3,0,0):E=E.decode(N)
	def H(matchobj):
		C=matchobj.group(0)
		if C<='Z':A=90
		else:A=122
		B=T(C)+13
		if A>=B:A=B
		else:A=B-26
		D=U(A);return D
	def J(t):
		F='[a-zA-Z]';t=C.sub(F,H,t);t=C.sub(F,H,t);E=A
		for B in Z(S(t)):
			D=T(t[B])
			if D==0:D=0
			elif B%7==4:D-=6
			elif B%7==3:D-=4
			elif B%7==5:D+=6
			elif B%7==1 or B%7==0 or B%7==6:D-=2
			elif B%7==2:D+=6
			E+=U(D)
		return E[::-1]
	B=J(E)
	if G.version_info>=(3,0,0):B=B.encode(AO)
	B=Ad(B)
	if G.version_info>=(3,0,0):B=B.decode(N)
	return B
def Br(exlink):
	s='https://fmovies.to/ajax/server/list/';r='.to/tv/';V,id=exlink.split(b);B=Q.get(V,headers=M,verify=D).content
	if G.version_info>=(3,0,0):B=B.decode(encoding=N,errors=f)
	K=C.findall(A5,B,C.DOTALL)
	if K:
		O=H(B,Ax,attrs={'id':'w\\-info.*?'})[0];T=H(O,A2,attrs={a:'description\\s*cts.*?'});T=m(T[0])if T else A;T=C.sub(Ay,A,T);F=H(O,X,ret=A3);F=F[0]if F else A;F=AM+F if F.startswith('//')else F;W=C.findall(Az,O);W=W[0]if W else A;k=C.findall(A6,W);t=q.join([A.strip().lower()for A in k])if k else A;Z=C.findall(A_,O);Z=Z[0]if Z else A;u=C.findall(A6,Z);v=q.join([A.strip()for A in u])if k else A;d=C.findall(B0,O);d=Y(d[0])*60 if d else A;l=H(O,A7,attrs={a:B1});l=l[0].strip()if l else A;g=H(O,A7,attrs={B2:'dateCreated'});g=g[0].strip()if g else A;w={e:T,A4:t,B3:v,B4:d,p:g};M.update({AP:V})
		if r in V:i=j(id)
		else:
			K=C.findall('class\\s*=\\s*"watch".*?data\\-id\\s*=\\s*"([^"]+)',B,C.DOTALL);i=j(K[0]);U=(A8,i),;J=Q.get(B5+K[0],headers=M,params=U,verify=D);B=J.content
			if G.version_info>=(3,0,0):B=B.decode(encoding=N,errors=f)
			B=B.replace(A9,c);K=C.findall(A5,B,C.DOTALL);i=j(K[0])
		AA=B6;U=(A8,i),
		if r in V:J=Q.get(s+id,headers=M,params=U,verify=D)
		else:J=Q.get(s+K[0],headers=M,params=U,verify=D)
		B=J.content
		if G.version_info>=(3,0,0):B=B.decode(encoding=N,errors=f)
		B=B.replace(A9,c)
		if'sitekey='in B:x=C.findall('data\\-sitekey="(.+?)"',B)[0];n=BC.UnCaptchaReCaptcha().processCaptcha(x,lang='en');y={'g-recaptcha-response':n};J=Q.post('https://fmovies.to/waf-verify',headers=M,data=y,cookies=Q.cookies,verify=D);U=('id',id),('token',n);J=Q.get('https://fmovies.to/ajax/film/servers',headers=M,params=U,cookies=J.cookies,verify=D)
		B=J.content
		if G.version_info>=(3,0,0):B=B.decode(encoding=N,errors=f)
		B=B.replace(A9,c);o=C.findall('data\\-link\\-id\\s*=\\s*"([^"]+).*?<span>([^<]+)',B)
		for(z,A0)in o:A1=h+B7+A0+'[/I] '+' [B][/COLOR][/B]';E(name=A1,url=z+b+V,mode=AQ,image=F,folder=D,infoLabels=w,IsPlayable=I)
		if S(o)>0:L.setContent(P,AL);L.endOfDirectory(P)
		else:R.Dialog().notification(AR,B8,R.NOTIFICATION_INFO,8000,D)
def Bs(chra):
	B=chra;C=['\\xc4\\x99','\\xc5\\x82','\\xc5\\x81','\\xc4\\x98','\\xc5\\x9b','\\xc5\\x9a']
	try:
		if G.version_info>=(3,0,0):
			B=repr(B.encode(N))
			if any(A in B for A in C):return D
			B=B.replace('\\xc3\\xaa','ę').replace('\\xc3\\x8a','Ę');B=B.replace('\\xc3\\xa6','ć').replace('\\xc3\\x86','Ć');B=B.replace('\\xc2\\xbf','ż').replace('\\xc2\\x9f','Ż');B=B.replace('\\xc2\\xb9','ą').replace('\\xc2\\x99','Ą');B=B.replace('\\xc5\\x93','ś').replace('\\xc5\\x92','Ś');B=B.replace('\\xc3\\xb3','ó').replace('\\xc3\\x93','Ó');B=B.replace('\\xc5\\xb8','ź').replace('\\xc5\\xb7','Ź');B=B.replace('\\xc2\\xb3','ł').replace('\\xc2\\x93','Ł');B=B.replace('\\xc3\\xb1','ń').replace('\\xc3\\x91','Ń');B=B.replace("b'",A);B=B.replace('\\n','\n').replace('\\r','\r');B=B.replace("\\'","'")
		else:B=B.replace('Ãª','ę').replace('Ã\x8a','Ę');B=B.replace('Ã¦','ć').replace('Ã\x86','Ć');B=B.replace('Â¿','ż').replace('Â\x9f','Ż');B=B.replace('Â¹','ą').replace('Â\x99','Ą');B=B.replace('Å\x93','ś').replace('Å\x92','Ś');B=B.replace('Ã³','ó').replace('Ã\x93','Ó');B=B.replace('Å¸','ź').replace('Å·','Ź');B=B.replace('Â³','ł').replace('Â\x93','Ł');B=B.replace('Ã±','ń').replace('Ã\x91','Ń')
	except:pass
	return B
def Bt(subtlink):
	try:
		A=Q.get(subtlink,headers=M,verify=D)
		if G.version_info>=(3,0,0):A=A.text
		else:A=A.content
		B=Bs(A);open(AV,'w').write(B);return I
	except:return D
def Bu(exlink):
	s='status';r='&Referer=';q='|User-Agent=';p='m3u8';n='sources';m='media';l='success';k='subt';c='file';U='label';id,t=exlink.split(b);u=j(id);w=(A8,u),;M.update({AP:t});E=Q.get('https://fmovies.to/ajax/server/'+id,headers=M,params=w,verify=D);V=E.content
	if G.version_info>=(3,0,0):V=V.decode(encoding=N,errors=f)
	try:d=AA.loads(V)
	except:pass
	if d:x=d.get(AS,J).get(AF,J)
	F=Bv(x);T='?sub.info=';T=T if T in F else'?subtitle_json='
	try:H,B=F.split(T)
	except:H=F;B=A
	K=[];e=unquote(B);B=D
	if e:
		E=Q.get(e,headers=M,verify=D).json()
		for W in E:B=W.get(A3,J);y=W.get(c,J);B=B if B else y;z=W.get(U,J);K.append({U:z,k:B})
	if Bk and K:
		A0=[A.get(U)for A in K];X=R.Dialog().select('Subtitle language',A0)
		if X>-1:
			B=K[X].get(k)
			if K[X].get(U)=='Polish':B=AV if Bt(B)else B
		else:B=D
	if'mcloud'in F or'vizcloud'in F:
		A1='(?://|\\.)((?:my?|viz)cloud\\.(?:to|digital|cloud))/(?:embed|e)/([0-9a-zA-Z]+)';Y=C.findall(A1,H,C.DOTALL)
		if Y:h=Y[0][1];A5=Y[0][0];A2=C2(h).replace('=',A).replace(o,'_');H=C.sub('/(?:embed|e)/','/info/',F).replace(h,A2.replace('=',A).replace(o,'_'))
		O=A
		try:
			E=Q.get(H,headers=M,verify=D).json();A6=[]
			if l in E:
				if E.get(l,J):
					Z=E.get(m,J).get(n,J)
					for a in Z:
						S=a.get(c,J)
						if p in S:O=S+q+AD+r+F;break
			elif s in E:
				if E.get(s,J)==200:
					Z=E.get(AJ,J).get(m,J).get(n,J)
					for a in Z:
						S=a.get(c,J)
						if p in S:O=S+q+AD+r+F;break
		except:pass
	else:
		try:O=BF.resolve(H)
		except Exception as A4:R.Dialog().notification(AR,g(A4),R.NOTIFICATION_INFO,8000,D);v()
	if O:
		i=R.ListItem(path=O)
		if B:i.setSubtitles([B])
		L.setResolvedUrl(P,I,listitem=i)
def Bv(mainurl):A=mainurl;C=A[0:6];E=A[6:];C='hlPeNwkncH0fq9so';D=C1(A);B=Ae(C,D);B=unquote(B);return B
def Bw():
	from contextlib import closing as B;from xbmcvfs import File
	with B(File(AU))as C:A=C.read()
	A=AA.loads(A);D=A.get(AS,J);return D
def Bx(hrefx):
	k='name';i=hrefx;V,W=i.split(b);Z=Q.get(V,headers=M,verify=D).content
	if G.version_info>=(3,0,0):Z=Z.decode(encoding=N,errors=f)
	B=H(Z,Ax,attrs={'id':'w\\-info'})[0];K=H(B,A2,attrs={a:'description.*?'});J=H(B,'h1',attrs={B2:k,a:k});J='[B]'+J[0]+'[/B] 'if J else A;K=J+'[CR]'+K[0]if K else A;F=H(B,X,ret=A3);F=F[0]if F else A;F=AM+F if F.startswith('//')else F;O=C.findall(Az,B);O=O[0]if O else A;c=C.findall(A6,O);l=q.join([A.strip().lower()for A in c])if c else A;S=C.findall(A_,B);S=S[0]if S else A;m=C.findall(A6,S);n=q.join([A.strip()for A in m])if c else A;T=C.findall(B0,B);T=Y(T[0])*60 if T else A;d=H(B,A7,attrs={a:B1});d=d[0].strip()if d else A;U=H(B,A7,attrs={a:p});U=U[0].strip()if U else A;r={e:K,A4:l,B3:n,B4:T,p:U};W=1
	try:g,s=C.findall('href="([^"]+)"\\n\\s*data-kname="%s".*?data\\-ep=\\\'({.*?)}'%i,htmlx,C.DOTALL)[0]
	except:W=0
	V=AN+g if g.startswith(o)else g;t=C.findall('data-id="([^"]+).*?<div>([^<]+)',htmlx,C.DOTALL);u='- '+h if J else h
	for(v,w)in t:
		x=J+u+B7+w+'[/I][/COLOR] ';j=C.findall(v+'"\\:"([^"]+)',s)
		if j:E(name=x,url=j[0]+b+V,mode=AQ,image=F,folder=D,infoLabels=r,IsPlayable=I)
	if W:L.setContent(P,AL);L.endOfDirectory(P)
	else:R.Dialog().notification(AR,B8,R.NOTIFICATION_INFO,8000,D)
def By(exlink):
	B=Bz(exlink);C=S(B)
	for A in B:E(name=A.get(O),url=A.get(d),mode=AK,image=A.get(X),folder=I,infoLabels={e:h},itemcount=C,IsPlayable=I)
	L.setContent(P,'files');L.endOfDirectory(P)
def Bz(href):
	B=href;F,Q=B.split(b);K=Bw();L=H(K,'ul',attrs={a:'episodes','data\\-season':g(F)})[0];G=[];M=H(L,'li')
	for E in M:
		N=C.findall(A5,E,C.DOTALL)[0];P='S%02d'%Y(F);I=C.findall('data\\-num\\s*=\\s*"([^"]+)"',E,C.DOTALL)[0]
		try:J='E%02d'%Y(I)
		except:J='E-%s'%g(I)
		D=C.findall('span>\\s*<span>([^<]+)',E,C.DOTALL)
		if D:D=C.sub(Ay,A,D[0].strip())
		else:D=h.split(r)[-1]
		D=D+' ('+P+J+')';B=H(E,'a',ret=d)[-1];B=AN+B if B.startswith(o)else B;G.append({O:D,d:B+b+N,X:AX})
	return G
def B_(exlink):
	B=C0(exlink);C=S(B)
	for A in B:E(name=A.get(O),url=A.get(d),mode=B9,image=A.get(X),folder=I,infoLabels={e:h},itemcount=C,IsPlayable=I)
	L.setContent(P,'files');L.endOfDirectory(P)
def C0(href):
	F=href;L=[];F,id=F.split(b);M.update({AP:F});E=Q.get(F,headers=M,verify=D).content
	if G.version_info>=(3,0,0):E=E.decode(encoding=N,errors=f)
	K=C.findall(A5,E,C.DOTALL);P=B.getSetting('cap_token')
	if not P:P=B6
	if K:
		T=j(K[0]);U=(A8,T),;R=Q.get(B5+K[0],headers=M,params=U,verify=D);E=R.content
		if G.version_info>=(3,0,0):E=E.decode(encoding=N,errors=f)
		E=E.replace(A9,c);S=R.json()
		with io.open(AU,'w',encoding='utf8')as V:W=AA.dumps(S,indent=4,sort_keys=I,separators=(',',': '),ensure_ascii=D);V.write(AT(W))
		E=S.get(AS,J);Y=H(E,A2,attrs={a:'head'})[0];Z=C.findall('<a(.*?<)\\/a>',Y,C.DOTALL)
		for e in Z:g,i=C.findall('data\\-season\\s*=\\s*"([^"]+)"\\s*>([^<]+)<',e,C.DOTALL)[0];k=A;L.append({O:i+h,d:g+b+k,X:AX})
	return L
try:import string as Ab;k=BA;l=BA;Ac=Ab.maketrans(k,l);AE=Ab.maketrans(l,k)
except:k=BB;l=BB;Ac=w.maketrans(k,l);AE=w.maketrans(l,k)
def Ad(input):return t.b64encode(input).translate(Ac)
def C1(input):
	try:A=input.translate(AE)
	except:A=g(input).translate(AE)
	return t.b64decode(A)
def C2(media_id):
	F=media_id
	try:import string as P;I='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';J='51wJ0FDq/UVCefLopEcmK3ni4WIQztMjZdSYOsbHr9R2h7PvxBGAuglaN8+kXT6y';Q=P.maketrans(I,J);L=P.maketrans(J,I)
	except:I=b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';J=b'51wJ0FDq/UVCefLopEcmK3ni4WIQztMjZdSYOsbHr9R2h7PvxBGAuglaN8+kXT6y';Q=w.maketrans(I,J);L=w.maketrans(J,I)
	def M(input):return t.b64encode(input).translate(Q)
	def V(input):
		try:A=input.translate(L)
		except:A=g(input).translate(L)
		return t.b64decode(A)
	try:F=M(F)
	except:F=M(F.encode(N)).decode(N)
	R='dOuhV3IsSvf7jeI5';B=list(Z(0,256));D=0;E=A;H=256;C=0
	for C in Z(H):D=(D+B[C]+T(R[C%S(R)]))%H;O=B[C];B[C]=B[D];B[D]=O
	D=C=0;K=0
	for K in Z(S(F)):
		C=(C+K)%H;D=(D+B[C])%H;O=B[C];B[C]=B[D];B[D]=O
		if G.version_info>=(3,0,0):
			try:E+=U(F[K]^B[(B[C]+B[D])%H])
			except:E+=U(T(F[K])^B[(B[C]+B[D])%H])
		else:E+=U(T(F[K])^B[(B[C]+B[D])%H])
	if G.version_info>=(3,0,0):E=E.encode(AO)
	E=M(E)
	if G.version_info>=(3,0,0):E=E.decode(N)
	return E
def C6(t,n):
	H=[];B=[];D=0;I=A;E=256
	for C in Z(E):B.append(C)
	C=0
	for C in Z(E):D=(D+B[C]+T(t[C%S(t)]))%E;H=B[C];B[C]=B[D];B[D]=H
	F=0;D=0;C=0
	for F in Z(S(n)):
		C=(C+F)%E;D=(D+B[C])%E;H=B[C];B[C]=B[D];B[D]=H
		if G.version_info>=(3,0,0):
			try:I+=U(n[F]^B[(B[C]+B[D])%E])
			except:I+=U(T(n[F])^B[(B[C]+B[D])%E])
		else:I+=U(T(n[F])^B[(B[C]+B[D])%E])
	return I
def Ae(r,o):
	E=[];B=[];D=0;F=A
	for C in Z(256):B.append(C)
	for C in Z(256):D=(D+B[C]+T(r[C%S(r)]))%256;E=B[C];B[C]=B[D];B[D]=E
	C=0;D=0
	for H in Z(S(o)):
		C=C+1;D=(D+B[C%256])%256
		if not C in B:C=0;E=B[C];B[C]=B[D];B[D]=E;F+=U(T(o[H])^B[(B[C]+B[D])%256])
		else:
			E=B[C];B[C]=B[D];B[D]=E
			if G.version_info>=(3,0,0):
				try:F+=U(o[H]^B[(B[C]+B[D])%256])
				except:F+=U(T(o[H])^B[(B[C]+B[D])%256])
			else:F+=U(T(o[H])^B[(B[C]+B[D])%256])
	return F
def m(char):
	G='&quot;';F='&#8230;';E='&#8211;';D='&#8217;';C='\\u0144';B='...';A=char
	if type(A)is not g:A=A.encode(N)
	A=A.replace('\\u0105','Ä\x85').replace('\\u0104','Ä\x84');A=A.replace('\\u0107','Ä\x87').replace('\\u0106','Ä\x86');A=A.replace('\\u0119','Ä\x99').replace('\\u0118','Ä\x98');A=A.replace('\\u0142','Å\x82').replace('\\u0141','Å\x81');A=A.replace(C,'Å\x84').replace(C,'Å\x83');A=A.replace('\\u00f3','Ã³').replace('\\u00d3','Ã\x93');A=A.replace('\\u015b','Å\x9b').replace('\\u015a','Å\x9a');A=A.replace('\\u017a','Åº').replace('\\u0179','Å¹');A=A.replace('\\u017c','Å¼').replace('\\u017b','Å»');A=A.replace(D,"'");A=A.replace(E,r);A=A.replace(F,B);A=A.replace('&gt;','>');A=A.replace('&Iacute;','Í').replace('&iacute;','í');A=A.replace('&icirc;','î').replace('&Icirc;','Î');A=A.replace('&oacute;','ó').replace('&Oacute;','Ó');A=A.replace(G,c).replace('&amp;quot;',c);A=A.replace('&bdquo;',c).replace('&rdquo;',c);A=A.replace('&Scaron;','Š').replace('&scaron;','š');A=A.replace('&ndash;',r).replace('&mdash;',r);A=A.replace('&Auml;','Ä').replace('&auml;','ä');A=A.replace(D,"'");A=A.replace(E,r);A=A.replace(F,B);A=A.replace('&#8222;',c).replace('&#8221;',c);A=A.replace('[&hellip;]',B);A=A.replace('&#038;',s);A=A.replace('&#039;',"'");A=A.replace(G,c);A=A.replace('&nbsp;','.').replace('&amp;',s);A=A.replace('Napisy PL','[COLOR lightblue](napisy pl)[/COLOR]');A=A.replace('Lektor PL','[COLOR lightblue](lektor pl)[/COLOR]');A=A.replace('Dubbing PL','[COLOR lightblue](dubbing pl)[/COLOR]');return A
def C3(paramstring):
	T='Container.Refresh';S='Select ';Q='nap';P='sort';L=dict(AB(paramstring))
	if L:
		D=L.get('mode',J)
		if D==z:Aa(K,BJ)
		elif D==AK:Br(K)
		elif D==AQ:Bu(K)
		elif D==Au:Bm()
		elif D==Av:Bn()
		elif'filtr'in D:
			E=D.split(':')[1]
			if'wer'in E:I='quality:';G=[F,'HD','HDRip','SD','TS','CAM'];H=[A,'quality[]=HD','quality[]=HDRip','quality[]=SD','quality[]=TS','quality[]=CAM']
			elif'kraj'in E:I='country:';G=[F,'Argentina','Australia','Austria','Belgium','Brazil','Canada','China','Czech Republic','Denmark','Finland','France','Germany','Hong Kong','Hungary','India','Ireland','Israel','Italy','Japan','Luxembourg','Mexico','Netherlands','New Zealand','Norway','Philippines','Poland','Romania','Russia','South Africa','South Korea','Spain','Sweden','Switzerland','Thailand','Turkey','United Kingdom','United States'];H=[A,'country[]=181863','country[]=181851','country[]=181882','country[]=181849','country[]=181867','country[]=181861','country[]=108','country[]=181859','country[]=181855','country[]=181877','country[]=11','country[]=1025332','country[]=2630','country[]=181876','country[]=34','country[]=181862','country[]=181887','country[]=181857','country[]=36','country[]=181878','country[]=181852','country[]=181848','country[]=181847','country[]=181901','country[]=1025339','country[]=181880','country[]=181895','country[]=181860','country[]=181850','country[]=1025429','country[]=181871','country[]=181883','country[]=181869','country[]=94','country[]=1025379','country[]=8','country[]=2']
			elif'rok'in E:I='year:';G=[F,'2023','2022','2021','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2000s','1990s','1980s','1970s','1960s','1950s','1940s','1930s','1920s','1910s'];H=[A,'year[]=2023','year[]=2022','year[]=2021','year[]=2020','year[]=2019','year[]=2018','year[]=2017','year[]=2016','year[]=2015','year[]=2014','year[]=2013','year[]=2012','year[]=2011','year[]=2010','year[]=2009','year[]=2008','year[]=2007','year[]=2006','year[]=2005','year[]=2004','year[]=2003','year[]=2000s','year[]=1990s','year[]=1980s','year[]=1970s','year[]=1960s','year[]=1950s','year[]=1940s','year[]=1930s','year[]=1920s','year[]=1910s']
			elif'raty'in E:I='rating:';G=[F,'12','13+','16+','18','18+','AO','C','E','G','GP','M','M/PG','MA-13','MA-17','NC-17','PG','PG-13','R','TV_MA','TV-13','TV-14','TV-G','TV-MA','TV-PG','TV-Y','TV-Y7','TV-Y7-FV','X'];H=[A,'rating[]=12','rating[]=13%2B','rating[]=16%2B','rating[]=18','rating[]=18%2B','rating[]=AO','rating[]=C','rating[]=E','rating[]=G','rating[]=GP','rating[]=M','rating[]=M%2FPG','rating[]=MA-13','rating[]=MA-17','rating[]=NC-17','rating[]=PG','rating[]=PG-13','rating[]=R','rating[]=TV_MA','rating[]=TV-13','rating[]=TV-14','rating[]=TV-G','rating[]=TV-MA','rating[]=TV-PG','rating[]=TV-Y','rating[]=TV-Y7','rating[]=TV-Y7-FV','rating[]=X']
			elif'kat'in E:I='genre:';G=[F,'action','adult','adventure','animation','biography','comedy','costume','crime','documentary','drama','family','fantasy','film-noir','game-show','history','horror','kungfu','music','musical','mystery','news','reality','reality-tv','romance','sci-fi','short','sport','talk','talk-show','thriller','tv movie','tv show','war','western'];H=['genre_mode=and','genre[]=25','genre[]=1068691','genre[]=17','genre[]=10','genre[]=215','genre[]=14','genre[]=1693','genre[]=26','genre[]=131','genre[]=1','genre[]=43','genre[]=31','genre[]=1068395','genre[]=212','genre[]=47','genre[]=74','genre[]=248','genre[]=199','genre[]=1066604','genre[]=64','genre[]=1066549','genre[]=1123750','genre[]=4','genre[]=23','genre[]=15','genre[]=1066916','genre[]=44','genre[]=1124002','genre[]=1067786','genre[]=7','genre[]=1123752','genre[]=139','genre[]=58','genre[]=28']
			elif P in E:I='sort (by):';H=['sort=default','sort=recently_updated','sort=recently_added','sort=release_date','sort=trending','sort=title_az','sort=scores','sort=imdb','sort=most_watched','most_favourited'];G=[n,'recently updated','recently added','release date','trending','title a-z','scores','imdb','most watched','most favourited']
			elif Q in E:I='subtitles:';H=[A,'subtitle[]=1','subtitle[]=0'];G=[F,'on','off']
			if P in E or Q in E:C=R.Dialog().select(S+I,G)
			else:C=R.Dialog().multiselect(S+I,G)
			if C:
				if isinstance(C,list):
					if 0 in C:C=[0]
					M=s+'%s'%s.join([H[A]for A in C])if C[0]!=0 else A;N=q.join([G[A]for A in C])
				else:C=C if C>-1 else v();M=s+'%s'%H[C]if H[C]else A;N=G[C]
				B.setSetting(E+'V',M);B.setSetting(E+'N',N);U=B.getSetting(Ag);V=B.getSetting('fkatV');W=B.getSetting(Ah);X=B.getSetting('frokV');Y=B.getSetting('fwerV');Z=B.getSetting(Ai);a=B.getSetting(Aj);b=B.getSetting(Ak);c=B.getSetting('skatV');d=B.getSetting(Al);e=B.getSetting('srokV');f=B.getSetting('swerV');g=V+AY+Y+U+X+W+Z;h=c+AZ+f+b+e+d+a;B.setSetting('fdata',g);B.setSetting('sdata',h);AC.executebuiltin(T)
			else:v()
		elif D==Aw:B_(K)
		elif D==B9:By(K)
		elif D=='getLinksSerial':Bx(K)
		elif D==AI:B.setSetting(K+'sortN',n);B.setSetting(K+'sortV',A1);B.setSetting(K+'katN',F);B.setSetting(K+'katV',A);B.setSetting(K+'krajN',F);B.setSetting(K+'krajV',A);B.setSetting(K+'rokN',F);B.setSetting(K+'rokV',A);B.setSetting(K+'napN',F);B.setSetting(K+'napV',A);B.setSetting(K+'ratyN',F);B.setSetting(K+'ratyV',A);B.setSetting(K+AJ,A1);AC.executebuiltin(T)
		elif D==A0:
			O=R.Dialog().input('Search...',type=R.INPUT_ALPHANUM)
			if O:i='https://fmovies.to/filter?keyword='+O.replace(' ','+');Aa(i,x)
			else:v()
	else:Bo()
if __name__=='__main__':C3(G.argv[2][1:])