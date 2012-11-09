Name:           perl-XML-Parser
Version:        2.36
Release:        3
Summary:        A low level Perl module for parsing XML either via trees or streaming

License:        GPL+ or Artistic
Url:            http://search.cpan.org/dist/XML-Parser/
Group:          Development/Libraries
Source0:        http://www.cpan.org/authors/id/M/MS/MSERGEANT/XML-Parser-%{version}.tar.gz

BuildRequires:  expat-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       "`perl
Requires:       $version))
Requires:       -V:version`";
Requires:       echo
Requires:       perl(:MODULE_COMPAT_%(eval

%description
This module provides ways to parse XML documents. It is built on top
of XML::Parser::Expat, which is a lower level interface to James
Clark's expat library. Each call to one of the parsing methods creates
a new instance of XML::Parser::Expat which is then used to parse the
document. Expat options may be provided when the XML::Parser object is
created. These options are then passed on to the Expat object on each
parse call. They can also be given as extra arguments to the parse
methods, in which case they override options given at XML::Parser
creation time.

%prep
%setup -q -n XML-Parser-%{version}
chmod 644 samples/{canonical,xml*}
perl -pi -e 's|^#!/usr/local/bin/perl\b|#!perl|' samples/{canonical,xml*}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="%{optflags}"

%check
make test

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*


%files
%defattr(-,root,root,-)
%{perl_vendorarch}/XML/*
%{perl_vendorarch}/auto/XML/*
%doc %{_mandir}/man3/*.3*
