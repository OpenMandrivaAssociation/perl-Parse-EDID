%define	modname	Parse-EDID

Summary:	Extended display identification data (EDID) parser
Name:		perl-%{modname}
Version:	1.0.7
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module provides some function to parse Extended Display Identification
Data binary data structures.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%make_install

%files
%doc README META.yml META.json Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
