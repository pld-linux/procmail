Summary:     procmail mail delivery agent
Summary(de): procmail Postzustellungs-Agent 
Summary(fr): Agent de distribution du courrier procmail
Summary(pl): dor�czyciel poczty
Summary(tr): procmail ileti da��t�m�
Name:        procmail
Version:     3.10
Release:     14
Copyright:   distributable
Group:       Daemons
Source:      ftp://ftp.informatik.rwth-aachen.de/pub/packages/procmail/%{name}-%{version}.tar.gz
Patch0:      %{name}-%{version}-misc.patch
Patch1:      %{name}-%{version}-lockf.patch
Patch2:      %{name}-%{version}-000lock.patch
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Red Hat Linux uses procmail for all local mail delivery.  In addition
to regluar mail delivery duties, procmail can be used to do many 
different automatic filtering, presorting, and mail handling jobs.
It is the basis for the SmartList mailing list processor.

%description -l de
Red Hat Linux verwendet f�r die Zustellung lokaler Post Procmail. 
Neben den �blichen Postauslieferungsdiensten erledigt procmail auch 
eine Vielzahl von anderen Dingen, etwa automatische Filterung, 
Vorsortieren und Mail-Handling. "Es bildet die Grundlage f�r den 
SmartList-Mailing-Listen-Prozessor. 

%description -l fr
Red Hat Linux utilise procmail pour la d�livrance de tous les courriers locaux.
En plus des t�ches classiques de d�livrance du courrier, procmail peut servir �
r�aliser de nombreux filtrages automatiques, des tris et des travaux de gestion
du courrier. C'est la base du gestionnaire de liste de diffusions SmartList. 

%description -l pl
Procmail jest u�ywany do dostarczania poczty u�ytkownikom. Opr�cz
wynikaj�cych z powy�szego obowi�zk�w, procmail mo�e automatycznie
filtrowa�, sortowa� i przetwarza� poczte. Jest podstaw� programu obs�ugi
list dyskusyjnych SmartList.

%description -l tr
Red Hat Linux t�m yerel ileti da��t�m� i�in procmail kullan�r. Normal ileti
da��t�m g�revlerine ek olarak, pek �ok de�i�ik s�zme, �ns�ralama ve iletiyi
alma i�lerini yapmak i�in kullan�labilir. SmartList posta listesi yaz�l�m�n�n
temelini olu�turur.

%prep
%setup -q
%patch -p1
%patch1 -p1 
%patch2 -p1 

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1,man/man5}

make BASENAME=$RPM_BUILD_ROOT/usr install.bin install.man

strip $RPM_BUILD_ROOT/usr/bin/{procmail,lockfile,formail}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(6755, root, mail) /usr/bin/procmail
%attr(2755, root, mail) /usr/bin/lockfile
%attr(0755, root, root) /usr/bin/formail
%attr(0755, root, root) /usr/bin/mailstat
%attr(0644, root,  man) /usr/man/man[15]/*

%changelog
* Sun Oct 11 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- added pl translation,
- some minor changes.

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
