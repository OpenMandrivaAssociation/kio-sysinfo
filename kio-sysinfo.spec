%define oname  kio_sysinfo
%define svn    822583

Name: kio-sysinfo
Version: 1.8.3
Release: %mkrel 0.%svn.3
Summary: KIO Slave sysinfo:/
License: LGPL
Group: System/Libraries
URL:     http://websvn.kde.org/trunk/playground/base/kio_sysinfo/ 
Source0: %name-%version.%svn.tar.bz2
# Source1:	48x48/apps/kcmprocessor.png
Source1:	cpu.png
# Source2:	48x48/devices/system.png
Source2:	sysinfo.png
BuildRequires: kdelibs4-devel
BuildRequires: hal-devel
BuildRequires: dbus-devel
BuildRequires: libhd-devel
BuildRoot: %{_tmppath}/%{name}-%{version}
Obsoletes: sysinfo < 1.8.2-4

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
%setup -q -n %{name}

#%__cp -f %SOURCE1 about/images/cpu.png
#%__cp -f %SOURCE2 about/images/sysinfo.png

%build
%cmake_kde4
%make

%install
rm -rf %buildroot

%makeinstall_std -C build

%{find_lang} kio_sysinfo

%clean
rm -rf %{buildroot}
