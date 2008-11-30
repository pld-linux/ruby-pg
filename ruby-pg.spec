Summary:	PostgreSQL module for Ruby
Summary(pl.UTF-8):	Moduł PostgreSQL dla Ruby
Name:		ruby-pg
Version:	0.7.9.2008.10.13
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0: http://rubyforge.org/frs/download.php/45156/ruby-pg-0.7.9.2008.10.13.tar.gz
# Source0-md5:	4ecf1004bb5f643a297ff22e075e1606
URL:		http://rubyforge.org/projects/ruby-pg/
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8.4-5
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-postgres
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostgreSQL module for Ruby.

%description -l pl.UTF-8
Moduł PostgreSQL dla Ruby.

%prep
%setup -q -n %{name}

%build
cd ext
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}

cd ext
%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{ruby_archdir}/pg.so
