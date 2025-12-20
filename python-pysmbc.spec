# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define module pysmbc

Summary:	Python bindings for the libsmbclient API from Samba
Name:		python-%{module}
Version:	1.0.25.1
Release:	1
Group:		Development/Python
License:	BSD
Url:		https://cyberelk.net/tim/data/pysmbc/
#Source0:	http://cyberelk.net/tim/data/pysmbc/%{module}-%{version}.tar.bz2
Source0:  https://files.pythonhosted.org/packages/source/p/pysmbc/pysmbc-%{version}.tar.gz
Patch0:		pysmbc-1.0.13_samba-4.0_libsmbclient_h.patch
Patch1:		pysmbc-python3-compilefixes.patch
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(python3)
%rename python-smbc

%description
Python bindings for the libsmbclient API, known as pysmbc. It was written
for use with system-config-printer, but can be put to other uses as well.

%prep
%setup -qn %{module}-%{version}
%autopatch -p1

%build
%py_build

%install
%py_install

%files
%{py3_platsitedir}/*.egg-info
%{py3_platsitedir}/smbc.*.so
