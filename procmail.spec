Summary:	procmail mail delivery agent
Summary(de):	procmail Postzustellungs-Agent
Summary(es):	Procmail: agente de entrega de mail
Summary(fr):	Agent de distribution du courrier procmail
Summary(pl):	Dorêczyciel poczty
Summary(pt_BR):	Procmail: agente de entrega de correio eletrônico
Summary(ru):	ðÒÏÇÒÁÍÍÁ ÏÂÒÁÂÏÔËÉ ÐÏÞÔÙ procmail
Summary(tr):	procmail ileti daðýtýmý
Summary(uk):	ðÒÏÇÒÁÍÁ ÏÂÒÏÂËÉ ÐÏÛÔÉ procmail
Summary(zh_CN):	[·þÎñÆ÷]·Ö·¢mailµ½ÓÃ»§µÄÊØ»¤½ø³Ì
Summary(zh_TW):	[ªÁ°È¾¹]¤Àµïmail¨ì¥Î¤áªº¦õÅÀ¶éµû
Name:		procmail
Version:	3.22
Release:	10
License:	GPL v2
Group:		Daemons
Source0:	ftp://ftp.procmail.org/pub/procmail/%{name}-%{version}.tar.gz
# Source0-md5:	1678ea99b973eb77eda4ecf6acae53f1
Source1:	%{name}-skel
Source2:	%{name}-%{name}rc
Source3:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-lockf.patch
Patch1:		%{name}-misc.patch
Patch2:		%{name}-FHS.patch
URL:		http://www.procmail.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Red Hat Linux uses procmail for all local mail delivery. In addition
to regluar mail delivery duties, procmail can be used to do many
different automatic filtering, presorting, and mail handling jobs. It
is the basis for the SmartList mailing list processor.

%description -l de
Red Hat Linux verwendet für die Zustellung lokaler Post Procmail.
Neben den üblichen Postauslieferungsdiensten erledigt procmail auch
eine Vielzahl von anderen Dingen, etwa automatische Filterung,
Vorsortieren und Mail-Handling. "Es bildet die Grundlage für den
SmartList-Mailing-Listen-Prozessor.

%description -l es
El Conectiva Linux usa procmail para todas las entregas de mail
locales. En adición al servicio de entregas de mails regulares,
procmail puede ser usado para hacer varios filtros automáticos
diferentes, preselección, y trabajos con mail. Es la base para el
procesador de lista de mail SmartList.

%description -l fr
Red Hat Linux utilise procmail pour la délivrance de tous les
courriers locaux. En plus des tâches classiques de délivrance du
courrier, procmail peut servir à réaliser de nombreux filtrages
automatiques, des tris et des travaux de gestion du courrier. C'est la
base du gestionnaire de liste de diffusions SmartList.

%description -l pl
Procmail jest u¿ywany do dostarczania poczty u¿ytkownikom. Oprócz
wynikaj±cych z powy¿szego obowi±zków, procmail mo¿e automatycznie
filtrowaæ, sortowaæ i przetwarzaæ poczte. Jest podstaw± programu
obs³ugi list dyskusyjnych SmartList.

%description -l pt_BR
O Conectiva Linux utiliza o procmail para todas as entregas de correio
eletrônico locais. Em adição ao serviço de entregas de mails
regulares, procmail pode ser usado para fazer vários filtros
automáticos diferentes, pré-seleção, e trabalhos com mail. Ele é a
base para o processador de lista de mail SmartList.

%description -l ru
ðÒÏÇÒÁÍÍÁ procmail ÉÓÐÏÌØÚÕÅÔÓÑ × PLD Linux ÄÌÑ ÄÏÓÔÁ×ËÉ ×ÓÅÊ ÌÏËÁÌØÎÏÊ
ÐÏÞÔÙ. ëÒÏÍÅ ÓÏÂÓÔ×ÅÎÎÏ ÄÏÓÔÁ×ËÉ ÐÏÞÔÙ, procmail ÍÏÖÅÔ ÂÙÔØ ÉÓÐÏÌØÚÏ×ÁÎ
ÄÌÑ Á×ÔÏÍÁÔÉÞÅÓËÏÊ ÆÉÌØÔÒÁÃÉÉ, ÓÏÒÔÉÒÏ×ËÉ É ÄÒÕÇÉÈ ÚÁÄÁÞ ÏÂÒÁÂÏÔËÉ
ÐÏÞÔÙ. ôÁËÖÅ procmail Ñ×ÌÑÅÔÓÑ ÏÓÎÏ×ÏÊ ÐÒÏÃÅÓÓÏÒÁ ÓÐÉÓËÏ× ÒÁÓÓÙÌËÉ
SmartList.

%description -l tr
Red Hat Linux tüm yerel ileti daðýtýmý için procmail kullanýr. Normal
ileti daðýtým görevlerine ek olarak, pek çok deðiþik süzme, önsýralama
ve iletiyi alma iþlerini yapmak için kullanýlabilir. SmartList posta
listesi yazýlýmýnýn temelini oluþturur.

%description -l uk
ðÒÏÇÒÁÍÁ procmail ×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ × PLD Linux ÄÌÑ ÄÏÓÔÁ×ËÉ ×Ó¦¤§
ÌÏËÁÌØÎÏ§ ÐÏÛÔÉ. ëÒ¦Í ×ÌÁÓÎÅ ÄÏÓÔÁ×ËÉ ÐÏÛÔÉ, procmail ÍÏÖÅ ÂÕÔÉ
×ÉËÏÒÉÓÔÁÎÉÊ ÄÌÑ Á×ÔÏÍÁÔÉÞÎÏ§ Æ¦ÌØÔÒÁÃ¦§, ÓÏÒÔÕ×ÁÎÎÑ ÔÁ ¦ÎÛÏ§
ÏÂÒÏÂËÉ ÐÏÛÔÉ. ôÁËÏÖ procmail ¤ ÏÓÎÏ×ÏÀ ÐÒÏÃÅÓÏÒÕ ÓÐÉÓË¦× ÒÏÚÓÉÌËÉ
SmartList.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
echo "" | %{__make} \
	CFLAGS0="%{rpmcflags} -w" \
	SEARCHLIBS="-lm"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}} \
	$RPM_BUILD_ROOT/etc/skel/Mail

%{__make} install.bin install.man \
	BASENAME=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.procmailrc
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/procmailrc
:> $RPM_BUILD_ROOT/etc/skel/Mail/mbox

bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(700,root,root) %dir /etc/skel/Mail
/etc/skel/Mail/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/procmailrc

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
%lang(cs) %{_mandir}/cs/man[15]/*
%lang(es) %{_mandir}/es/man[15]/*
%lang(fi) %{_mandir}/fi/man[15]/*
%lang(hu) %{_mandir}/hu/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
