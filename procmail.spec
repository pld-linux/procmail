Summary:	procmail mail delivery agent
Summary(de.UTF-8):	procmail Postzustellungs-Agent
Summary(es.UTF-8):	Procmail: agente de entrega de mail
Summary(fr.UTF-8):	Agent de distribution du courrier procmail
Summary(pl.UTF-8):	Doręczyciel poczty
Summary(pt_BR.UTF-8):	Procmail: agente de entrega de correio eletrônico
Summary(ru.UTF-8):	Программа обработки почты procmail
Summary(tr.UTF-8):	procmail ileti dağıtımı
Summary(uk.UTF-8):	Програма обробки пошти procmail
Summary(zh_CN.UTF-8):	[服务器]分发mail到用户的守护进程
Summary(zh_TW.UTF-8):	[祀務器]分蛛mail到用戶的佐鰾園評
Name:		procmail
Version:	3.22
Release:	17
License:	GPL v2+ or Artistic
Group:		Applications/Mail
Source0:	http://www.procmail.org/%{name}-%{version}.tar.gz
# Source0-md5:	1678ea99b973eb77eda4ecf6acae53f1
Source1:	%{name}-skel
Source2:	%{name}-%{name}rc
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	2d534a6e29d220f59e911d2360a4d7ef
Patch0:		%{name}-lockf.patch
Patch1:		%{name}-misc.patch
Patch2:		%{name}-FHS.patch
Patch3:		private_getline.patch
Patch4:		ignore-dot.patch
Patch5:		procmail_3.22-8.debian.patch
Patch6:		procmail-3.22-CVE-2014-3618.patch
Patch7:		procmail-3.22-ipv6.patch
Patch8:		procmail-3.22-truncate.patch
URL:		http://www.procmail.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Red Hat Linux uses procmail for all local mail delivery. In addition
to regluar mail delivery duties, procmail can be used to do many
different automatic filtering, presorting, and mail handling jobs. It
is the basis for the SmartList mailing list processor.

%description -l de.UTF-8
Red Hat Linux verwendet für die Zustellung lokaler Post Procmail.
Neben den üblichen Postauslieferungsdiensten erledigt procmail auch
eine Vielzahl von anderen Dingen, etwa automatische Filterung,
Vorsortieren und Mail-Handling. "Es bildet die Grundlage für den
SmartList-Mailing-Listen-Prozessor.

%description -l es.UTF-8
El Conectiva Linux usa procmail para todas las entregas de mail
locales. En adición al servicio de entregas de mails regulares,
procmail puede ser usado para hacer varios filtros automáticos
diferentes, preselección, y trabajos con mail. Es la base para el
procesador de lista de mail SmartList.

%description -l fr.UTF-8
Red Hat Linux utilise procmail pour la délivrance de tous les
courriers locaux. En plus des tâches classiques de délivrance du
courrier, procmail peut servir à réaliser de nombreux filtrages
automatiques, des tris et des travaux de gestion du courrier. C'est la
base du gestionnaire de liste de diffusions SmartList.

%description -l pl.UTF-8
Procmail jest używany do dostarczania poczty użytkownikom. Oprócz
wynikających z powyższego obowiązków, procmail może automatycznie
filtrować, sortować i przetwarzać pocztę. Jest podstawą programu
obsługi list dyskusyjnych SmartList.

%description -l pt_BR.UTF-8
O Conectiva Linux utiliza o procmail para todas as entregas de correio
eletrônico locais. Em adição ao serviço de entregas de mails
regulares, procmail pode ser usado para fazer vários filtros
automáticos diferentes, pré-seleção, e trabalhos com mail. Ele é a
base para o processador de lista de mail SmartList.

%description -l ru.UTF-8
Программа procmail используется в PLD Linux для доставки всей
локальной почты. Кроме собственно доставки почты, procmail может быть
использован для автоматической фильтрации, сортировки и других задач
обработки почты. Также procmail является основой процессора списков
рассылки SmartList.

%description -l tr.UTF-8
Red Hat Linux tüm yerel ileti dağıtımı için procmail kullanır. Normal
ileti dağıtım görevlerine ek olarak, pek çok değişik süzme, önsıralama
ve iletiyi alma işlerini yapmak için kullanılabilir. SmartList posta
listesi yazılımının temelini oluşturur.

%description -l uk.UTF-8
Програма procmail використовується в PLD Linux для доставки всієї
локальної пошти. Крім власне доставки пошти, procmail може бути
використаний для автоматичної фільтрації, сортування та іншої обробки
пошти. Також procmail є основою процесору списків розсилки SmartList.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
echo "" | %{__make} \
	CFLAGS0="%{rpmcflags} %{rpmcppflags} -w" \
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
/etc/skel/Mail/mbox
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/procmailrc
%attr(755,root,root) %{_bindir}/formail
%attr(755,root,root) %{_bindir}/mailstat
%attr(755,root,root) %{_bindir}/procmail
%attr(2755,root,mail) %{_bindir}/lockfile
%{_mandir}/man1/formail.1*
%{_mandir}/man1/lockfile.1*
%{_mandir}/man1/procmail.1*
%{_mandir}/man5/procmailex.5*
%{_mandir}/man5/procmailrc.5*
%{_mandir}/man5/procmailsc.5*
%lang(cs) %{_mandir}/cs/man[15]/*
%lang(es) %{_mandir}/es/man[15]/*
%lang(fi) %{_mandir}/fi/man[15]/*
%lang(hu) %{_mandir}/hu/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
