%define version 1.2.0
%define release 0
%define name    check_dir
%define _prefix /usr/lib/nagios/plugins/contrib

Summary:   Checks Nagios latency
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   GPL
Packager:  Matteo Corti <matteo.corti@id.ethz.ch>
Group:     Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source:    http://www.id.ethz.ch/people/allid_list/corti/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
Checks Nagios latency

%prep
%setup -q

%build

%install
make DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0644)
%doc AUTHORS ChangeLog NEWS README INSTALL TODO COPYING VERSION
%attr(0755, root, root) %{_prefix}/check_dir

%changelog
* Mon Sep 24 2007 Matteo Corti <matteo.corti@id.ethz.ch> - 1.2-0
- first RPM package

