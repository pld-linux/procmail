Summary:     procmail Mail Delivery Agent
Summary(pl): procmail - dorêczyciel poczty (MDA)
Name:        procmail
Version:     3.13.1
Release:     4
Group:       Daemons
Group(pl):   Serwery
Copyright:   GPL
Source:      procmail-3.13.1.tar.gz
Patch0:      procmail-maildir.patch
Patch1:      procmail-locking.patch
Patch2:      procmail-nospoollock.patch
Buildroot:   /tmp/%{name}-%{version}-root/
Provides:    localmail procmail


%description
Most mail servers such as sendmail need to have a local delivery agent. 
Procmail can be used as the local delivery agent for you mail server.  It
supports a rich command set that allows you to pre-sort, archive, or re-mail
incoming mail automatically.  SmartList also needs procmail to operate.

This release is patched to add maildir delivery support, to remove locks
in directory deliveries, and to avoid automatically creating
/var/spool/mail/USERNAME.

%description -l pl
Wiele z serwerów pocztowych (np.: sendmail) wymagaj± programu do lokalnego
dostarczania poczty. Procmail mo¿e byæ u¿ywany w³a¶nie jako taki program.
Umo¿liwia on automatyczne sortowanie, archiwizacjê oraz przesy³anie 
przychodz±cej poczty. Jest podstaw± programu obs³ugi list dyskusyjnych
SmartList.

Procmail w tym pakiecie zawiera wsparcie dla folderów pocztowych Maildir/,
nie blokuje folderów pocztowych, które s± katalogami oraz nie tworzy
automatycznie folderu /var/spool/mail/USERNAME.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
echo "
" | make BASENAME=$RPM_BUILD_ROOT install


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/man/man1
install -d $RPM_BUILD_ROOT/usr/man/man5
install -d $RPM_BUILD_ROOT/usr/doc
install -d $RPM_BUILD_ROOT/var/spool/mail
chmod 1777 $RPM_BUILD_ROOT/var/spool/mail
install -s new/procmail $RPM_BUILD_ROOT/usr/bin
install -s new/lockfile $RPM_BUILD_ROOT/usr/bin
install -s new/formail $RPM_BUILD_ROOT/usr/bin
install -s new/mailstat $RPM_BUILD_ROOT/usr/bin
install new/formail.1 $RPM_BUILD_ROOT/usr/man/man1
install new/lockfile.1 $RPM_BUILD_ROOT/usr/man/man1
install new/procmail.1 $RPM_BUILD_ROOT/usr/man/man1
install new/procmailex.5 $RPM_BUILD_ROOT/usr/man/man5
install new/procmailrc.5 $RPM_BUILD_ROOT/usr/man/man5
install new/procmailsc.5 $RPM_BUILD_ROOT/usr/man/man5

gzip -9nf FAQ FEATURES HISTORY INSTALL README SmartList/* Artistic COPYING
gzip -9nf KNOWN_BUGS Manifest examples/*
gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644, root, root, 755)
%doc {FAQ,FEATURES,HISTORY,INSTALL,README,Artistic,COPYING}.gz
%doc {KNOWN_BUGS,Manifest}.gz
%doc examples/ SmartList/

%attr(755, root, mail) /usr/bin/procmail
%attr(755, root, mail) /usr/bin/lockfile
%attr(755, root, root) /usr/bin/formail
%attr(755, root, root) /usr/bin/mailstat
%attr(644, root, man)  /usr/man/man[15]/*

%changelog
* Sun May 02 1999 Artur Wróblewski <wrobell@posexperts.com.pl>
  [3.13.1-4]
- gzipped manpages and documentation
- polish translations
- file attributes from spec by Marcin Korzonek <mkorz@shadow.eu.org>
- non suid/sgid binaries
- %clean macro

* Tue Apr 06 1999 Bruce Guenter <bruce.guenter@qcc.sk.ca>

- Added nospoollock patch to avoid creating /var/spool/mail/USERNAME.
- Updated to procmail 3.13.1

* Mon Apr 05 1999 Bruce Guenter <bruce.guenter@qcc.sk.ca>

- Added maildir patch
- Added no-lock-directory patch

* Mon Apr 05 1999 James Bourne <jbourne@affinity-systems.ab.ca>

- updated to procmail 3.13

* Tue Jan 12 1999 James Bourne <jbourne@affinity-systems.ab.ca>

- added attr's to files section

* Thu Jan 07 1999 James Bourne <jbourne@affinity-systems.ab.ca>

- Rebuilt RPM and SRPM with pgp signature and proper spec file for rhcn.

* Thu Dec 17 1998 James Bourne <jbourne@affinity-systems.ab.ca>

- built RPM and SRPM.  only changes are that the spec file uses it's own
	install section and does not use the procmail install methods.
