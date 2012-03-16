Summary:	PostgreSQL module for Ruby
Summary(pl.UTF-8):	Moduł PostgreSQL dla Ruby
Name:		ruby-pg
Version:	0.13.2
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0:	http://bitbucket.org/ged/ruby-pg/get/v%{version}.tar.gz
# Source0-md5:	6dfc70279ae5f8ea0d5cfb318086c5fd
URL:		http://rubyforge.org/projects/ruby-pg/
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.277
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
%setup -q -n ged-ruby-pg-c79cd308363d
# -n pg-%{version}
#mv ged-ruby-pg-c79cd308363d pg-%{version}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_rubylibdir}/pg
%{ruby_rubylibdir}/pg.rb
%attr(755,root,root) %{ruby_archdir}/pg_ext.so
