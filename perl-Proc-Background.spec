%define	pdir	Proc
%define	pnam	Background
%include	/usr/lib/rpm/macros.perl
Summary:	Proc-Background perl module
Summary(pl):	Modu³ perla Proc-Background
Name:		perl-Proc-Background
Version:	1.06
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
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
Proc-Background - umo¿liwia uruchamianie pogramów w tle.

%prep
%setup -q -n Proc-Background-%{version}

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
