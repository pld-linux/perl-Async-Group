%include	/usr/lib/rpm/macros.perl
Summary:	Async-Group perl module
Summary(pl):	Modu³ perla Async-Group
Name:		perl-Async-Group
Version:	0.3
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Async/Async-Group-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
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
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Async/Group
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%dir %{perl_sitelib}/Async
%{perl_sitelib}/Async/Group.pm

%dir %{perl_sitearch}/auto/Async
%{perl_sitearch}/auto/Async/Group

%{_mandir}/man3/*
