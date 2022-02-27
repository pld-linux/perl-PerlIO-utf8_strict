#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	PerlIO
%define		pnam	utf8_strict
Summary:	PerlIO::utf8_strict - Fast and correct UTF-8 IO
Name:		perl-%{pdir}-%{pnam}
Version:	0.007
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PerlIO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9e8fba7f15c612c4f2ed2f961bf1141b
URL:		http://search.cpan.org/dist/PerlIO-utf8_strict/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a fast and correct UTF-8 PerlIO layer.
Unlike perl's default :utf8 layer it checks the input for correctness.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/PerlIO/utf8_strict.pm
%dir %{perl_vendorarch}/auto/PerlIO/utf8_strict
%attr(755,root,root) %{perl_vendorarch}/auto/PerlIO/utf8_strict/*.so
%{_mandir}/man3/*
