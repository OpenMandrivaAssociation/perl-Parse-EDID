%define	modname	Parse-EDID
%define	modver	1.0.6

Summary:	Extended display identification data (EDID) parser
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module provides some function to parse Extended Display Identification
Data binary data structures.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml META.json Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
