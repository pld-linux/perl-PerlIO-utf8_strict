#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	PerlIO
%define		pnam	utf8_strict
Summary:	PerlIO::utf8_strict - fast and correct UTF-8 I/O
Summary(pl.UTF-8):	PerlIO::utf8_strict - szybkie i poprawne we/wy UTF-8
Name:		perl-%{pdir}-%{pnam}
Version:	0.010
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/PerlIO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d90ca967f66e05ad9221c79060868346
URL:		https://metacpan.org/dist/PerlIO-utf8_strict
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a fast and correct UTF-8 PerlIO layer. Unlike
Perl's default :utf8 layer it checks the input for correctness.

%description -l pl.UTF-8
Ten moduł zapewnia warstwę PerlIO do szybkiego i poprawnego UTF-8. W
przeciwieństwie do domyślnej warstwy :utf8 Perla, sprawdza wejście pod
kątem poprawności.

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
%doc Changes README
%{perl_vendorarch}/PerlIO/utf8_strict.pm
%dir %{perl_vendorarch}/auto/PerlIO/utf8_strict
%attr(755,root,root) %{perl_vendorarch}/auto/PerlIO/utf8_strict/utf8_strict.so
%{_mandir}/man3/PerlIO::utf8_strict.3pm*
