%define __libtoolize    /bin/true

Name:		kio-sysinfo
Version:	1.8.2
Release:	%mkrel 6
Summary:	KIO Slave sysinfo:/
License:	LGPL
Group:          System/Libraries
URL:            http://www.kde-apps.org/content/show.php?content=58704
Source0:	http://download.tuxfamily.org/kiosysinfo/Sources/%name-%version.tar.gz
# fwang: Source1,2 from http://www.kde-look.org/content/show.php?content=61727
# Source1:	48x48/apps/kcmprocessor.png
Source1:	cpu.png
# Source2:	48x48/devices/system.png
Source2:	sysinfo.png
Patch0:         kio-sysinfo-1.7.1-fix-system-display.patch
# fwang: Patch for uz translation
Patch1:		kio-sysinfo-1.8.2-uz-translation.patch
BuildRequires:  kdelibs-devel
BuildRequires:  hal-devel
BuildRequires:  dbus-devel
BuildRequires:	libhd-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
Obsoletes:	sysinfo < 1.8.2-4

%description
KIO Slave sysinfo:/. It shows various information about your pc, 
like cpu, ram. kernel version, exc. It also shows the removable 
devices and partition (total space/available space) and you can open,
mount and unmount it from this KIO slave.

%files -f kio_sysinfo.lang
%defattr(-,root,root)
%{_libdir}/kde3/*
%{_datadir}/applications/kde/kfmclient_sysinfo.desktop
%{_datadir}/apps/sysinfo
%{_datadir}/mimelnk/application/x-sysinfo.desktop
%{_datadir}/services/ksysinfopart.desktop
%{_datadir}/services/sysinfo.protocol

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

cp -f %SOURCE1 about/images/cpu.png
cp -f %SOURCE2 about/images/sysinfo.png

%build

%configure2_5x --with-qt-dir=%{qt3dir} \
	--with-qt-includes=%{qt3include} \
	--with-qt-libraries=%{qt3lib}

%make

%install
rm -rf %{buildroot}

%makeinstall_std

#move mime to proper place
mv %buildroot/%{_datadir}/mimelnk/applications  %buildroot/%{_datadir}/mimelnk/application

%{find_lang} kio_sysinfo

%clean
rm -rf %{buildroot}
