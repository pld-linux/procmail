Summary:	procmail mail delivery agent
Summary(de):	procmail Postzustellungs-Agent 
Summary(fr):	Agent de distribution du courrier procmail
Summary(pl):	Dorêczyciel poczty
Summary(tr):	procmail ileti daðýtýmý
Name:		procmail
Version:	3.14
Release:	5
License:	GPL
Group:		Daemons
Group(pl):	Serwery
Source0:	ftp://ftp.informatik.rwth-aachen.de/pub/packages/procmail/%{name}-%{version}.tar.gz
Source1:	%{name}-skel
Patch0:		%{name}-lockf.patch
Patch1:		%{name}-misc.patch
Patch2:		%{name}-FHS.patch
Patch3:		%{name}-overrun.patch
Patch4:		%{name}-no_libnsl.patch
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

%description -l tr
Red Hat Linux tüm yerel ileti daðýtýmý için procmail kullanýr. Normal
ileti daðýtým görevlerine ek olarak, pek çok deðiþik süzme, önsýralama
ve iletiyi alma iþlerini yapmak için kullanýlabilir. SmartList posta
listesi yazýlýmýnýn temelini oluþturur.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
echo "" | make CFLAGS0="$RPM_OPT_FLAGS -w"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}} \
	$RPM_BUILD_ROOT/etc/skel/{C/Mail,pl/Mail}

%{__make} install.bin install.man \
	BASENAME=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

strip $RPM_BUILD_ROOT%{_bindir}/{procmail,lockfile,formail}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/skel/pl/.procmailrc
:> $RPM_BUILD_ROOT/etc/skel/C/Mail/mbox
:> $RPM_BUILD_ROOT/etc/skel/pl/Mail/mbox

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,5}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(700,root,root) %dir /etc/skel/C/Mail
/etc/skel/C/Mail/*
%lang(pl) %attr(700,root,root) %dir /etc/skel/pl/Mail
%lang(pl) /etc/skel/pl/Mail/*

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
