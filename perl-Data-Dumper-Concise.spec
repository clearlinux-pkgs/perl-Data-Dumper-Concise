#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Dumper-Concise
Version  : 2.023
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Data-Dumper-Concise-2.023.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Data-Dumper-Concise-2.023.tar.gz
Summary  : 'Less indentation and newlines plus sub deparsing'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-Dumper-Concise-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Data::Dumper::Concise - Less indentation and newlines plus sub deparsing
SYNOPSIS
use Data::Dumper::Concise;

%package dev
Summary: dev components for the perl-Data-Dumper-Concise package.
Group: Development
Provides: perl-Data-Dumper-Concise-devel = %{version}-%{release}
Requires: perl-Data-Dumper-Concise = %{version}-%{release}

%description dev
dev components for the perl-Data-Dumper-Concise package.


%package perl
Summary: perl components for the perl-Data-Dumper-Concise package.
Group: Default
Requires: perl-Data-Dumper-Concise = %{version}-%{release}

%description perl
perl components for the perl-Data-Dumper-Concise package.


%prep
%setup -q -n Data-Dumper-Concise-2.023
cd %{_builddir}/Data-Dumper-Concise-2.023

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Dumper::Concise.3
/usr/share/man/man3/Data::Dumper::Concise::Sugar.3
/usr/share/man/man3/Devel::Dwarn.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Data/Dumper/Concise.pm
/usr/lib/perl5/vendor_perl/5.30.1/Data/Dumper/Concise/Sugar.pm
/usr/lib/perl5/vendor_perl/5.30.1/Devel/Dwarn.pm
