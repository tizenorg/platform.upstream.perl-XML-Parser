Name:           perl-XML-Parser
%define cpan_name XML-Parser
Summary:        A perl module for parsing XML documents
Version:        2.41
Release:        9
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
AutoReqProv:    on
Url:            http://www.cpan.org/modules/by-module/XML/ 
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  libexpat-devel

%description
This module provides ways to parse XML documents. It is built on top of
 XML::Parser::Expat, which is a lower level interface to James Clark's expat
 library. Each call to one of the parsing methods creates a new instance of
 XML::Parser::Expat which is then used to parse the document. Expat options may
 be provided when the XML::Parser object is created. These options are then
 passed on to the Expat object on each parse call. They can also be given as
 extra arguments to the parse methods, in which case they override options
 given at XML::Parser creation time.

The behavior of the parser is controlled either by "Style" and/or "Handlers"
 options, or by "setHandlers" method. These all provide mechanisms for
 XML::Parser to set the handlers needed by XML::Parser::Expat. If neither
 Style nor Handlers are specified, then parsing just checks the document
 for being well-formed.

When underlying handlers get called, they receive as their first parameter
 the Expat object, not the Parser object.

You will find examples in
/usr/share/doc/packages/perl-XML-Parser/samples.  For documentation
read the XML::Parser and XML::Parser::Expat man pages.


%prep
%setup -n XML-Parser-%{version} -q

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
%{__make}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(0644,root,root,0755)

%changelog
