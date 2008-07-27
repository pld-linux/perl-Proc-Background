#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Proc
%define		pnam	Background
Summary:	Proc::Background Perl module - generic interface to background process management
Summary(pl.UTF-8):	Moduł Perla Proc::Background - ogólny interfejs do zarządzania procesami w tle
Name:		perl-Proc-Background
Version:	1.08
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e02f11b627332169c37cab39cccf6451
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(Proc::Generic)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc::Background Perl module is a generic interface for placing
processes in the background on Unix platforms. This module lets you
start, kill, wait on, retrieve exit values, and see if background
processes still exist.

%description -l pl.UTF-8
Moduł Perla Proc::Background stanowi podstawowy interfejs dla
umieszczania procesów w tle na platformach uniksowych. Moduł ten
umożliwia uruchamianie, zabijanie procesów, oczekiwanie na ich
zakończenie i odbieranie kodu powrotu procesu. Za jego pomocą można
też zobaczyć, jakie procesy nadal działają w tle.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/timed-process
%{perl_vendorlib}/Proc/Background.pm
%dir %{perl_vendorlib}/Proc/Background
%{perl_vendorlib}/Proc/Background/Unix.pm
#%%{perl_vendorlib}/Proc/Background/Win32.pm
%{_mandir}/man1/*
%{_mandir}/man3/Proc::Background.*
%{_mandir}/man3/Proc::Background::Unix*
#%%{_mandir}/man3/Proc::Background::Win32*
