%include	/usr/lib/rpm/macros.perl
%define		pdir	Async
%define		pnam	Group
Summary:	Async-Group perl module
Summary(pl):	Modu³ perla Async-Group
Name:		perl-Async-Group
Version:	0.3
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Async-Group is a perl class to deal with simultaneous asynchronous
calls.

%description -l pl
Modu³ perla Async-Group.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/Async
%{perl_sitelib}/Async/Group.pm
%{_mandir}/man3/*
