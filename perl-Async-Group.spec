%include	/usr/lib/rpm/macros.perl
Summary:	Async-Group perl module
Summary(pl):	Modu³ perla Async-Group
Name:		perl-Async-Group
Version:	0.3
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Async/Async-Group-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Async-Group is a perl class to deal with simultaneous asynchronous
calls.

%description -l pl
Modu³ perla Async-Group.

%prep
%setup -q -n Async-Group-%{version}

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
