Name:		diskimage-builder
Summary:	Image building tools for OpenStack
Version:	0.0.5
Release:	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://launchpad.net/diskimage-builder
Source0:	http://tarballs.openstack.org/diskimage-builder/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-d2to1
BuildRequires: python-pbr

Requires: kpartx
Requires: qemu-img
Requires: busybox
Requires: curl

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/%{name}/lib
mkdir -p %{buildroot}%{_datadir}/%{name}/elements

install -p -D -m 644 lib/* %{buildroot}%{_datadir}/%{name}/lib
cp -vr elements/ %{buildroot}%{_datadir}/%{name}

# explicitly remove config-applier since it does a pip install
rm -rf %{buildroot}%{_datadir}/%{name}/elements/config-applier

%description
Components of TripleO that are responsible for building disk images.

%files
%doc LICENSE
%doc docs/ci.md
%{_bindir}/*
%{python_sitelib}/diskimage_builder*
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/elements

%changelog
* Wed Oct 9 2013 Jeff Peeler <jpeeler@redhat.com> 0.0.5-1
- rebase to 0.0.5

* Mon Sep 16 2013 Jeff Peeler <jpeeler@redhat.com> 0.0.1-7
- add patch to allow proper Fedora image creation when using vm element

* Fri Sep 13 2013 Jeff Peeler <jpeeler@redhat.com> 0.0.1-6
- add patches to ccd7b86b606e678bf7281baff05c420b089c5d8f (fixes kpartx issue)

* Thu Sep 5 2013 Jeff Peeler <jpeeler@redhat.com> 0.0.1-5
- rebase to a495079695e914fa7ec93292497bfc2471f41510
- Source moved from stackforge to openstack
- added curl requires
- switched to pbr
- remove all sudo related files as they are no longer used

* Tue Aug 13 2013 Jeff Peeler <jpeeler@redhat.com> 0.0.1-4
- removed config-applier element

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Jeff Peeler <jpeeler@redhat.com> 0.0.1-2
- rebased and dropped patches

* Mon Jul 29 2013 Jeff Peeler <jpeeler@redhat.com> 0.0.1-1
- initial package straight from github commit sha
