Summary:	PostgreSQL module for Ruby
Summary(pl.UTF-8):	Moduł PostgreSQL dla Ruby
Name:		ruby-pg
Version:	0.13.2
Release:	2
License:	Ruby License
Group:		Development/Languages
Source0:	http://bitbucket.org/ged/ruby-pg/get/v%{version}.tar.gz
# Source0-md5:	6dfc70279ae5f8ea0d5cfb318086c5fd
URL:		http://rubyforge.org/projects/ruby-pg/
BuildRequires:	postgresql-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel >= 1:1.8.4-5
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-postgres
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostgreSQL module for Ruby.

%description -l pl.UTF-8
Moduł PostgreSQL dla Ruby.

%prep
%setup -qc
mv ged-ruby-pg-c79cd308363d/* .
cp %{_datadir}/setup.rb .

%build
%{__ruby} setup.rb config
%{__make} V=1 -C ext \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorarchdir},%{ruby_vendorlibdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -p ext/*.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_vendorlibdir}/pg.rb
%{ruby_vendorlibdir}/pg
%attr(755,root,root) %{ruby_vendorarchdir}/pg_ext.so
