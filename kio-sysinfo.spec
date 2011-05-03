# svn co svn://anonsvn.kde.org/home/kde/trunk/playground/base/kio_sysinfo/
%define oname  kio_sysinfo
%define svn    1230316

Name: kio-sysinfo
Version: 1.8.3
Release: %mkrel -c %svn 1
Summary: KIO Slave sysinfo:/
License: LGPL
Group: System/Libraries
URL:     http://websvn.kde.org/trunk/playground/base/kio_sysinfo/ 
Source0: %oname-%svn.tar.xz
Source1:	cpu.png
Source2:	sysinfo.png
BuildRequires: kdelibs4-devel
#BuildRequires: dbus-devel
BuildRequires: libhd-devel
BuildRoot: %{_tmppath}/%{name}-%{version}
Obsoletes: sysinfo < 1.8.2-4
Obsoletes: kde3-kio-sysinfo  < 1.8.2-11

%description
KIO Slave sysinfo:/. It shows various information about your pc, 
like cpu, ram. kernel version, exc. It also shows the removable 
devices and partition (total space/available space) and you can open,
mount and unmount it from this KIO slave.

%files -f kio_sysinfo.lang
%defattr(-,root,root)
%{_kde_libdir}/kde4/*
%{_kde_appsdir}/sysinfo
%{_kde_datadir}/applications/kde4/kfmclient_sysinfo.desktop
%{_kde_datadir}/kde4/services/ksysinfopart.desktop
%{_kde_datadir}/kde4/services/sysinfo.protocol
%{_kde_datadir}/mime/packages/x-sysinfo.xml

#--------------------------------------------------------------------

%prep
%setup -qn %{oname}

%build
%cmake_kde4 -DSYSINFO_DISTRO:STRING=mandriva
%make

%install
rm -rf %buildroot

%makeinstall_std

%{find_lang} kio_sysinfo

%clean
rm -rf %{buildroot}
