Summary:	procmail mail delivery agent
Summary(de):	procmail Postzustellungs-Agent 
Summary(fr):	Agent de distribution du courrier procmail
Summary(pl):	Dor�czyciel poczty
Summary(tr):	procmail ileti da��t�m�
Name:		procmail
Version:	3.21
Release:	1
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://ftp.procmail.org/pub/procmail/%{name}-%{version}.tar.gz
Source1:	%{name}-skel
Source2:	%{name}-procmailrc
Patch0:		%{name}-lockf.patch
Patch1:		%{name}-misc.patch
Patch2:		%{name}-FHS.patch
Patch3:		%{name}-no_libnsl.patch
Patch4:		%{name}-maildir_name.patch
URL:		http://www.procmail.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Red Hat Linux uses procmail for all local mail delivery. In addition
to regluar mail delivery duties, procmail can be used to do many
different automatic filtering, presorting, and mail handling jobs. It
is the basis for the SmartList mailing list processor.

%description -l de
Red Hat Linux verwendet f�r die Zustellung lokaler Post Procmail.
Neben den �blichen Postauslieferungsdiensten erledigt procmail auch
eine Vielzahl von anderen Dingen, etwa automatische Filterung,
Vorsortieren und Mail-Handling. "Es bildet die Grundlage f�r den
SmartList-Mailing-Listen-Prozessor.

%description -l fr
Red Hat Linux utilise procmail pour la d�livrance de tous les
courriers locaux. En plus des t�ches classiques de d�livrance du
courrier, procmail peut servir � r�aliser de nombreux filtrages
automatiques, des tris et des travaux de gestion du courrier. C'est la
base du gestionnaire de liste de diffusions SmartList.

%description -l pl
Procmail jest u�ywany do dostarczania poczty u�ytkownikom. Opr�cz
wynikaj�cych z powy�szego obowi�zk�w, procmail mo�e automatycznie
filtrowa�, sortowa� i przetwarza� poczte. Jest podstaw� programu
obs�ugi list dyskusyjnych SmartList.

%description -l tr
Red Hat Linux t�m yerel ileti da��t�m� i�in procmail kullan�r. Normal
ileti da��t�m g�revlerine ek olarak, pek �ok de�i�ik s�zme, �ns�ralama
ve iletiyi alma i�lerini yapmak i�in kullan�labilir. SmartList posta
listesi yaz�l�m�n�n temelini olu�turur.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
echo "" | make CFLAGS0="%{rpmcflags} -w"

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(700,root,root) %dir /etc/skel/Mail
/etc/skel/Mail/*
%config(noreplace) /etc/procmailrc

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
