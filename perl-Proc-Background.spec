%include	/usr/lib/rpm/macros.perl
Summary:	Proc-Background perl module
Summary(pl):	Modu³ perla Proc-Background
Name:		perl-Proc-Background
Version:	0.02
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Proc/Proc-Background-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
Provides:	perl(Proc::Generic)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-Background - generic interface to place programs in background
processing.

%description -l pl
Proc-Background - umo¿liwia uruchamianie pogramów w tle.

%prep
%setup -q -n Proc-Background-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Proc/Background
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/timed-process

%{perl_sitelib}/Proc/Background.pm
%{perl_sitelib}/Proc/Background/Unix.pm
%{perl_sitelib}/Proc/Background/Win32.pm
%{perl_sitearch}/auto/Proc/Background

%{_mandir}/man[13]/*
