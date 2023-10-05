Summary:	Python module to customize a process title
Name:		python3-setproctitle
Version:	1.3.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
URL:		http://pypi.python.org/pypi/setproctitle
BuildRequires:	rpmbuild(macros) >= 1.710
Source0:	https://pypi.debian.net/setproctitle/setproctitle-%{version}.tar.gz
# Source0-md5:	1c042d6717212de791c4f9b63e7b544e
BuildRequires:	python3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multiprocess systems, allowing to identify tasks each
forked process is busy with. This technique has been used by
PostgreSQL and OpenSSH.

It's based on PostgreSQL implementation which has proven to be
portable.

%prep
%setup -q -n setproctitle-%{version}

%build
%{__python3} setup.py \
	build -b build-3

%install
rm -rf $RPM_BUILD_ROOT

%py3_install \
	--root $RPM_BUILD_ROOT

chmod 0755 $RPM_BUILD_ROOT%{py3_sitedir}/setproctitle/*setproctitle*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/setproctitle
%{py3_sitedir}/setproctitle/__init__.py
%{py3_sitedir}/setproctitle/__pycache__
%{py3_sitedir}/setproctitle/py.typed
%attr(755,root,root) %{py3_sitedir}/setproctitle/*setproctitle.*.so
%{py3_sitedir}/setproctitle-*.egg-info
