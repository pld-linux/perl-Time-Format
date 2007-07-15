#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Format
Summary:	Easy-to-use date/time formatting
Summary(pl.UTF-8):	Łatwe w użyciu formatowanie daty/czasu
Name:		perl-Time-Format
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f19a947ae3c2490a3edc9ca859ec43b3
URL:		http://search.cpan.org/dist/Time-Format/
BuildRequires:	perl-DateTime
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy-to-use date/time formatting.

%description -l pl.UTF-8
Łatwe w użyciu formatowanie daty/czasu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Time/*.pm
%{_mandir}/man3/*
