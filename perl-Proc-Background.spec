%include	/usr/lib/rpm/macros.perl
%define	pdir	Proc
%define	pnam	Background
Summary:	Proc::Background perl module
Summary(pl):	Modu³ perla Proc::Background
Name:		perl-Proc-Background
Version:	1.07
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Provides:	perl(Proc::Generic)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc::Background - generic interface to place programs in background
processing.

%description -l pl
Proc::Background - umo¿liwia uruchamianie pogramów w tle.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/timed-process
%{perl_sitelib}/Proc/Background.pm
%dir %{perl_sitelib}/Proc/Background
%{perl_sitelib}/Proc/Background/Unix.pm
%{perl_sitelib}/Proc/Background/Win32.pm
%{_mandir}/man[13]/*
