%define upstream_name    MooseX-Role-Parameterized
%define upstream_version 0.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Metaclass for parameterizable roles
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Moose)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Your parameterized role consists of two new things: parameter declarations
and a 'role' block.

Parameters are declared using the the /parameter manpage keyword which very
much resembles the Moose/has manpage. You can use any option that the
Moose/has manpage accepts. The default value for the 'is' option is 'ro' as
that's a very common case. Use 'is => 'bare'' if you want no accessor.
These parameters will get their values when the consuming class (or role)
uses the Moose/with manpage. A parameter object will be constructed with
these values, and passed to the 'role' block.

The 'role' block then uses the usual the Moose::Role manpage keywords to
build up a role. You can shift off the parameter object to inspect what the
consuming class provided as parameters. You use the parameters to customize
your role however you wish.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1mdv2011.0
+ Revision: 659978
- update to new version 0.26

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.250.0-2
+ Revision: 657453
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1
+ Revision: 643409
- update to new version 0.25

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 625276
- update to new version 0.23

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 601985
- update to new version 0.22
- new version

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 596622
- update to 0.20

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 552420
- update to 0.19

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.1
+ Revision: 518078
- update to 0.18

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.1
+ Revision: 504491
- update to 0.17

* Fri Feb 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.1
+ Revision: 501146
- update to 0.16

* Wed Jan 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 486604
- update to 0.15

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 474653
- update to 0.14

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 471162
- import perl-MooseX-Role-Parameterized


* Sun Nov 29 2009 cpan2dist 0.13-1mdv
- initial mdv release, generated with cpan2dist
