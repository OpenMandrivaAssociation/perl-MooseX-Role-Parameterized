%define upstream_name    MooseX-Role-Parameterized
%define upstream_version 0.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Metaclass for parameterizable roles
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Moose)
BuildRequires: perl(Test::More) >= 0.96
BuildRequires: perl(Test::Fatal)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


