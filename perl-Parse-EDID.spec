%define	modname	Parse-EDID
%define	modver	1.0.4

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Extended display identification data (EDID) parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{modname}-%{modver}.tar.gz
BuildArch:	noarch

%description
This module provides some function to parse Extended Display Identification
Data binary data structures.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml META.json Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
