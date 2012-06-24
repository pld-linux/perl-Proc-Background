%include	/usr/lib/rpm/macros.perl
%define	pdir	Proc
%define	pnam	Background
Summary:	Proc-Background perl module
Summary(pl):	Modu� perla Proc-Background
Name:		perl-Proc-Background
Version:	1.06
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Provides:	perl(Proc::Generic)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-Background - generic interface to place programs in background
processing.

%description -l pl
Proc-Background - umo�liwia uruchamianie pogram�w w tle.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/timed-process
%{perl_sitelib}/Proc/Background.pm
%{perl_sitelib}/Proc/Background/Unix.pm
%{perl_sitelib}/Proc/Background/Win32.pm
%{_mandir}/man[13]/*
