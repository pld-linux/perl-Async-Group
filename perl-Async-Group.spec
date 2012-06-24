#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Async
%define		pnam	Group
Summary:	Async::Group - Perl class to deal with simultaneous asynchronous calls
Summary(pl):	Async::Group - klasa Perla do obs�ugi jednoczesnych wywo�a� asynchronicznych
Name:		perl-Async-Group
Version:	0.3
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a18d7ef93a00825ad8d7df2ef65c7cc
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Async::Group is a Perl class which enables you to call several
asynchronous routines.  Each routine may have their own callback. When
all the routine are over (i.e. all their callback were called),
Async::Group will call the global callback given by the user.

%description -l pl
Async::Group to klasa Perla umo�liwiaj�ca wywo�ywanie kilku
asynchronicznych podprogram�w. Ka�dy z nich mo�e mie� swoje w�asne
po��czenie zwrotne. Gdy wszystkie te podprogramy si� zako�cz� (tzn.
zostan� wywo�ane ich po��czenia zwrotne), Async::Group wywo�a globalne
po��czenie zwrotne podane przez u�ytkownika.

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
%dir %{perl_vendorlib}/Async
%{perl_vendorlib}/Async/Group.pm
%{_mandir}/man3/*
